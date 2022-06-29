#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <vector>

#include "trajectory.h"
#include "projectile.h"
#include "support.h"
#include "Menu/menu.h"
#include "Menu/menu.cpp"
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
    // MENU
    Menu menu;
    menu.add_title("Semi-Realistic Projectile Motion Simulation");
    string desc = "In this simulation, you will be provided three"
                  "\noptions for the type of plots and"
                  "\ntrajectories you want. The program"
                  "\nwill then calculate the relevant data, plots,"
                  "\nand statistics and save the output in"
                  "\nthe folder named 'data_plots_stats'.\n";

    menu.add_desc(desc);
    menu.display_title();
    menu.display_desc();
    menu.add_option("Single Trajectory.");
    menu.add_option("Various trajectories at varying angles.");
    menu.add_option("Trajectory Drag vs altitude-dependent adiabatic drag Comparison.");
    menu.display_options();
    cout << endl;
    int choice = menu.choose();
    // store choice to be read through python
    ofstream choiceF("choice.txt");
    choiceF << choice;
    choiceF.close();

    // general trajectory parameters
    double angle = 0;
    double V0 = 0;
    double X0 = 0;
    double Y0 = 0;
    double dt = 0;
    double mass = 0;
    double radius = 0;
    // Drag Dependent parameters
    double C = 0;      // drag coefficient
    double vWindX = 0; // wind velocity in X
    // Adiabatic Height Variation Parameters
    double T0 = 0; // Kelvin
    bool drag = false;
    bool adiabatic = false;

    // Trajectory Customization!!! --- SINGLE TRAJECTORY
    if (choice == 1)
    {
        // user input for custom scenario
        prompt_toggle_Inits(drag, adiabatic, C, vWindX, T0,
                            angle, V0, X0, Y0, dt, mass, radius, false);
        Projectile shell(mass, radius);
        Trajectory traj(angle, V0, X0, Y0, dt, C, vWindX, T0,
                        drag, adiabatic, shell);
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

    else if (choice == 2) // Many Trajectories at various angles
    {
        double dTheta = 0;
        double maxAngle = 0;
        vector<Trajectory> trajArray;
        // user input for custom scenario
        prompt_toggle_Inits(drag, adiabatic, C, vWindX, T0,
                            angle, V0, X0, Y0, dt, mass, radius, false);
        Projectile shell(mass, radius);
        cout << "Specify the angle step: ";
        cin >> dTheta;
        cout << "Specify the Max angle: ";
        cin >> maxAngle;
        while (maxAngle < angle)
        {
            cout << "Max angle must be greater than initial angle!" << endl;
            cout << "Specify the Max angle: ";
            cin >> maxAngle;
        }
        while (angle <= maxAngle)
        {
            // create trajectory
            Trajectory traj(angle, V0, X0, Y0, dt, C, vWindX, T0,
                            drag, adiabatic, shell);
            traj.set_angleStep(dTheta);
            traj.createTrajectory();
            // store trajectory
            trajArray.push_back(traj);
            // update current angle
            angle += dTheta;
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
        trajArray[0].outputStatsMany(angle, maxAngle, dTheta);
        f2.close();
    }
    else if (choice == 3)
    {
        prompt_toggle_Inits(drag, adiabatic, C, vWindX, T0,
                            angle, V0, X0, Y0, dt, mass, radius, true);
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