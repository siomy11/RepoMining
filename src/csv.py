import csv
import scipy
import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode,  plot
from plotly.graph_objs import *
init_notebook_mode()

#things to do

#either have the provider have the names for data as "DATE" and "DATA"
#or have python know that if its a string then skip it, tried but then read all
#numbers as strings

#the test file being used has dates with no data, where they put a period

#maybe if there's also blank space just skip it


np.set_printoptions(threshold=np.inf)
with open('test.csv') as csvfile: #for now just reading it from my computer
    readCSV = csv.reader(csvfile, delimiter = ',') 
    
    dates = []
    info = []
    
    for row in readCSV:
        time = row[0]
        data = row[1]

        if time == "." or data == ".":   #where there's a date with no data put ' . '
            continue
        
        elif time == "DATE" and data == "DATA": #assuming first row has date and date strings, check above
            continue
            
        elif time == " " or data == " ": #testing for blanks
            continue
            
        else:                           #only add them in here
            dates.append(time)
            info.append(data)
            
    dates = list(map(float,dates))      #change all strings into floats 
    info = list(map(float,info))
    
    arraydates = np.asarray(dates)   #change list into array
    arrayinfo = np.asanyarray(info)  
    
    z_score = []
    
    if len(dates) == len(info):       #do Q1
        zscore = (scipy.stats.zscore(arrayinfo)) #calculate zscore
        
        trace = go.Scatter(  #ignore this just playing around 
                x = dates,
                y = zscore,
                line = dict(
                        color = ('rgb(205,12,24)'),
                        width = 4
                        )
        )
        
        data = [trace]
        layout = Layout(
                showlegend=False,
                height=600,
                width=600,
                )
        fig = dict( data=data, layout=layout )
        plot(fig)  #a graph, just testing
        

    else:
        print("columns are not of same length")
        
        
        
        

   
  


            
            
    

            
  
            
        
    
