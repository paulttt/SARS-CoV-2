"""
function lib to centralize path references to .txt, .csv, binaries etc.
Author: Theo Bernier - theo.ju.bern@gmail.com
"""
from pathlib import Path


file=Path(__file__)
ROOT_PATH = file.parent.parent
DATA_PATH = ROOT_PATH.joinpath("data")
BACKUPDATA_PATH = DATA_PATH.joinpath(".backup")

def get_backupData_path():
    return BACKUPDATA_PATH

def get_RKI_file():
    RKI_fileName = "RKI_COVID19.csv"
    return DATA_PATH.joinpath(RKI_fileName)

def get_RKI_landkreise_file():
    RKI_landkreise_fileName = "RKI_Corona_Landkreise_updated.csv"
    return DATA_PATH.joinpath(RKI_landkreise_fileName)

def get_Landkreise_file():
    landkreise_filename = "Landkreise.csv"
    return DATA_PATH.joinpath(landkreise_filename)

def get_altersgruppen_geschlecht():
    altersgruppen_geschlecht_filename = "Altersgruppen_Geschlecht.csv"
    return DATA_PATH.joinpath(altersgruppen_geschlecht_filename)
def get_template_path():
    template_dir = "templates"
    return ROOT_PATH.joinpath(template_dir)