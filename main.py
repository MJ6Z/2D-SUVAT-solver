import suvatEngine as engine # woop woop my own code works
import numpy as np
import plotly.express as px

# The cool bit is in the other file :)
plot1 = engine.suvat(20,50) 
# make the object from the class suvat, see suvatengine.py
# (velocity, theta)

x = plot1.projectile_x() #grab data from object
y = plot1.projectile_y()
y=y.flatten()   #boring making data usable with plot.ly
x=x.flatten()
xl = x.tolist()
yl = y.tolist()

print(xl)
print(yl)


#plot the figure
fig = px.line(x=xl, y=yl)
fig.show()
print(plot1.returnvalues())


