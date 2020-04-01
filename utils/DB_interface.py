"""

Author: Theo Bernier - theo.ju.bern@gmail.com
"""

from arcgis.gis import GIS
import os
from shutil import copyfile
import pandas as pd
import path_config as pc
from datetime import datetime
import chardet


class DB_interface:
    def __init__(self):
        self.RKI_item_id = "dd4580c810204019a7b8eb3e0b329dd6"
        self.RKI_landkreise_item_id = "917fc37a709542548cc3be077a786c17"
        self.anonGIS = GIS()
        pass

    def pull_data(self, item_id):
        data = self.anonGIS.content.get(item_id)
        return data

    def get_data_as_df(self, item_id):
        data = self.pull_data(item_id)
        if len(data.tables) > 0:
            table = data.tables[0]
        else:
            table = data.layers[0]
        df = table.query("1=1").sdf
        return df

    def update_RKI_landkreise_csv(self):
        # Make backup of data agregated up until now
        RKI_landkreise_file = pc.get_RKI_landkreise_file()
        now = str(datetime.now()).replace(" ", "_")
        now = now.replace(":","_")
        now = now[:19]
        backupFileName = "RKI_landkreise_up_to_"+now+".csv"
        backupFilePath = pc.get_backupData_path().joinpath(backupFileName)

        # Load old data, pull and append new data, overwrite csv file with appended df
        #copyfile(RKI_landkreise_file, backupFilePath)
        df_new = self.get_data_as_df(self.RKI_landkreise_item_id)
        df_new = df_new.drop("SHAPE",1)
        df_new.to_csv("temp.temp", index=False)
        df_new = pd.read_csv("temp.temp")
        os.remove("temp.temp")
        sorted_new = df_new.reindex(sorted(df_new.columns), axis=1)
        with open(RKI_landkreise_file, 'rb') as f:
            result = chardet.detect(f.read())  # or readline if the file is large
        df_old = pd.read_csv(RKI_landkreise_file, encoding=result['encoding'])
        sorted_old = df_old.reindex(sorted(df_old.columns), axis=1)

        #compare new rows with all old row and drop exact duplicates
        to_drop = []
        for i, row in df_new.iterrows():
            if (df_old == row).all(1).any():
                to_drop.append(i)

        sorted_new = sorted_new.drop(i,axis=0)
        df_all = sorted_old.append(sorted_new, ignore_index=True, sort=True)
        df_all.to_csv(pc.get_RKI_landkreise_file(), index=False)

    def update_RKI_csv(self):
        df = self.get_data_as_df(self.RKI_item_id)
        df.to_csv(pc.get_RKI_file())




if __name__ == "__main__":
    DB = DB_interface()
    #data = DB.pull_RKI_data()
    DB.update_RKI_csv()
    DB.update_RKI_landkreise_csv()



