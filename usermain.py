import suvatEngine as engine # woop woop my own code works
import numpy as np
import plotly.graph_objects as go
fig = go.Figure()

def plotit(v,theta):

    #suvat-engine makes the dataset 
    plot1 = engine.suvat(float(v),float(theta)) 

    #making the data passable to plotly
    x = plot1.projectile_x() 
    y = plot1.projectile_y()
    y=y.flatten()   
    x=x.flatten()
    xl = x.tolist()
    yl = y.tolist()

    #plot the figure
    fig.add_trace(go.Scatter(x=xl, y=yl,mode="lines"))



InP=""
mode = int(input("mode1/2:  "))
if mode == 1:
    while InP!="plot":
        try:
            InP = input("v,theta:   ")
            values=InP.split(",")
            plotit(values[0],values[1])
            del plot1
        except:
            None
    
else:
    try:
        v=float(input("v:  "))
        theta = [0,5,10,15,20,25,30,35,45,50,55,60,65,70,75,80,85,90]
        for i in range(len(theta)):
            plotit(v,theta[i])
    except:
        None






#making it look nice n that

fig.update_layout(
    title="hi", xaxis_title="Horizontal travel in M", yaxis_title="Vericle travel in M"
)

fig.update_yaxes(
    scaleanchor = "x",
    scaleratio = 1,
  )


#plot figure
fig.show()
