from datetime import datetime
from json import dumps, loads
import pandas as pd
import numpy as np
from flask import Blueprint, Flask, jsonify, flash, request,redirect, send_from_directory, json, session
import os
from werkzeug.utils import secure_filename
from report_format import DarTReportFormat
from constants import UPLOAD_FOLDER



bp = Blueprint('dartview', __name__)
# home = Path.home().absolute().as_posix()
# mypath = home + "/flask"
# if not os.path.isdir(mypath):
#     os.makedirs(mypath)


#UPLOAD_FOLDER =constants.UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'csv'}
ALLELE_ID= "AlleleID"
SNP_MARKER_IDENTIFIER= '|'
report_Mcall_rate= pd.Series()
DART_HEADERS ='*'
genotypic_data = pd.DataFrame()

def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/', methods=['GET', 'POST'])
def load_file():
    if request.method=='GET':
        print("getting fish")
        return send_from_directory('client/public', 'index.html')
    
    
@bp.route('/base')
def base():
    return send_from_directory('client/public', 'index.html')

@bp.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@bp.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    
    if request.method=='POST':

        
        if 'file' not in request.files: 
            flash('No file part', 'error')
            return redirect(request.url)
        file= request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            if not allowed_file(file.filename):
                flash('File type not allowed', 'error')
                return redirect("/base")
            #Secure the filename before storing it directly to the filesystem
            #geneate a unique filename by appending a random hex string
            
            filename = secure_filename(file.filename)
            new_filename= f'{filename.split(".")[0]}-{os.urandom(15).hex()}.csv'.replace(" ", "")
            
            session['filename'] = new_filename
            file.save(os.path.join(UPLOAD_FOLDER, new_filename))
            data = pd.read_csv(os.path.join(UPLOAD_FOLDER, new_filename), dtype=str, header=None)
            #Get first column
            first_column = data.iloc[:,0]
            
            sample_meta_row =0
            for val in first_column:
                if val==DART_HEADERS:
                    sample_meta_row+=1
                else:
                    break
            #prinmt marker names
            #print(first_column.loc[sample_meta_row+1:])
            #print("sample meta row is", first_column.iloc[sample_meta_row+2:20])
            # Use Marker id column to check the report type
            dart_report_format = check_report_format(first_column.iloc[sample_meta_row+1:21])
            print("dart report format is", dart_report_format)
            
           #subset with sample meta data
            sample_df= data.iloc[:sample_meta_row+1]
            first_row = sample_df.iloc[0]
            #get number of markers , subtract 1 to account for the header row
            markers_number= len(first_column)-sample_meta_row-1
            #markers_number = int(markers_number/2 if dart_report_format==2 else markers_number)

            #print("Markers number is", markers_number)

            
            #remove *s from the sample_df
            sample_meta_list = []

            start_genotypic_col= 0
            #Get start of genotypic data
            for val in first_row:
                if val == DART_HEADERS:
                    start_genotypic_col+=1
                else:
                    break

            sample_df2 = sample_df.iloc[:, start_genotypic_col:]

            for row in sample_df2.iterrows():
                sample_meta_list.append(row)


            #print(sample_meta_list[0])

            samples_number= len(first_row)- start_genotypic_col
            
            allele_id_pos= sample_meta_row

            #Remove all columns above the allele id position
            data = data.iloc[allele_id_pos:,:]

            #Assign first row as the header
            data_header = data.iloc[0]
            data= data[1:]
            
            data.columns= data_header
        
            marker_list = data.iloc[:,0]
            marker_metadata = data_header.iloc[0:start_genotypic_col]
           
            
            
            #report_Mcall_rate= data.CallRate .apply(lambda x: float(x))
            #print("report call rate values are",report_Mcall_rate )
            #if 1==1:
            #genotypic_data.style.pipe(make_pretty)
            #return render_template('basic_table.html', row_data=list(report_Mcall_rate.values.tolist()))
            
            #Get the genotypic data from this-- remove the meta data
            genotypic_data= data.iloc[:, start_genotypic_col:]
            #genotypic_data.insert(0,"AlleleID", marker_column,True)
            
            #genotypic_data.columns = genotypic_data.iloc[0]
            
            
            #genotypes_number = genotypic_data.iloc[0].count()
        
            #genotypic_data = genotypic_data.replace(["-"], np.nan)
            #genotypic_data.index = first_column.loc[sample_meta_row+1:]
            #print(genotypic_data.columns)
           # my_list= []
            #for genotype, score in genotypic_data.items():
                #my_list.append(str(score))
               # print(score)
            #print(type(my_list[0]))
            #return render_template('genotypic_table.html', row_data=genotypic_data.to_csv(index=False))
                 
            

            # calculated_Mcall_rate= genotypic_data.apply("count", axis=1)
            # genotypic_data_nan= genotypic_data.replace(["-"], np.nan)
            # print(genotypic_data.T)
            # calculated_Scall_rate = genotypic_data_nan.apply("count", axis=0)
           # print(calculated_Scall_rate)

            # calculated_Mcall_rate= calculated_Mcall_rate.apply(lambda x: x/samples_number)

            # calculated_Scall_rate = calculated_Scall_rate.apply(lambda x: x/markers_number)
            #print(report_Mcall_rate)
            #return render_template('basic_table.html', row_data=list(report_Mcall_rate.values.tolist()))
            #return  genotypic_data.to_json(orient='records')
            #return redirect(url_for('display_data'))

            #MAF= calculate_maf(genotypic_data, samples_number)

            #genotypic_data.to_csv(path_or_buf=os.path.join("/home/moses/flask/flask-tables/templates", "genoptype.csv"),na_rep="-", index=False)
            #return render_template('genotypic_table.html')
            

            # df = pd.DataFrame({
            #     "metadata_name": ["Report CallRate", "Calculated CallRate","MAFF"],
            #     "min": [np.min(report_Mcall_rate), np.min(calculated_Mcall_rate), np.min(MAF)],
            #     "mean": [np.mean(report_Mcall_rate), np.mean(calculated_Mcall_rate), np.mean(MAF)],
            #     "max": [np.max(report_Mcall_rate), np.max(calculated_Mcall_rate), np.max(MAF)]
            # }, index=["row0","row1", "row1"])

           
            #return render_template("basic_table.html",row_data=list(df.values.tolist()))
            # genotypic_data.reset_index(drop=True, inplace=True)
            # marker_column.reset_index(drop=True, inplace=True)
            # result= marker_column.join(genotypic_data)
            # result.set_index('AlleleID',inplace=True)
          
            # result2 = result.to_json(orient="columns")
            # parsed= loads(result2)
            # print(dumps(parsed, indent=4))
            sample_list = genotypic_data.columns.tolist()
            
            data = genotypic_data.to_numpy().tolist()
            data.append(marker_list.to_numpy().tolist())
            data.append(sample_list)
            data.append(marker_metadata.to_numpy().tolist())
        
            json_data =  json.dumps(data)
            

            return json_data
          
        

        
def check_report_format(first_column):
    #pick the first 6 markers ids values for comparison and store in a list
    marker_id_list= []
    
    count =0
    for val in first_column:
        if count ==6:
            break
        count+=1
        marker_id_list.append(val)
    
    #Check for silico DArT
    if  SNP_MARKER_IDENTIFIER not in marker_id_list[0]:
        return DarTReportFormat.SILICO_DART.name
    # else its a SNP check if 2 or 1 row format, Hapamap later
    else:
        filtered_marker_id_list= [marker_id.split(SNP_MARKER_IDENTIFIER)[0] for marker_id in  marker_id_list]
        print("filtered marker list", filtered_marker_id_list)
        if len(filtered_marker_id_list) > len(set(filtered_marker_id_list)):
            return DarTReportFormat.SNP_TWO_ROW.name
        return DarTReportFormat.SNP_ONE_ROW.name
    
def calculate_maf(genotypic_data, samples_number):
    ones = genotypic_data.apply(lambda x: x=='1').apply("sum", axis=1)
    ones.index= range(len(ones))
            
    zeros = genotypic_data.apply(lambda x: x=='0', axis=1).apply("sum", axis=1)
    zeros.index= range(len(zeros))
    twos = genotypic_data.apply(lambda x: x=='2', axis=1).apply("sum", axis=1)
    twos.index= range(len(twos))
    NAs = genotypic_data.apply(lambda x: x.isna(), axis=1).apply("sum", axis=1)
    NAs.index= range(len(NAs))
        
    MAF = []
    for i in range(len(ones)):
        MAF.append(np.sort([ones[i], zeros[i], twos[i]])[1]/(samples_number - NAs[i]))
    return MAF

def sort_by_column(genotypic_data, column_name):
    return genotypic_data.sort_values(by=[column_name])
   


def make_pretty(styler):
    styler.background_gradient(axis=None, vmin=1, vmax=5, cmap="YlGnBu")
    return styler



    



