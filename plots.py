from matplotlib import pyplot as plt
import pandas as pd
import sys

class trajPlot():
    # Static class variables
    plotDir = "Plots/"
    dataDir = "Data/"
    Ids = ("Drag","HEIGHT_DRAG","NO_DRAG")

    def __init__(self,pName="",dName="",figsize = (13,8),
    comparisons=False, manyTraj = False, scatterSize = 2):
        # init and default plot/data names
        self.plotName = pName
        self.dataName = dName
        self.dataPath = trajPlot.dataDir + self.dataName
        self.plotPath = trajPlot.plotDir + self.plotName
        self.figsize = figsize
        self.scatterSize = scatterSize
        self.is_comparing = comparisons
        self.manyTraj = manyTraj

    def read_data(self,dataName="",Id = ""):
        # Dataframe
        try:    
            if self.dataPath != "":
                self.df = pd.read_csv(trajPlot.dataDir+dataName)
            else:
                self.df = pd.read_csv(self.dataPath)
            if self.is_comparing:
                self.df2 = self.df[self.df["id"] == Id]
                self.df = self.df2
            # All parameter data from specidied csv file 
            self.x = self.df["x"]
            self.y = self.df["y"]
            self.t = self.df["t"]
            self.v = self.df["v"]
            self.a = self.df["angle"]
            
        except:
            print("Specified Data Does Not Exist or not a csv!!!")
            sys.exit()
        
    def posTraj(self,color = "black",Label = ""):
        #self.axes.scatter(self.x,self.y,c=color,s = self.scatterSize,label= Label)
        self.axes.plot(self.x,self.y,c=color,label= Label)
        
    def speedTraj(self,color = "blue",Label = ""):
        #self.axes.scatter(self.t,self.v,c=color,s = self.scatterSize,label= Label)
        self.axes.plot(self.t,self.v,c=color,label= Label)
    
    def speedAndPosTraj(self,speedColor = "blue", posColor = "black", Label = ""):
        #self.axes[0].scatter(self.x,self.y,c=posColor,s = self.scatterSize,label= Label)
        #self.axes[1].scatter(self.t,self.v,c=speedColor,s = self.scatterSize,label= Label)
        self.axes[0].plot(self.x,self.y,c=posColor,label= Label)
        self.axes[1].plot(self.t,self.v,c=speedColor,label= Label)

    def newSubplot(self,xlb = [],ylb=[], title=[],rowCols =[1,1]):
        """
        Creates a figure and axes for the class object. 
        This function most only be called once per trajecory object instance
        """
        self.fig, self.axes = plt.subplots(rowCols[0],rowCols[1],figsize=self.figsize)
        if (rowCols[0] > 1 or rowCols[0] > 1):
            for i,ax in enumerate(self.axes):
                ax.set_xlabel(xlb[i], fontsize=10)
                ax.set_ylabel(ylb[i], fontsize=10)
                ax.set_title(title[i], fontsize=10)
        else:
            self.axes.set_xlabel(xlb[0], fontsize=10)
            self.axes.set_ylabel(ylb[0], fontsize=10)
            self.axes.set_title(title[0], fontsize=10)
    
    def saveFig(self,pName = "",res = 450):
        if pName != "": # then assign value
            self.plotPath = trajPlot.plotDir + pName
        plt.tight_layout()
        self.fig.savefig(self.plotPath,dpi=res)

    # Setters, Getters, and checkers
    def setPlotName(self,name):
        self.plotName = name
    def setDataName(self,name):
        self.dataName = name
    def setFigsize(self,size):
        self.figsize = size
    def isComparing(self, bool):
        self.is_comparing = bool
    def setLegend(self):
        self.axes.legend()
    def getAngle(self):
        return self.df["angle"][0]
    def closePlot(self):
        plt.close()

# df = pd.read_csv("Data/trajData2.csv")
# plt.plot(df["x"], df["y"])
# plt.savefig("Plots/test.png")