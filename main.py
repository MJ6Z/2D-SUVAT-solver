
# INSTALL --- pip install numpy    and pip install plotly

import suvatEngine as engine # woop woop my own code works
import numpy as np
import plotly.graph_objects as go


def plotter(v,theta,h,name):
    #suvat-engine makes the dataset 
    plot = engine.suvat(float(v),float(theta),float(h))
    
    #grab the data
    x = plot.projectile_x()
    y = plot.projectile_y()

    #plot the figure
    fig.add_trace(go.Scatter(x=x, y=y,mode="lines", name=name))
    del plot



fig = go.Figure()



print("""

2D SUVAT solver!

velocity in ms-1
height in m
theta in degrees from the verticle

full input (1) or a sepcific velocity & height at all angles (2)?:
enter b to break, and plot your graph.

""")
print()

uin=""
mode = int(input("1 / 2:  "))
if mode == 1:


    while uin!="b":
        uin = input("v,theta,h:   ")
        values=uin.split(",")
        try:
            plotter(values[0],values[1],values[2],uin)
        except:
            print("invalid input, b to break.")



else:
    uin=input("v,h:  ")
    values=uin.split(",")
    for i in range(1,90):
        plotter(values[0],i,values[1],i)



#labeling
fig.update_layout(title="Trajectories (velocity, theta from the verticle, height)", xaxis_title="Horizontal travel (M)", yaxis_title="Vericle travel (M)")

#make 1x=1y, as the graph should be life-like.
fig.update_yaxes(scaleanchor = "x", scaleratio = 1,)

#plot figure
fig.show()
