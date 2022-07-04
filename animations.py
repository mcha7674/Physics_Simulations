from matplotlib import pyplot as plt
from numpy import block
import pandas as pd
from matplotlib.animation import PillowWriter
from matplotlib.animation import FuncAnimation
import matplotlib.colors
import math
import os
"""
Writing a class that animates a plot as a gif
Creates x vs y animation for a singular trajectory
"""
class Animation():
    def __init__(self,dataPath, figSize = (10,6), color = "black",isComparing = False,isMulti=False, realTime = False):
        self.df = pd.read_csv(dataPath)
        print("INIT DATASIZE: ", len(self.df["x"]))
        self.dataPath = dataPath
        self.figSize = figSize
        self.color = color
        self.isComparing = isComparing
        self.isMulti = isMulti
        # initializ fig, axis,and empty plot
        self.fig,self.ax = plt.subplots(figsize=figSize)        
        # for efficiency in the animation
        self._setGraphLimits()
        # initiate empty plot array and dataframes array
        self.dataFrames = []
        self.curves = []
        if isComparing:
            self._initComparePlots()
            self.curve1, = self.ax.plot([],[],c = "blue",label="Air")
            self.curve2, = self.ax.plot([],[],c = "black", label="Vaccum")
            self.curve3, = self.ax.plot([],[],c = "orange",label="Adiabatic")
            self.curves.append(self.curve1)
            self.curves.append(self.curve2)
            self.curves.append(self.curve3)
        elif isMulti:
            self._initMultiPlots()
            for i,df in enumerate(self.dataFrames):
                degree_sign= u'\N{DEGREE SIGN}'
                self.label = str(int(df["angle"][0])) + degree_sign
                self.curve, = self.ax.plot([],[],label = str(self.label))
                self.curves.append(self.curve)
        else:
            self.dataFrames.append(self.df)
            self.curve, = self.ax.plot([],[],c = "black")
            self.curves.append(self.curve)
        # Time of Flight - adjusted
        self.t = self.df["t"]
        self.dt = self.t[1] - self.t[0]
        # calc correct interval.
        if (realTime):
            # mult by 900 instead of 1000 to account for system delays
            self.interval = int(self.dt * 905) # since interval is in ms
            print("USING REAL TIME, Interval =  ",self.interval)
        else: self.interval = 1
        print('Interval: ', self.interval/1000," seconds")
      
    
    def _initMultiPlots(self):
        if self.isMulti:
            numOfTraj = int(self.df["traj"].iloc[-1])
            for i in range (1,numOfTraj+1):
                df_temp = self.df[self.df["traj"] == i]
                df_temp.reset_index(inplace=True)
                self.dataFrames.append(df_temp)

    def _initComparePlots(self):
        if self.isComparing:
            self.df1 = self.df[self.df["id"] == "DRAG"]
            self.df1.reset_index(inplace=True)
            self.df2 = self.df[self.df["id"] == "NO_DRAG"]
            self.df2.reset_index(inplace=True)
            self.df3 = self.df[self.df["id"] == "HEIGHT_DRAG"]
            self.df3.reset_index(inplace=True)
            self.dataFrames.append(self.df1)
            self.dataFrames.append(self.df2)
            self.dataFrames.append(self.df3)

    def _setGraphLimits(self):
        self.x = self.df["x"]
        self.y = self.df["y"]
        xOffset = 0.05*(self.x.max())
        yOffset = 0.05*(self.y.max())
        self.ax.set_xlim(self.x.min()-xOffset,self.x.max()+xOffset)
        self.ax.set_ylim(self.y[0],self.y.max()+yOffset)
        
    def _animate(self,i):
        for k,curve in enumerate(self.curves):
            self.curves[k].set_data(self.dataFrames[k]["x"][:i],self.dataFrames[k]["y"][:i])
        return self.curves
   
    def decorateGraph(self, title = "", xLabel = "", yLabel = "",
    setLegend = False,label = "", setTight = True):
        self.ax.set_xlabel(xLabel)
        self.ax.set_ylabel(yLabel)
        self.ax.set_title(title)
        self.ax.set_label(label)
        if setLegend:
            self.ax.legend()
        self.fig.tight_layout()

    def createAnimation(self):
        self.animation = FuncAnimation(self.fig,func=self._animate,interval = self.interval,
            frames=len(self.df["x"]),repeat=False,blit=False)        

    def saveAnimation(self,gifPath = 'Plots/graph.gif',dpi = 300):
        self.animation.save(gifPath,writer='pillow',fps=self.fps)

    def showPlot(self,Block=False):
        plt.show(block = Block)
    
    def closePlot(self):
        plt.close()

# ani = Animation("Data/trajData.csv",figSize=(9,6),isComparing=False,isMulti=False,realTime=True)
# ani.decorateGraph(title = "Trajectories in real time", xLabel="X (meters)",
# yLabel= "Y (meters)",setLegend=True)
# ani.createAnimation()
# ani.showPlot(Block=True)
# # ani.closePlot()
# ani.saveAnimation()


  
