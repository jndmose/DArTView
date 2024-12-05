from flask import json, Blueprint, session, request
from itertools import compress
from .constants import UPLOAD_FOLDER

DART_HEADERS ='*'
import pandas as pd
import numpy as np
import os
from pathlib import Path

# home = Path.home().absolute().as_posix()
# mypath = home + "/flask"
# if not os.path.isdir(mypath):
#     os.makedirs(mypath)


# UPLOAD_FOLDER =mypath
bp = Blueprint("sortdata", __name__)

@bp.route('/sort_data',  methods=['GET', 'POST'])
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
    sorted_data= data_with_headers
    sort_criteria = request.json
    new_dict = {key: val for key, val in sort_criteria.items() if val != "-unsorted-"}
    if(not new_dict):
        return json.dumps(genotypic_data.to_numpy().tolist())
    
    if("metadata1" in new_dict):
        metadata = new_dict["metadata1"]
        sort_order= new_dict["sortorder1"]
        if(metadata=="SampleCallRate"):
            sampleCallRate= calculateSampleCallRate(data_with_headers, start_genotypic_col)
            sorted_data=Sort_with_samplecallrate(data_with_headers, sampleCallRate, start_genotypic_col,sort_order)
           
         
        else:
            markerCallRate = calculateMarkerCallRate(data_with_headers,start_genotypic_col)
            data_with_headers["MarkerCallRate"]= markerCallRate  
            sorted_data= data_with_headers.sort_values(by=metadata, ascending=sort_order=='Ascending',kind='mergesort')
            sorted_data= sorted_data.drop([metadata], axis=1)
            
    
    if("metadata2" in new_dict):
        metadata = new_dict["metadata2"]
        sort_order= new_dict["sortorder2"]
        if(metadata=="SampleCallRate"):
            sampleCallRate= calculateSampleCallRate(sorted_data, start_genotypic_col)
            sorted_data=Sort_with_samplecallrate(sorted_data, sampleCallRate, start_genotypic_col, sort_order)
        
        else:
            markerCallRate= calculateMarkerCallRate(sorted_data,start_genotypic_col)
            print(markerCallRate)
            sorted_data["MarkerCallRate"]= calculateMarkerCallRate(sorted_data,start_genotypic_col)
            #print(sorted_data)
            
            sorted_data= sorted_data.sort_values(by=metadata, ascending=sort_order=='Ascending',kind='mergesort')
           #print(sorted_data.iloc[:, start_genotypic_col:])
            sorted_data= sorted_data.drop([metadata], axis=1)
          
           
        
        
    

    data =  json.dumps(sorted_data.iloc[:, start_genotypic_col:].to_numpy().tolist())
    return data

def Sort_with_samplecallrate(data, sampleCallrate, start_genotypic_col, sort_order):
    
    metadata_data = data.iloc[:,:start_genotypic_col]
    genotypic_data= data.iloc[:, start_genotypic_col:]
    genotypic_data_T = genotypic_data.T
    
    data_header = genotypic_data_T.columns
            
    genotypic_data_T.columns= range(len(data_header))

    genotypic_data_T[len(genotypic_data_T.columns)]=sampleCallrate
    genotypic_data_T.rename(columns={genotypic_data_T.columns[len(genotypic_data_T.columns)-1]:"SampleCallRate"}, inplace=True)
    
    sorted_data_T = genotypic_data_T.sort_values(by="SampleCallRate", ascending=sort_order=='Ascending', kind="mergesort")
    
    
    sorted_data_T= sorted_data_T.drop(['SampleCallRate'], axis=1)
    new_data = sorted_data_T.T
    metadata_data.reset_index(drop=True, inplace=True)
    new_data.reset_index(drop=True, inplace=True)
    #print(metadata_data)
   
    result= metadata_data.join(new_data)
    
    return result

def calculateMarkerCallRate(data, start_genotypic_column):
    genotypic_data =data.iloc[:, start_genotypic_column:]
    genotypic_data_nan= genotypic_data.replace(["-"], np.nan)
    calculated_Mcall_rate= genotypic_data_nan.apply("count", axis=1)
    return calculated_Mcall_rate

def calculateSampleCallRate(data, start_genotypic_column):
    genotypic_data= data.iloc[:, start_genotypic_column:]
    genotypic_data_nan= genotypic_data.replace(["-"], np.nan)
    
    calculated_Scall_rate = genotypic_data_nan.apply("count", axis=0)
    return calculated_Scall_rate
