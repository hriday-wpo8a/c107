import plotly.graph_objects as go
import pandas as pd
import csv

df=pd.read_csv("data.csv")

print(df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    x=df.groupby("level")["attempt"].mean(),
    y=['Level 1','Level 2','Level 3','level 4'],
    orientation='h'
))
fig.show()