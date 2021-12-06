import plotly.express as px
import csv 
with open("ice.csv") as csv_files:
    df=csv.DictReader(csv_files)
    fig=px.scatter(df,x="Temperature", y="Cold")
    fig.show()


