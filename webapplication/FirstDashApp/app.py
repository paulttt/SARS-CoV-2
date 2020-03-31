import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime
import dateutil.relativedelta as relativedelta
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd



start = datetime.datetime.today() - relativedelta(weeks=3)
end = datetime.datetime.today()

#df = pd.read_csv("TimeSeriesData.csv")

trace_close = go.Scatter(x = list(df.index),
                         y = list(df.data)
                         name="Infections",
                         line=dict(color="#eb7434")

)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    style={ 'font-family':"Courier New, monospace" },
    children=[
    html.H1('Forecast on Corona Virus Infections for Germany on a county level'),
    html.Div(className="row", children=[
        html.Div(className="four columns", children=[
            html.H5('Landkreis'),
            dcc.Dropdown(
                id='landkreis',
                options=[{'label':c, 'value':c} for c in Landkreise],
                value='München'
            )
        ]),
        html.Div(className="four columns", children=[
            html.H5('Bundesland'),
            dcc.Dropdown(
                id='bundesland'
            )
        ]),
        html.Div(className="four columns", children=[
            html.H5('Selected Metrics'),
            dcc.Checklist(
                id='metrics',
                options=[{'label':m, 'value':m} for m in ['Infected', 'Deaths', 'Recovered']],
                value=['Infected', 'Deaths']
            )
        ])
    ]),
    dcc.Graph(
        id="plot_new_metrics",
        config={ 'displayModeBar': False }
    ),
    dcc.Graph(
        id="plot_cum_metrics",
        config={ 'displayModeBar': False }
    )
])

@app.callback(
    [Output('state', 'options'), Output('state', 'value')],
    [Input('country', 'value')]
)
def update_states(country):
    states = list(allData.loc[allData['Country/Region'] == country]['Province/State'].unique())
    states.insert(0, '<all>')
    states.sort()
    state_options = [{'label':s, 'value':s} for s in states]
    state_value = state_options[0]['value']
    return state_options, state_value

def nonreactive_data(country, state):
    data = allData.loc[allData['Country/Region'] == country] \
                  .drop('Country/Region', axis=1)
    if state == '<all>':
        data = data.drop('Province/State', axis=1).groupby("date").sum().reset_index()
    else:
        data = data.loc[data['Province/State'] == state]
    newCases = data.select_dtypes(include='Int64').diff().fillna(0)
    newCases.columns = [column.replace('Cum', 'New') for column in newCases.columns]
    data = data.join(newCases)
    data['dateStr'] = data['date'].dt.strftime('%b %d, %Y')
    return data

def barchart(data, metrics, prefix="", yaxisTitle=""):
    figure = go.Figure(data=[
        go.Bar(
            name=metric, x=data.date, y=data[prefix + metric],
            marker_line_color='rgb(0,0,0)', marker_line_width=1,
            marker_color={ 'Deaths':'rgb(200,30,30)', 'Recovered':'rgb(30,200,30)', 'Confirmed':'rgb(100,140,240)'}[metric]
        ) for metric in metrics
    ])
    figure.update_layout(
              barmode='group', legend=dict(x=.05, y=0.95, font={'size':15}, bgcolor='rgba(240,240,240,0.5)'),
              plot_bgcolor='#FFFFFF', font=tickFont) \
          .update_xaxes(
              title="", tickangle=-90, type='category', showgrid=True, gridcolor='#DDDDDD',
              tickfont=tickFont, ticktext=data.dateStr, tickvals=data.date) \
          .update_yaxes(
              title=yaxisTitle, showgrid=True, gridcolor='#DDDDDD')
    return figure

@app.callback(
    Output('plot_new_metrics', 'figure'),
    [Input('country', 'value'), Input('state', 'value'), Input('metrics', 'value')]
)
def update_plot_new_metrics(country, state, metrics):
    data = nonreactive_data(country, state)
    return barchart(data, metrics, prefix="New", yaxisTitle="New Cases per Day")

@app.callback(
    Output('plot_cum_metrics', 'figure'),
    [Input('country', 'value'), Input('state', 'value'), Input('metrics', 'value')]
)
def update_plot_cum_metrics(country, state, metrics):
    data = nonreactive_data(country, state)
    return barchart(data, metrics, prefix="Cum", yaxisTitle="Cumulated Cases")

server = app.server

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=True)
"""
app = dash.Dash()

app.layout = html.Div(
    html.H1(children="Hello World")
)

if __name__ == "__main__":
    app.run_server(debug=True)
"""