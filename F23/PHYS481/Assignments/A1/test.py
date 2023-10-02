import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



DS_1_path = "DATASET_1.txt.TXT" # RELATIVE PATH OF THE CHOSEN DATA SET

DS_2_path = "DATASET_2.txt.TXT"

DS_3_path = "DATASET_3_S.txt.TXT"



def import_dataset(file_name):
  '''This function will import the data from the specified file and return a pandas dataframe'''
  return pd.read_csv(
        file_name, 
        skiprows=19, 
        names=['Entry','ArdTime','ADC', 'SiPM', 'Deadtime', 'Temp'], 
        lineterminator='\n', 
        sep='\s+', 
        encoding='unicode_escape', 
        engine='python'
    )



dataset_1 = import_dataset(DS_1_path)
dataset_2 = import_dataset(DS_2_path)
dataset_3 = import_dataset(DS_3_path)


# converting the ArdTime column from milliseconds to seconds for all datasets

dataset_1.ArdTime = dataset_1.ArdTime/1000 # converting the ArdTime column from milliseconds to seconds for dataset_1
dataset_2.ArdTime = dataset_2.ArdTime/1000 # converting the ArdTime column from milliseconds to seconds for dataset_2
dataset_3.ArdTime = dataset_3.ArdTime/1000 # converting the ArdTime column from milliseconds to seconds for dataset_3

dataset_1.Deadtime = dataset_1.Deadtime/1000 # converting the Deadtime column from milliseconds to seconds for dataset_1
dataset_2.Deadtime = dataset_2.Deadtime/1000 # converting the Deadtime column from milliseconds to seconds for dataset_2
dataset_3.Deadtime = dataset_3.Deadtime/1000 # converting the Deadtime column from milliseconds to seconds for dataset_3

