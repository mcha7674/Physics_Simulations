#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <vector>
#include <chrono>
#include <iomanip>
#include "trajectory.h"
#include "support.h"

using namespace std;

// Default Constructor - analytical solution of simple default projectile
Trajectory::Trajectory() {}

// Parameterized constructor with with shell specification and custom conditions
Trajectory::Trajectory(double chosenAngle, double chosenV0, double chosenX0, double chosenY0,
                       double dt, double C,
                       double windX,
                       double T, bool isDragging,
                       bool isAdiabatic, Projectile projectile)
{
    // init parameters
    angle = chosenAngle;
    v0 = chosenV0;
    x0 = X;
    y0 = Y;
    vy0 = vY;
    vx0 = vX;
    shell = projectile;
    // Toggles
    drag = isDragging;
    adiabatic = isAdiabatic;
    // custom prereq parameters
    set_C(C);
    set_vWindX(windX);
    set_T(T);
    set_dt(dt);
    // Initialize velocity Parameters
    vx0 = v0 * cos(degreeToRads(angle));
    vy0 = v0 * sin(degreeToRads(angle));
    // Toggle Initializations
    if (drag)
    {
      
        B2 = 0.5 * C * airDensity * shell.get_CrossSection(); // const
        double vDiff = vX - vWindX;
        double m = shell.get_mass();
        double vDiffAbs = sqrt((pow(vDiff, 2)) + (pow(vY, 2)));
        Fx = ((B2)*vDiffAbs * (vX - vWindX));
        Fy = ((B2)*vDiffAbs * vY);
    }
    if (adiabatic)
    {
        py = airDensity * pow((1 - (a * y0 / T0)), alpha);
        B2 = 0.5 * C * py * shell.get_CrossSection();
    }
    // with no drag, forces stay initialized at 0
    // append Origin to data containers
    xData.push_back(chosenX0);
    yData.push_back(chosenY0);
    vData.push_back(chosenV0);
}

void Trajectory::createTrajectory()
{
    int i = 0;
    double t = 0; // time elapsed
    // init parameters
    X = x0;
    Y = y0;
    V = v0;
    vY = vy0;
    vX = vx0;
    while (Y >= 0) // while projectile is above ground, run the simulation
    {
        t = i * dt;
        if (!drag) // medium is a vaccum
        {   // use analytical solution
            X = x0 + (vx0 * t);
            Y = y0 + (vy0 * t) - (0.5 * g * (t * t));
            // vX unchanged but vY varies
            vY = vy0 - (g * t);
            V = sqrt((pow(vX, 2) + pow(vY, 2)));
        }
        else
        {
            // Making the trajectory CALCULATIONS
            X = X + vX * dt;
            Y = Y + vY * dt;
            vX = vX - ((Fx / shell.get_mass()) * dt);
            vY = vY - ((Fy / shell.get_mass()) * dt) - (g * dt);
            V = sqrt((pow(vX, 2) + pow(vY, 2))); // speed of shell
        }
        if (adiabatic)
        {
            py = airDensity * pow((1 - (a * Y / T0)), alpha);
            // Constant B2 now overwritten with a variant one B2(py)
            B2 = 0.5 * C * (py)*shell.get_CrossSection(); // B2 Now changes with py
        }
        if (drag)
        {
            double m = shell.get_mass();
            double vDiff = vX - vWindX;
            double vDiffAbs = sqrt((pow(vDiff, 2)) + (pow(vY, 2)));
            Fx = ((B2)*vDiffAbs * (vX - vWindX));
            Fy = ((B2)*vDiffAbs * vY);
        }
        // Append new X and Y values
        if (Y >= 0)
        {
            xData.push_back(X);
            yData.push_back(Y);
            vData.push_back(V);
        }
        
        i++;
    }
    range = interpolatedRange(); // range of the trajectory in meters
    flightTime = t;
    maxHeight = findMaxY();
    // add final data point
    xData.push_back(range);
    yData.push_back(0);
    vData.push_back(0);
}
// INTERPOLATED RANGE FUNCTION
double Trajectory::interpolatedRange()
{
    // using interpolation formula
    double Yn = yData[yData.size() - 2];
    double Yn1 = yData[yData.size() - 1];
    double Xn = xData[xData.size() - 2];
    double Xn1 = xData[xData.size() - 1];
    double r = -1 * (Yn / Yn1);
    double xl = (Xn + r * Xn1) / (r + 1);
    return xl;
}
// FIND HEIGHT OF TRAJECTORY
double Trajectory::findMaxY()
{ // iterates through dataY array to find max Y
    double h = 0;
    for (int i = 0; i < yData.size(); i++)
    {
        if (yData[i] > h)
        {
            h = yData[i];
        }
    }
    return h;
}

// Data Output
void Trajectory::outputData(ofstream &f)
{
    for (int i = 0; i < xData.size(); i++)
    {
        double t = i * dt;
        f << xData[i] << "," << yData[i] << "," << t << "," << vData[i] << "," << angle << endl;
    }
}

void Trajectory::outputMultiData(ofstream &f, int trajNum)
{
    for (int i = 0; i < xData.size(); i++)
    {
        double t = i * dt;
        f << xData[i] << "," << yData[i] << "," << t << "," << vData[i] << "," << angle<<","<<trajNum << endl;
    }
}

// Data output for comparison plots
void Trajectory::outputComparisonData(ofstream &f, trajType type)
{
    string id = "";
    switch (type)
    {
    case DRAG:
        id = "DRAG";
        break;
    case HEIGHT_DRAG:
        id = "HEIGHT_DRAG";
        break;
    case NO_DRAG:
        id = "NO_DRAG";
        break;
    default:
        break;
    }
    for (int i = 0; i < xData.size(); i++)
    {
        double t = i * dt;
        f << xData[i] << "," << yData[i] << "," << t << "," << vData[i] << "," << angle << "," << id << endl;
    }
}

void Trajectory::outputStatsSingle()
{
    // output to stats file
    string filename = "Stats/stats_single.txt";
    ofstream f(filename, ios_base::out | ios_base::app); // append
    f << "==========TRAJECTORY STATS==========" << endl;
    f << "Adiabatic: " << boolalpha << adiabatic << endl;
    f << "Drag: " << boolalpha << drag << endl;
    f << "maxH: " << maxHeight << " meters" << endl;
    f << "Range: " << range << " meters" << endl;
    f << "flightTime: " << flightTime << " seconds" << endl;
    f << "PROJECTILE:" << endl;
    f << "mass = " << shell.get_mass() << " kg " << endl;
    f << "radius = " << shell.get_radius() << " meters" << endl;
    f << "area cross section = " << shell.get_CrossSection() << " meters^2" << endl;
    f << "Custom Inputs:" << endl;
    f << "Drag Coeffiecient (C): " << C << endl;
    f << "Chosen Wind Velocity: " << vWindX << endl;
    f << "Chosen Initial Velocity: " << v0 << endl;
    f << "Chosen Angle: " << angle << endl;
    // TIME STAMP using chrono library and output to f using iomanip
    auto now = chrono::system_clock::now();
    auto UTC = chrono::duration_cast<chrono::seconds>(now.time_since_epoch()).count();
    auto in_time_t = chrono::system_clock::to_time_t(now);
    f << "\nTIME STAMP: " << put_time(localtime(&in_time_t), "%Y-%m-%d %X") << endl;
    f << "====================================" << endl
      << endl;
}

void Trajectory::outputStatsMany(double initAngle, double finalAngle, double dTheta)
{
    // output to stats file
    string filename = "Stats/stats_multi.txt";
    ofstream f(filename, ios_base::out | ios_base::app); // append
    f << "==========TRAJECTORY STATS MANY==========" << endl;
    f << "Adiabatic: " << boolalpha << adiabatic << endl;
    f << "Drag: " << boolalpha << drag << endl;
    f << "PROJECTILE:" << endl;
    f << "mass = " << shell.get_mass() << " kg " << endl;
    f << "radius = " << shell.get_radius() << " meters" << endl;
    f << "area cross section = " << shell.get_CrossSection() << " meters^2" << endl;
    f << endl;
    f << "Custom Inputs:" << endl;
    f << "Angle Range: " << initAngle << "-" << finalAngle << " degrees "
      << "at steps of" << dTheta << "degrees" << endl;
    f << "Drag Coeffiecient (C): " << C << endl;
    if (adiabatic)
    {
        f << "Chosen atmospheric temperature: " << T0 << endl;
    }
    f << "Chosen Wind Velocity: " << vWindX << endl;
    f << "Chosen Initial Velocity: " << v0 << endl;
    // TIME STAMP using chrono library and output to f using iomanip
    auto now = chrono::system_clock::now();
    auto UTC = chrono::duration_cast<chrono::seconds>(now.time_since_epoch()).count();
    auto in_time_t = chrono::system_clock::to_time_t(now);
    f << "\nTIME STAMP: " << put_time(localtime(&in_time_t), "%Y-%m-%d %X") << endl;
    f << "====================================" << endl
      << endl;
}

////////////////////////////////////////////////////////////////////////////////////////
// OUTSIDE OF CLASS

int findMaxTrajectory(vector<Trajectory> &trajArray, double &maxAngle,
                      double &maxRange, double &maxHeight, double &maxFlightTime)
{   //Finds the max trajectory from an array of trajectories and saves its stats to external vars
    int maxTrajIndex;
    for (int i = 0; i < trajArray.size(); i++)
    {
        if (trajArray[i].getRange() > maxRange)
        {
            maxAngle = trajArray[i].getAngle();
            maxRange = trajArray[i].getRange();
            maxHeight = trajArray[i].getHeight();
            maxFlightTime = trajArray[i].getFlightTime();
            maxTrajIndex = i;
        }
    }
    return maxTrajIndex;
}
