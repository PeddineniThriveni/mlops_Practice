import ssl
import certifi
ssl._create_default_https_context = lambda:ssl.create_default_context(cafile=certifi.where())
import pandas as pd
from sklearn.datasets import fetch_california_housing
import os

def load_and_save_data():
    # Create folder if not exists
    os.makedirs("Data/Raw", exist_ok=True)
raw_data_dir = os.path.join(os.getcwd(), "Data", "Raw")
#os.makedirs(raw_data_dir, exist_ok=True)


data=fetch_california_housing(as_frame= True)
df=data.frame

df.to_csv(os.path.join(raw_data_dir,"house_data.CSV"), index=False)

if __name__=='__main__':
    load_and_save_data()
