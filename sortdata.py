from flask import json, Blueprint
DART_HEADERS ='*'
import pandas as pd
import numpy as np
import os
UPLOAD_FOLDER = "/home/moses/flask"
bp = Blueprint("sortdata", __name__)

@bp.route('/sort_data')
def display_data():

    data = pd.read_csv(os.path.join(UPLOAD_FOLDER, "sort-data.csv"), dtype=str, header=None)
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

    #Remove all columns above the allele id position
    #data_with_headers = data_with_headers.iloc[allele_id_pos:,:]

    
         
    
    data_header= data_with_headers.iloc[0]
    data_with_headers= data_with_headers[1:]
    data_with_headers.columns= data_header
           
    sorted_data= data_with_headers.sort_values(by="CallRate", ascending=True)
    
    genotypic_data= sorted_data.iloc[:, start_genotypic_col:]
    
    #print(genotypic_data)
    #genotypic_data= genotypic_data.iloc[1:]
    data =  json.dumps(genotypic_data.to_numpy().tolist())
    return data