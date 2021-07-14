import numpy as np
import csv
import plotly_express as px

def get_dataSource (dataPath):
    marks=[]
    days=[]

    with open (dataPath)as f:
        csvreader = csv.DictReader(f)
        for row in csvreader:
            marks.append(float(row['Marks']))
            days.append(float(row['Days']))
            
    return{'x':marks,'y':days}

def plotFig(dataPath):
    with open ('marks.csv') as f:
        df = csv.DictReader(f)
        figure = px.scatter(df,x='Marks',y='Days')
        figure.show()

def correlation(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print(correlation[0,1])

def main():
    dataPath = 'marks.csv'
    dataSource =  get_dataSource(dataPath)
    correlation(dataSource)
    plotFig(dataPath)

main()