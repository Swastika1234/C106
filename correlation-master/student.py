import csv
import numpy as np
def getData(dataPath):
    marks=[]
    days=[]
    with open(dataPath) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
    return {"x":marks,"y":days}
def findRelation(dataSource):
    corelation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("corelation= ",corelation[0,1])

def setup():
    dataPath="student.csv"
    dataSource=getData(dataPath)
    findRelation(dataSource)
setup()

