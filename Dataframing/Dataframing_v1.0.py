import os
import csv
import numpy as np
from tqdm import tqdm

def Dataframe(inputs_in_path, outputs_in_path, inputs_in_df, outputs_in_df, df_path):

    inputs = os.listdir(inputs_in_path)
    outputs = os.listdir(outputs_in_path)

    with open(df_path, 'a+') as f:

        writer = csv.writer(f)

        writer.writerow(['InputImages', 'MaskImages', 'TargetImages'])

        for j in tqdm(inputs, leave=False):
            for i in tqdm(outputs, leave=False):

                if j[:11] == i[:11] and j[-6:] != i[-6:]:
                                            
                    df_data = [inputs_in_df + j, outputs_in_df + i, outputs_in_df + j]

                    writer.writerow(df_data)
                                                            
    print('Done dataframing.')

Dataframe = Dataframe(inputs_in_path='/path/to/input/images/',
                      outputs_in_path='/path/to/output/and/mask/images/',
                      inputs_in_df='/path/to/input/images/saved/in/the/dataframe/',
                      outputs_in_df='/path/to/output/and/mask/images/saved/in/the/dataframe/',
                      df_path='/path/Dataframe.csv')
