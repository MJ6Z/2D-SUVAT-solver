
try:
    import suvatEngine as engine # woop woop my own code works
    import numpy as np
    import plotly.graph_objects as go
except ImportError:
    import pip
    pip.main(['install', '--user', 'numpy'])
    pip.main(['install', '--user', 'plotly'])




fig = go.Figure()


def plotter(v,theta,h,name):
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



print("""

2D SUVAT solver!
full input (1) or v+h at all angles (2)?:
enter b to break, and plot your graph.

""")


uin=""
mode = int(input("1 / 2:  "))
if mode == 1:


    while uin!="b":
        uin = input("v,theta,h:   ")
        values=uin.split(",")
        try:
            plotter(values[0],values[1],values[2],uin)
        except:
            None



elif mode == 2:
    uin=input("v,h:  ")
    values=uin.split(",")
    for i in range(1,90):
        plotter(values[0],i,values[1],i)
else:
    None



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
