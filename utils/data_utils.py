import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

from path_config import *


class DataLoader(object):
    '''
    '''
    def __init__(self):
        self.df_rki = get_RKI_file()
        self.df_landkreise = pd.read_csv(get_Landkreise_file(), encoding = "utf-8", sep=';').drop(columns=['LandkreisId'])


    def calling_api(self):
        '''
        Calling the API, initiate the DB interface and scrape the latest data from web.
        '''
        db = DB_interface()
        db.update_RKI_csv()
        db.update_RKI_landkreise_csv()


    def compute_population(self):
        # Compute the whole population of Germany via dataset 'landkreise.csv'
        self.df_landkreise['Bevoelkerung'] = self.df_landkreise['Bevoelkerung'].str.replace(" ","")
        self.df_landkreise['Bevoelkerung'] = self.df_landkreise['Bevoelkerung'].astype(int)
        return (self.df_landkreise['Bevoelkerung'].sum())
