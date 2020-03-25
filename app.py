from flask import Flask
from multiprocessing import Process
import waitress
import time
import DB_interface as DBI




@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/start_bckgrnd_update')
def start_bckgrnd_update():
    p = Process(target=bckgrnd_update, name="background_update")
    p.start()
    p.join()

def bckgrnd_update():
    global updating
    updating = True
    while updating:
        print(time.now)
        print("updating RKI DBs now")
        DB = DBI.DB_interface()
        DB.update_RKI_csv()
        DB.update_RKI_landkreise_csv()
        day = 24*3600 #seconds in a day
        time.sleep(day)



if __name__ == "__main__":
    app = Flask(__name__)
    waitress.serve(app)