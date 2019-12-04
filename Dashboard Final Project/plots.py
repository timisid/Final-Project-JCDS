import plotly
import plotly.graph_objects  as go
import plotly.express as px
import pandas as pd
import json

def count_type1():
    df = pd.read_csv('womens-clothing-clean-2-done.csv')
    df_group= df['Rating'].value_counts()
    
    fig = go.Figure([
        go.Bar(x=df_group.index , y= df_group.values)
    ])
    fig_json = json.dumps(fig , cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
    # fig.show()
def count_type2():
    df = pd.read_csv('womens-clothing-clean-2-done.csv')
    df_group= df['Sentiment'].value_counts()
    
    fig = go.Figure([
        go.Bar(x=df_group.index , y= df_group.values)
    ])
    fig_json = json.dumps(fig , cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
def count_type3():
    df = pd.read_csv('womens-clothing-clean-2-done.csv')
    df_group= df['Recommended IND'].value_counts()
    
    fig = go.Figure([
        go.Bar(x=df_group.index , y= df_group.values)
    ])
    fig_json = json.dumps(fig , cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

