import scheduler
import time
from DB_interface import *

# this file gets scheduled 4 times a day on my local machine and pulls
# new data from the API.

def pull_data():
    DB = DB_interface()
    DB.update_RKI_csv()
    DB.update_RKI_landkreise_csv()

if __name__ == "__main__":
    pull_data()