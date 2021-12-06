import plotly.express as px
import csv 
with open("coffee.csv") as csv_files:
    df=csv.DictReader(csv_files)
    fig=px.scatter(df,x="Coffee in ml", y="sleep in hours", color="week")
    fig.show()

