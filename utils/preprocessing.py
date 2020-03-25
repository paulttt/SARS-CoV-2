import pandas as pd

# return all cases until a given date:
# input:
#       df_agg     aggregated dataframe based on IdLandkreis and Meldedatum
#       date       date of question
# output: 
#       df         dataframe of current values at requested date
def cases_at_date(df_agg, date = "2020-03-20T00:00:00.000Z"):
    df = df_agg[df_agg['Meldedatum'] <= date]\
        .groupby(['IdLandkreis']).max().reset_index()\
        .drop(columns=['Meldedatum'])
    return df;