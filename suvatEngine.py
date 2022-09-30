import numpy as np

class suvat:
    def __init__(self,v,theta):
        self.g = 9.81
        self.v = v
        self.theta = theta
        self.rads = theta*(np.pi/180)
        self.v0y = v * np.cos(self.rads)
        self.v0x = v * np.sin(self.rads) 
        self.maxt = (2*self.v0y)/self.g
        self.timearray = np.linspace(0,self.maxt,100)[:,None] # array from 0 to t, 100 increments.


    def projectile_x(self):
        return (self.timearray*self.v0x) # horizontal displacement x=HorizS

    def projectile_y(self):
        return (self.timearray*self.v0y)-((self.g/2)*(self.timearray**2)) # suvat equation moment, verticle displacement, y=vertS




 #   def returnvalues(self):
  #      return("v: "+self.v+"  theta: "+self.theta+"  time-elapsed: "+self.maxt+"  v0x: "+self.v0x+"  v0y: "+self.v0y)

        





