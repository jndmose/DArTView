from flask import json, Blueprint, session
DART_HEADERS ='*'
import pandas as pd
import numpy as np
import os
UPLOAD_FOLDER = "/home/moses/flask"
bp = Blueprint("sortdata", __name__)

@bp.route('/sort_data')
def display_data():

    data = pd.read_csv(os.path.join(UPLOAD_FOLDER, session['filename']), dtype=str, header=None)
    #Get first column
    first_column = data.iloc[:,0]         
    sample_meta_row =0
    for val in first_column:
        if val==DART_HEADERS:
            sample_meta_row+=1
        else:
            break
           
    sample_df= data.iloc[:sample_meta_row+1]
    data_with_headers= data.iloc[sample_meta_row:]
    
    
   
    first_row = sample_df.iloc[0]
            
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
            
    allele_id_pos= sample_meta_row

    data_header= data_with_headers.iloc[0]
    data_with_headers= data_with_headers[1:]
    data_with_headers.columns= data_header
    genotypic_data= data_with_headers.iloc[:, start_genotypic_col:]
    genotypic_data_nan= genotypic_data.replace(["-"], np.nan)
    calculated_Mcall_rate= genotypic_data_nan.apply("count", axis=1)
    calculated_Scall_rate = genotypic_data_nan.apply("count", axis=0)
    data_with_headers["MarkerCallRate"]= calculated_Mcall_rate
     
    sorted_data= data_with_headers.sort_values(by="MarkerCallRate", ascending=False,kind='mergesort' )

    sorted_data= sorted_data.drop(['MarkerCallRate'], axis=1)
 
    genotypic_data= sorted_data.iloc[:, start_genotypic_col:]
    
    genotypic_data_T = genotypic_data.T
    data_header = genotypic_data_T.columns
            
    genotypic_data_T.columns= range(len(data_header))

    genotypic_data_T[len(genotypic_data_T.columns)]=calculated_Scall_rate
    genotypic_data_T.rename(columns={genotypic_data_T.columns[len(genotypic_data_T.columns)-1]:"SampleCallRate"}, inplace=True)
    
    sorted_data_T = genotypic_data_T.sort_values(by="SampleCallRate", ascending=False, kind="mergesort")
    
    sorted_data_T= sorted_data_T.drop(['SampleCallRate'], axis=1)

    data =  json.dumps(sorted_data_T.T.to_numpy().tolist())
    return data