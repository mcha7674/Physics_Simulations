import subprocess
import sys
import os
from matplotlib import pyplot as plt
import numpy
import pandas as pd
from os.path import exists
# Custom imports
import plots # Custom Plots class
import gui_source as gui # All code for the GUI

def saveFolderCheck():
    # Verify if Data and Plot folder exist, else create them in working directory
    data_exists = exists("Data")
    plots_exists = exists("Plots")
    stats_exists = exists("Stats")
    if (not data_exists):
        os.mkdir("Data")
    if (not plots_exists):
        os.mkdir("Plots")
    if (not stats_exists):
        os.mkdir("Stats")

def showRecent(recent_saved_plots, plotPath = "Plots/"):
    is_showing = input("Show recently created plots? (y/n): ")
    if is_showing == "y":
        directory = plotPath
        for filename in recent_saved_plots:
            f = os.path.join(directory, filename)
            # checking if it is a file
            if os.path.isfile(f):
                print("Opening '", f, "'")
                im = Image.open(f)  # image library output image
                im.show()

def rm_data(mother_folder = "data_plots_stats",directories = ("Data","Plots","Stats")):
    for directory in directories:
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                shutil.copy(f, mother_folder)
                if directory == "Stats":
                    is_clearing = input(f"Clear {filename} Memory?(y/n): ")
                    if is_clearing == "y":
                        os.remove(f)
                    else: continue
                else: os.remove(f)

saveFolderCheck()
recent_saved_plots = []
iteration = 0
while True:
    # init vars
    CPP_exe = "source.exe"
    plotPath = "Plots/"
    dataPath = "Data/"
    plotName = ""
    dataName = ""
    figSize = (14,12)
    # Run the cpp data aquisition script
    subprocess.call(CPP_exe) 
    # Check menu choice from file
    menu_choice = check_choice()
    ######## Data and Plot Paths for SINGLE TRAJECTORY ##############
    # Check if file exists
    file_exists = exists(dataPath + dataName)
    if(file_exists and menu_choice == 1):
        plotName = "singlePos({}).png".format(iteration)
        dataName = "trajData.csv"   
        # single Positional trajectory
        xyPlot = plots.trajPlot(figsize=figSize)
        xyPlot.read_data(dataName=dataName)
        xyPlot.newSubplot(xlb=["Position in X (meters)"],
        ylb = ["Position in Y (meters)"],title=["Trajectory of Shell"])
        xyPlot.posTraj()
        print("Plot saved to ", plotPath + plotName)
        xyPlot.saveFig(pName = plotName)
        recent_saved_plots.append(plotName)
        # single trajectory velocity
        vPlot = plots.trajPlot(figsize=figSize)
        vPlot.read_data(dataName=dataName)
        vPlot.newSubplot(xlb=["Time (seconds)"],
        ylb = ["Projectile Speed (meters/second)"],title=["Speed of projectile vs Time"])
        vPlot.speedTraj(color="blue")
        plotName = "singleSpeed.png"
        print("Plot saved to ", plotPath + plotName)
        vPlot.saveFig(pName = plotName)
        recent_saved_plots.append(plotName)
        # single positional AND velocity trajectories
        vAndXY_plot = plots.trajPlot(figsize=figSize)
        vAndXY_plot.read_data(dataName=dataName)
        vAndXY_plot.newSubplot(xlb=["Position in X (meters)","Time (seconds)"],
        ylb = ["Position in Y (meters)","Projectile Speed (meters/second)"],
        title=["Trajectory of Shell","Speed of projectile vs Time"],rowCols=[2,1])
        plotName = "singleSpeedAndPos.png"
        vAndXY_plot.speedAndPosTraj(speedColor="blue",posColor="black")
        print("Plot saved to ", plotPath + plotName)
        vAndXY_plot.saveFig(pName = plotName)
        recent_saved_plots.append(plotName)
    ######## Data and Plot Paths for MULTIPLE TRAJECTORIES ##############
    plotName = "manyTraj({}).png".format(iteration)
    dataName = "trajData2.csv"
    dataName2 = "maxTraj.csv"
    # Check if file exists
    file_exists = exists(dataPath + dataName)
    if(file_exists and menu_choice == 2):
        multiPlot = plots.trajPlot(manyTraj=True)
        multiPlot.read_data(dataName=dataName)
        multiPlot.newSubplot(xlb=["Position in X (meters)"],
        ylb = ["Position in Y (meters)"],title=["Trajectory of Shell"])
        multiPlot.posTraj()
        multiPlot.read_data(dataName=dataName2)
        maxAngle = multiPlot.getAngle()
        multiPlot.posTraj(color="orange",
            Label = "Trajectory with max range for angle {} degrees".format(maxAngle))
        multiPlot.setLegend()
        multiPlot.saveFig(plotName)
        recent_saved_plots.append(plotName)
        print("Plot saved to ", plotPath + plotName)
    ################Trajectory Comparisons#########################
    dataName = "comparisons.csv"
    # Check if file exists
    file_exists = exists(dataPath + dataName)
    if(file_exists and menu_choice == 3):
        # JUST DRAG PLOTS
        plotName = "drag_comparisons({}).png".format(iteration)
        plotGroup3 = plots.trajPlot(comparisons=True)
        plotGroup3.read_data(dataName="comparisons.csv",Id="DRAG")
        plotGroup3.newSubplot(xlb=["Position in X (meters)"],
        ylb = ["Position in Y (meters)"],title=["Trajectory of Shell"])
        plotGroup3.posTraj(Label = "Drag With NO Adiabatic Height Dependence",
        color="blue")
        plotGroup3.read_data(dataName="comparisons.csv",Id="HEIGHT_DRAG")
        plotGroup3.posTraj(Label = "Drag With Adiabatic Height Dependence",
        color="orange")
        plotGroup3.setLegend()
        plotGroup3.saveFig(plotName)
        recent_saved_plots.append(plotName)
        print("Plot with Drag and Height dependent drag comparisons saved to ",
              plotPath + plotName)
        # Plot No DRAG AND DRAG PLOTS
        plotName = "comparisons({}).png".format(iteration)
        plotGroup3.read_data(dataName="comparisons.csv",Id="NO_DRAG")
        plotGroup3.posTraj(Label = "Vaccum",color="black")
        plotGroup3.setLegend()
        plotGroup3.saveFig(plotName)
        recent_saved_plots.append(plotName)
        print("Plot with Drag and vaccum comparisons saved to ",
              plotPath + plotName)
    ##################################################
    # Ask for save location of Plots, Data, And Stats
    # create program folders that includes all of the above
    if not os.path.exists("data_plots_stats"):
        os.mkdir("data_plots_stats")
    # Will utilize PyQT5 GUI save file dialog
    #############################################
    # Ask to show plots
    # reading png image file in Plots directory
    showRecent(recent_saved_plots)
    #################END CONDITION####################
    program_continue = input("\nContinue? (y/n): ")
    if program_continue != "y":
        break
    else:
        recent_saved_plots = []  # rest recent saved plots
        iteration += 1
# Add data to program folder and delete FIles in Data and Plots in temp directories
rm_data()

# Output Stats TxT file
