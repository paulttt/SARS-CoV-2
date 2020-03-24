import pandas as pd 
import geopandas as gpd
import descartes # to plot
import numpy as np
import matplotlib.pyplot as plt

# how to do mapplotting based on geopandas: https://www.kdnuggets.com/2020/01/open-data-germany-maps-viz.html


top_cities = {
    'Berlin': (13.404954, 52.520008), 
    'Cologne': (6.953101, 50.935173),
    'Düsseldorf': (6.782048, 51.227144),
    'Frankfurt am Main': (8.682127, 50.110924),
    'Hamburg': (9.993682, 53.551086),
    'Leipzig': (12.387772, 51.343479),
    'Munich': (11.576124, 48.137154),
    'Dortmund': (7.468554, 51.513400),
    'Stuttgart': (9.181332, 48.777128),
    'Nuremberg': (11.077438, 49.449820),
    'Hannover': (9.73322, 52.37052)
}



# plot map of 
# input: 
#         df_county:    dataframe with geometry information about the counties
#         feature:      string        name of column that is plotted: (e.g. AnzahlFall)
def plot_map(df_county, feature):
    plt.rcParams['figure.figsize'] = [16, 11]
    fig, ax = plt.subplots()

    df_county.plot(
        ax=ax, 
        column=feature, 
        categorical=False, 
        legend=True, 
        cmap='autumn_r',
        alpha=0.8
    )

    for c in top_cities.keys():

        ax.text(
            x=top_cities[c][0], 
            y=top_cities[c][1] + 0.08, 
            s=c, 
            fontsize=12,
            ha='center', 
        )

        ax.plot(
            top_cities[c][0], 
            top_cities[c][1], 
            marker='o',
            c='black', 
            alpha=0.5
        )

    ax.set(
        title='Germany: Corona based on County', 
        aspect=1.3, 
        facecolor='lightblue'
    );
    return; 
















###### not important: #################################################
# plot map of 
# input: 
#         df_county:    dataframe with geometry information about the counties
#         feature:      string        name of column that is plotted: (e.g. AnzahlFall)
def plot_map_bystate(county_df, feature):
# prepare identifying the different counties:
    # Color by state (= first two numbers in cca_2):
    county_df = county_df \
        .assign(first_dig_cca_2 = lambda x: x['cca_2'].str.slice(start=0, stop=2))

    # convert first digits of cca_2 to float
    county_df = county_df.astype({'first_dig_cca_2': 'float64'})

    # kick non numeric cca_2 value:
    county_df = county_df.drop(county_df.loc[county_df['first_dig_cca_2'].isna()].index)
    
    
# start plot
    plt.rcParams['figure.figsize'] = [16, 11]
    fig, ax = plt.subplots()

    county_df.plot(
        ax=ax, 
        column='first_dig_cca_2', 
        categorical=True, 
        legend=True, 
        legend_kwds={'title': feature, 'loc':'lower right'},
        cmap='tab20',
        alpha=0.9
    )

    for c in top_cities.keys():
        ax.text(
            x=top_cities[c][0], 
            y=top_cities[c][1] + 0.08, 
            s=c, 
            fontsize=12,
            ha='center', 
        )

        ax.plot(
            top_cities[c][0], 
            top_cities[c][1], 
            marker='o',
            c='black', 
            alpha=0.5
        )

    ax.set(
        title='Germany First-Digit-County Codes Areas', 
        aspect=1.3,
        facecolor='white'
    )
    return; 

