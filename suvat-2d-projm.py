import sys
import numpy as np
import plotly.graph_objects as go
import math
fig = go.Figure()

class suvat:
    def __init__(self,v,theta,h):
        self.g = 9.81 
        self.v = v
        self.h = h
        self.theta = theta # from the verticle
        self.rads = theta*(np.pi/180) # putting theta in rads for numpy

        #verticle and horizontal componants of v at t=0.
        self.v0y = v * np.cos(self.rads)
        self.v0x = v * np.sin(self.rads) 

        #flight time
        if h==0:
            self.maxt = (2*self.v0y)/self.g
        else:
            self.maxt = (math.sqrt(2*self.g*self.h+(self.v0y**2))+self.v0y)/self.g 

        # array from 0 to t, 2000 increments, used to calculate.
        self.timearray = np.linspace(0,self.maxt,2000)[:,None]



    def projectile_x(self):
        x=(self.timearray*self.v0x) # horizontal displacement for the x axis.
        x=x.flatten()  # formatting for the graphing engine.
        return x.tolist() # more formatting & return.


    def projectile_y(self):
        y=(self.timearray*self.v0y)-((self.g/2)*(self.timearray**2))+self.h # verticle displacement for the y axis.
        y=y.flatten()   # formatting for the graphing engine.
        return y.tolist()


    def name(self):
        name = "",self.v,",",self.theta,",",self.h,"" # name of the line is the input values of the object.
        return name

if sys.argv[1]=="help" or sys.argv[1]=="--help" or sys.argv[1]=="-help": # prints the help menu.
    print("""

    2D SUVAT solver!

    velocity in ms-1
    height in m
    theta in degrees from the ~~verticle~~

    modes:
    1: plot as many trajectories at specified v,theta,h values.
    2: plot 90 trajectores at the same v,h value for theta 0 to 90.

    data entry:
    1 v,h,theta-v,h,theta- ect.
    2 v,h-

    """)
    quit()

try:
    long = sys.argv[2].split("-") # evaling cmdl argument
except:
    quit()


# mode 1, see readme
if sys.argv[1]=="1":
    for i in range(len(long)): # breaking down each dataset from said argument.
        small=long[i].split(",")#   ^^

        try:
            set=suvat(float(small[0]),float(small[1]),float(small[2])) #makes obj with said values

            #calculation.
            xdata=set.projectile_x()
            ydata=set.projectile_y()
            name =str(set.name())

            #plotting.
            fig.add_trace(go.Scatter(x=xdata, y=ydata,mode="lines", name=name))
            del set

        except:
            print("value error dataset: ",long[i]," quitting." )
            quit()




#mode2, see readme
elif sys.argv[1]=="2":
    try:
        data = sys.argv[2].split(",")
        for i in range(0,90,2): # theta 0-90 in steps of 2 degrees.
            set=suvat(float(data[0]),float(i),float(data[1])) #makes obj with said values

            #calculation.
            xdata=set.projectile_x()
            ydata=set.projectile_y()
            name =str(set.name())

            #plotting.
            fig.add_trace(go.Scatter(x=xdata, y=ydata,mode="lines", name=name))
            del set
    except:
        print("Invalid data quitting.")
        quit()

else:
    print("Invalid input quitting.")
    quit()


#labeling
fig.update_layout(title="Trajectories (velocity, theta from the verticle, height)", xaxis_title="Horizontal travel (M)", yaxis_title="Vericle travel (M)")

#make 1x=1y, as the graph should be life-like.
fig.update_yaxes(scaleanchor = "x", scaleratio = 1,)

#plot figure
fig.show()

