# Set up path references and dependencies.
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.append(os.path.join(parentdir, "utils"))

# Import important helper libraries.
from flask import Flask, render_template

# Import modules created to serve the project.
#from utils import DB_interface as DBI
#from utils import path_config as pc
#from utils import model


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
	
"""
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
        day = 24 * 3600
        time.sleep(day)

"""
	
if __name__ == "__main__":
    app.run(debug=True)