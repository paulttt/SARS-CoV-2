"""
Super short program to download latest data from the Drive Folder
"""
from utils import path_config as pc
from utils.Drive_interface import Drive

landkreise = pc.get_RKI_landkreise_file()
RKI = pc.get_RKI_file()
landkreiseName = landkreise.name
RKI_name = RKI.name

drive = Drive()

drive.download_latest_file(landkreiseName, landkreise)
drive.download_latest_file(RKI_name, RKI)