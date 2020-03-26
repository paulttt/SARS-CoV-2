from flask import Flask, render_template
from multiprocessing import Process
import waitress
import time
from datetime import datetime
from utils import DB_interface as DBI
from utils import path_config as pc

tmplt_path = pc.get_template_path()
app = Flask(__name__, template_folder=tmplt_path)

@app.route('/')
def hello_world():
    user = {'username': 'MSE!'}
    posts = [
        {
            'author': {'username': 'Paul'},
            'body': 'Henrik stinkt wie sau'
        },
        {
            'author': {'username': 'Henrik'},
            'body': 'Ja, aber nach Fisch!'
        }
    ]
    return render_template("index.html", title="home", user = user, posts=posts)

@app.route('/start_bckgrnd_update')
def start_bckgrnd_update():
    p = Process(target=bckgrnd_update, name="background_update")
    p.start()
    #p.join()
    now = datetime.now()
    user = {'username': 'MSE!'}
    posts = [
        {
            'author': {'username': 'Paul'},
            'body': 'Henrik has the update just been started?'
        },
        {
            'author': {'username': 'Henrik'},
            'body': 'You bet your sweet ass it has!'
        },
        {
            'author': {'username': 'Paul'},
            'body': 'So what time was is when it started?'
        },
        {
            'author': {'username': 'Henrik'},
            'body': 'It was exactly %s !' % now
        }

    ]
    return render_template("start_bckgrnd_update.html", title="home", user = user, posts=posts)

def bckgrnd_update():
    global updating
    updating = True
    while updating:
        print(datetime.now())
        print("updating RKI DBs now")
        DB = DBI.DB_interface()
        DB.update_RKI_csv()
        DB.update_RKI_landkreise_csv()
        day = 24*3600 #seconds in a day
        time.sleep(day)



if __name__ == "__main__":
    waitress.serve(app)