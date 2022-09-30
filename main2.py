import suvatEngine as engine # woop woop my own code works
import numpy as np
import plotly.express as px
UIP=""

while UIP!="plot":
    try:
        UIP = input("v,theta:   ")
        values=UIP.split(",")
        values = [int(values[i]) for i in len(values)]
        plot1 = engine.suvat(values[0],values[1]) 
        x = plot1.projectile_x() 
        y = plot1.projectile_y()
        y=y.flatten()   
        x=x.flatten()
        xl = x.tolist()
        yl = y.tolist()
        print(xl)
        print(yl)
        #plot the figure
        fig = px.line(x=xl, y=yl)
        del plot1
    except:
        None
fig.show()
