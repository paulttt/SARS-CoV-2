import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

from path_config import *


class DataLoader(object):
    '''
    Taking the data from the RKI and prepare it for the SEIR model.
    '''
    def __init__(self):
        #self.df_rki = self.get_rki_dataframe()
        self.df_rki = pd.read_csv(get_RKI_file())
        self.df_landkreise = pd.read_csv(get_Landkreise_file(), encoding = "utf-8", sep=';').drop(columns=['LandkreisId'])

    def calling_api(self):
        '''
        Calling the API, initiate the DB interface and scrape the latest data from web.
        '''
        db = DB_interface()
        db.update_RKI_csv()
        db.update_RKI_landkreise_csv()


    def get_rki_dataframe(self):
        '''
        Merging two csv files to have a more complete dataframe from the RKI (Robert-Koch-Insitut).
        '''
        tmp = pd.read_csv(get_RKI_file())
        tmp = tmp[tmp['IdLandkreis']!='0-1']
        nuts = pd.read_csv(get_RKI_landkreise_file())
        nuts = nuts.filter(['county', 'NUTS'])

        result = pd.merge(left=tmp, right=nuts, how='left', left_on='Landkreis', right_on='county').drop(columns=['county'])
        return (result)


    def compute_population(self):
        # Compute the whole population of Germany via dataset 'landkreise.csv'
        self.df_landkreise['Bevoelkerung'] = self.df_landkreise['Bevoelkerung'].str.replace(" ","")
        self.df_landkreise['Bevoelkerung'] = self.df_landkreise['Bevoelkerung'].astype(int)
        return (self.df_landkreise['Bevoelkerung'].sum())


    def compute_cases(self):
        # Compute the whole infected Corona cases for Germany.
        return (self.df_rki['AnzahlFall'].sum())
