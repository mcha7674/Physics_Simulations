from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.animation import PillowWriter
from matplotlib.animation import FuncAnimation
import matplotlib.colors
import math
"""
Writing a class that animates a plot as a gif
Creates x vs y animation for a singular trajectory
"""
class Animation():
    def __init__(self,dataPath, figSize = (8,7), color = "black"):
        self.df = pd.read_csv(dataPath)
        self.dataPath = dataPath
        self.figSize = figSize
        self.color = color
        # initializ fig, axis,and empty plot
        self.fig,self.ax = plt.subplots(figsize=figSize)        
        # for efficiency in the animation
        self._determineSlice()
        self._setGraphLimits()
        # initiate empty plot
        self._initPlot()
        # Time of Flight - adjusted
        self.t = self.df["t"]
        self.dt = self.t[1] - self.t[0] 
        self.fps = 1/self.dt # Get accurate fps to simulate real time trajectory
        print("FPS: ",self.fps)
        if (self.fps <= 10):
            # Set to 15 if below 10 to prioritize aesthetic
            self.fps = 15
        print("FPS: ",self.fps)
    
    def _initPlot(self):
        self.curve, = self.ax.plot([],[],c = self.color)

    def _determineSlice(self):
        size = len(self.df["x"])
        start = 700 
        if (size >= start):
            slice =  math.ceil((size/(start-100)))
            self.df = self.df.iloc[::slice]
        # save last value
        df_temp = self.df.iloc[-1]
        # add back in the last value
        self.df = self.df.append(df_temp, ignore_index=True)

    def _setGraphLimits(self):
        self.x = self.df["x"]
        self.y = self.df["y"]
        xOffset = 0.05*(self.x.max())
        yOffset = 0.05*(self.y.max())
        self.ax.set_xlim(self.x[0],self.x.max()+xOffset)
        self.ax.set_ylim(self.y[0],self.y.max()+yOffset)
        
    def _animate(self,i):
        self.curve.set_data(self.df["x"][:i],self.df["y"][:i])
        # set Red Circle
        return self.curve,
    
    def decorateGraph(self, title = "", xLabel = "", yLabel = "",
    setLegend = False,label = "", setTight = True):
        self.ax.set_xlabel(xLabel)
        self.ax.set_ylabel(yLabel)
        self.ax.set_title(title)
        self.ax.set_label(label)
        if setLegend:
            self.ax.legend()
        self.fig.tight_layout()

    def createAnimation(self,interval):
        self.animation = FuncAnimation(self.fig,func=self._animate,interval = interval,
            frames=len(self.df["x"]),repeat=False,blit=True)        

    def saveAnimation(self,gifPath = 'Plots/graph.gif',dpi = 200):
        self.animation.save(gifPath,writer = "pillow" ,fps=self.fps)

    def showPlot(self):
        plt.show()

# ani = Animation("Data/trajData2.csv",figSize=(6,5))
# ani.decorateGraph(title = "Single Trajectory", xLabel="X (meters)",
# yLabel= "Y (meters)")
# ani.createAnimation(interval=1)
# ani.showPlot()
# ani.saveAnimation()


  
