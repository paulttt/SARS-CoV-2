# Set up path references and dependencies.
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.append(os.path.join(parentdir, "utils"))

# Import important helper libraries.
from flask import Flask, render_template
import numpy as np

import plotly
import plotly.graph_objs as pgo
import json

# Import modules created to serve the project.
#from utils import DB_interface as DBI
#from utils import path_config as pc
from utils import model

app = Flask(__name__)

@app.route('/')
def index():
    result_plot = compute_model_output()
    return render_template("index.html", graphJSON=result_plot)

def compute_model_output():
    num_steps = 500
    init_inf = 5
    t_inc = 5
    t_inf = 9
    r_t = 2.5 #np.random.normal(2.5, 1.0)
    rho = 1.0
    kappa_0 = 0.0
    kappa = 0.0

    n_pop = 2000

    seir = model.SEIRModel(num_steps,n_pop, init_inf, t_inc, t_inf, r_t, rho, kappa_0, kappa)

    s, e, i, r = seir.run()

    days = np.linspace(0, 1, num_steps)

    trace_0 = pgo.Scatter(x=days, y=s, mode='lines', name='s', line=dict(color='rgba(245, 80, 15, 1)'))
    trace_1 = pgo.Scatter(x=days, y=e, mode='lines', name='e', line=dict(color='rgba(30, 80, 65, 1)'))
    trace_2 = pgo.Scatter(x=days, y=i, mode='lines', name='i', line=dict(color='rgba(0, 90, 35, 1)'))
    trace_3 = pgo.Scatter(x=days, y=r, mode='lines', name='r', line=dict(color='rgba(140, 90, 30, 1)'))

    data = [trace_0, trace_1, trace_2, trace_3]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return (graphJSON)




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
