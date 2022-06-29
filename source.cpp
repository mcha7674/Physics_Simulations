#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <vector>
#include <sstream>

#include "trajectory.h"
#include "projectile.h"
#include "support.h"

using namespace std;

/*
Capabilities:
* Plot numerous trajectories at various angles - highlighting max - conditions specified
* Plots of single trajectory with certain conditions enabled
* Plots of trajectory comparisons for all conditions
* Stats to accompany each figure
* Projectile specifications
* Environment variables
NOTE: The adiabatic approximation for trajectories with height dependent drag works best
sea level to a max altitude of about 10 km (The troposhere) at which point the approximation breaks down,
imaginary values may occur at high altitudes so limit must be set to 10 km
Adiabatic approach assumes very slow convection, so that projectile does not have enough time to cool down
*/

int main()
{
    // Input File Handling
    string trajType = "";
    vector <double> numericInputs;
    vector <bool> booleanInputs;
    string filename = "inputs.dat";
    handleFileInputs(filename, numericInputs, booleanInputs, trajType);
    for (int i = 0; i < numericInputs.size();i++)
    {
        cout << numericInputs[i] << endl;
    }
    for (int i = 0; i < booleanInputs.size();i++)
    {
        cout << boolalpha <<booleanInputs[i] << endl;
    }
    cout << trajType << endl;
    // general trajectory parameters - init like this for readability
    double X0 = numericInputs[0];
    double Y0 = numericInputs[1];
    double V0 = numericInputs[2];
    double angle = numericInputs[3];
    double finalAngle = numericInputs[4];
    double mass = numericInputs[5];
    double radius = numericInputs[6];
    double C = numericInputs[7];
    double T0 = numericInputs[8]; 
    double vWindX = numericInputs[9];
    bool airToggle = booleanInputs[0];
    bool vacToggle = booleanInputs[1];
    bool compareToggle = booleanInputs[2];
    bool adiabatic = false;
    double stepAngle = numericInputs[10];
    double dt = numericInputs[11];
    if (T0 != 0 || trajType == "compare"){adiabatic = true;}
    // Trajectory Customization!!! --- SINGLE TRAJECTORY
    cout << "final angle: "<< finalAngle << endl;
    if (trajType == "single")
    {
        Projectile shell(mass, radius);
        Trajectory traj(angle, V0, X0, Y0, dt, C, vWindX, T0,
                        airToggle, adiabatic, shell);
        cout << "Trajectory Initialized!" << endl;
        cout << "Creating Trajectory Data..." << endl;
        traj.createTrajectory();
        string filename = "Data/trajData.csv";
        ofstream f(filename);
        cout << "Outputting Trajectory Data to '"<< filename << "'..." << endl;
        f << "x,"<< "y,"<< "t,"<< "v,"<< "angle" << endl;
        traj.outputData(f);
        cout << "Trajectory data stored!" << endl
             << endl;
        traj.outputStatsSingle();
        cout << "Stats stored!" << endl;
        f.close();
    }
    else if (trajType == "multi") // Many Trajectories at various angles
    {
        vector<Trajectory> trajArray;
        Projectile shell(mass, radius);
        // create trajectory
        while (angle <= finalAngle)
        {
        Trajectory traj(angle, V0, X0, Y0, dt, C, vWindX, T0,
                        airToggle, adiabatic, shell);
        traj.set_angleStep(stepAngle);
        traj.createTrajectory();
        // store trajectory
        trajArray.push_back(traj);
        // update current angle
        angle += stepAngle;
        }
        // output trajectory data
        string filename = "Data/trajData2.csv";
        cout << "Outputting Trajectory Data to '"<< filename<< "'..." << endl;
        ofstream f(filename);
        f << "x,"<< "y,"<< "t,"<< "v,"<< "angle" << endl;
        for (int i = 0; i < trajArray.size(); i++)
        {
            trajArray[i].outputData(f);
            cout << "Trajectory " << i + 1 << " data stored!" << endl
                 << endl;
        }
        f.close();
        // Find max Trajectory
        cout << "Finding and outputting max trajectory data..." << endl;
        double maxTrajAngle = 0;
        double maxRange = 0;
        double maxHeight = 0;
        double maxFlightTime = 0;
        int maxTrajIndex = findMaxTrajectory(trajArray, maxTrajAngle, maxRange, maxHeight, maxFlightTime);
        cout << "Max Trajectory found to be trajectory " << maxTrajIndex + 1 << "!" << endl;
        filename = "Data/maxTraj.csv";
        ofstream f2(filename);
        f2 << "x,"<< "y,"<< "t,"<< "v,"<< "angle" << endl;
        trajArray[maxTrajIndex].outputData(f2);
        cout << "Max trajectory data stored in '" << filename << "'" << endl
             << endl;
        trajArray[0].outputStatsMany(angle, finalAngle, stepAngle);
        f2.close();
    }
    else if (trajType == "compare")
    {
        Projectile shell(mass, radius);
        Trajectory trajDrag(angle, V0, X0, Y0, dt, C, vWindX, T0,
                            true, false, shell);
        Trajectory trajHeightDrag(angle, V0, X0, Y0, dt, C, vWindX, T0,
                                  true, true, shell);
        Trajectory trajNoDrag(angle, V0, X0, Y0, dt, C, vWindX, T0,
                              false, false, shell);
        cout << "3 Trajectories Initialized!" << endl;
        cout << "Creating Trajectory Data..." << endl;
        trajDrag.createTrajectory();
        trajHeightDrag.createTrajectory();
        trajNoDrag.createTrajectory();
        string filename = "Data/comparisons.csv";
        // truncate file
        ofstream f(filename, ofstream::out | ofstream::trunc);
        f.close();
        // Now open a clean file to append
        f.open(filename, ios_base::out | ios_base::app);
        cout << "Outputting Trajectory Data to '"
             << filename
             << "'..." << endl;
        f << "x,"<< "y,"<< "t,"<< "v,"<< "angle,"<< "id" << endl;
        trajDrag.outputComparisonData(f, DRAG);
        trajHeightDrag.outputComparisonData(f, HEIGHT_DRAG);
        trajNoDrag.outputComparisonData(f, NO_DRAG);
        cout << "Trajectory data stored!" << endl
             << endl;
        cout << "Storing Stats..." << endl;
        trajDrag.outputStatsSingle();
        trajHeightDrag.outputStatsSingle();
        trajNoDrag.outputStatsSingle();
        cout << "Stats stored!" << endl;
        f.close();
    }
    return 0;
}