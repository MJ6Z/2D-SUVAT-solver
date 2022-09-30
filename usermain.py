import suvatEngine as engine # woop woop my own code works
import numpy as np
import plotly.graph_objects as go
fig = go.Figure()


def plotit(v,theta,h,name):
    #suvat-engine makes the dataset 
    plot = engine.suvat(float(v),float(theta),float(h))
    #making the data passable to plotly
    x = plot.projectile_x()
    y = plot.projectile_y()
    y=y.flatten()   
    x=x.flatten()
    xl = x.tolist()
    yl = y.tolist()
    #plot the figure
    fig.add_trace(go.Scatter(x=xl, y=yl,mode="lines", name=name))
    del plot



InP=""
mode = int(input("mode1/2:  "))
if mode == 1:


    while True:
        Inp = input("v,theta,h:   ")
        if Inp == "b" or Inp=="plot":
            break
        values=Inp.split(",")
        plotit(values[0],values[1],values[2],"name")



else:
    Inp=input("v,h:  ")
    theta_range = [0,10,20,30,40,50,60,70,80,90]
    values=Inp.split(",")
    for i in range(1,89):
        plotit(values[0],i,values[1],i)







#labeling

fig.update_layout(
    title="Trajectories", xaxis_title="Horizontal travel in M", yaxis_title="Vericle travel in M"
)

#make 1x=1y, as the graph should be life-like.
fig.update_yaxes(
    scaleanchor = "x",
    scaleratio = 1,
  )


#plot figure
fig.show()
