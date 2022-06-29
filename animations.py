from matplotlib import pyplot as plt
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
    def __init__(self,dataPath, figSize = (8,7), color = "black",isComparing = False,isMulti=False):
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
        if (len(self.df) > 500):
            self.sliceNum = int(math.ceil(len(self.df)/500))
            print("SLICENUM: ",self.sliceNum)
            self._slice(self.sliceNum)
        self._setGraphLimits()
        # initiate empty plot array and dataframes array
        self.dataFrames = []
        self.curves = []
        if isComparing:
            self._initComparePlots()
            for df in self.dataFrames:
                self._determineSlice(df)
            self.curve1, = self.ax.plot([],[],c = "blue",label="Air")
            self.curve2, = self.ax.plot([],[],c = "black", label="Vaccum")
            self.curve3, = self.ax.plot([],[],c = "orange",label="Adiabatic")
            self.curves.append(self.curve1)
            self.curves.append(self.curve2)
            self.curves.append(self.curve3)
        elif isMulti:
            self._initMultiPlots()
            for i,df in enumerate(self.dataFrames):
                self._determineSlice(df)
                degree_sign= u'\N{DEGREE SIGN}'
                self.label = str(int(df["angle"][0])) + degree_sign
                self.curve, = self.ax.plot([],[],label = str(self.label))
                self.curves.append(self.curve)
        else:
            self.dataFrames.append(self.df)
            self._determineSlice(self.dataFrames[0])
            self.curve, = self.ax.plot([],[],c = "black")
            self.curves.append(self.curve)
        # Time of Flight - adjusted
        self.t = self.df["t"]
        self.dt = self.t[1] - self.t[0] 
        # calc fps
        self.fps = int(1/self.dt) # Get accurate fps to simulate real time trajectory
        if self.fps == 0:self.fps = 1
        fps = 15
        print("FPS calc: ",self.fps)
        #if self.fps <10:self.fps+=5 
        #print("FPS adjusted: ",self.fps)     
    
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

    def _slice(self,sliceNum):
        print("SLICE: ",sliceNum)
        self.df = self.df.iloc[::sliceNum]
        self.df.reset_index(inplace=True)
        print("POST DATA SIZE: ", len(self.df["x"]))

    def _determineSlice(self,df):
        size = len(df["x"])
        print("PRE DATA SIZE: ", size)         
        threshold = 200
        if (size > threshold):
            slice =  int(math.ceil((size/(threshold))))
            df = df.iloc[::slice]
            print("POST DATA SIZE: ", len(df["x"]))
            print("SLICE: ", slice)
            # add back in the last value
            df.reset_index(inplace=True)

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

    def createAnimation(self,interval):
        self.animation = FuncAnimation(self.fig,func=self._animate,interval = interval,
            frames=len(self.df["x"]),repeat=False,blit=True)        

    def saveAnimation(self,gifPath = 'Plots/graph.gif',dpi = 300):
        self.animation.save(gifPath,writer='pillow',fps=self.fps)

    def showPlot(self):
        plt.show()

ani = Animation("Data/trajData2.csv",figSize=(6,5),isComparing=False,isMulti=True)
ani.decorateGraph(title = "Trajectories in real time", xLabel="X (meters)",
yLabel= "Y (meters)",setLegend=True)
ani.createAnimation(interval=1)
#ani.showPlot()
ani.saveAnimation()


  
