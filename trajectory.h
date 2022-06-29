#pragma once

#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <vector>
#include "projectile.h"
using namespace std;

// GLOBAL CONSTANTS
#define PI 3.14159 // directive, defining PI to be its value too a few digits

enum trajType
{
    DRAG = 1,
    HEIGHT_DRAG = 2,
    NO_DRAG = 3
};

// -----------TRAJECTORY CLASS -------------
class Trajectory
{
private:
    // Projectile
    Projectile shell;
    // General Trajectory Parameters
    double g = 9.81; // gravity acceleration
    double dt = 0;
    double V = 0; // current speed
    double v0 = 0; // initial speed
    double vy0 = 0; // init speed in y
    double vx0 = 0; // init speed in x
    double vX = 0; // variable Vx
    double vY = 0; // variable Vy
    double X = 0;  // horizontal position
    double Y = 0;  // vertical position
    double x0 = 0;
    double y0 = 0;
    // Drag Dependent parameters
    double C = 0;      // drag coefficient
    double Fy = 0;     // force in the Y
    double Fx = 0;     // Force in the X
    double B2 = 0;     // Newtons's Drag Constant (for High Velocity)
    double vWindX = 0; // wind velocity in X
    // Adiabatic Height Variation Parameters
    double T0 = 0;                   // Kelvin
    const double a = 0.0065;         // Kelvin/m density equation constant that fits observed data
    const double alpha = 2.5;        // Exponent in density equation dependent in air
    const double airDensity = 1.225; // kg/m^3 at sea level
    long double py = 0;
    // Trajectory Statistics variables
    double maxHeight = 0;  // maximum height of the trajectory in meters
    double angle = 0;      // Angle of the trajectory in degrees
    double range = 0;      // range of the trajectory in meters
    double flightTime = 0; // total time in the air
    double angleStep = 0;
    // Condition toggle vars
    bool drag = false;      // Drag toggle
    bool adiabatic = false; // adiabatic conditions toggle
    // Trajectory Data
    vector<double> xData; // x pos
    vector<double> yData; // y pos
    vector<double> vData; // velocity
    // private helper functions
    double findMaxY();          // finds and sets the height from yData
    double interpolatedRange(); // returns interpolated range of a trajectory

public:
    // Default constructor -> default scenario, simple projectile
    Trajectory();
    // The Parameterized Constructor -> initializes vars
    Trajectory(double chosenAngle, double chosenV0, double chosenX0,
               double chosenY0, double dt, double C,
               double windX, double T,
               bool isDragging,
               bool isAdiabatic, Projectile projectile);
    // Setters
    void setAngle(double ang) { angle = ang; };
    void set_C(double c) { C = c; };
    void set_vWindX(double windX) { vWindX = windX; };
    void set_T(double t) { T0 = t; };
    void set_dt(double Dt) { dt = Dt; };
    void set_angleStep(double step) { angleStep = step; }
    // Getters
    double getAngle() { return angle; }
    double getRange() { return range; }
    double getHeight() { return maxHeight; }
    double getFlightTime() { return flightTime; }

    // Data Output
    void outputData(ofstream &f);
    void outputComparisonData(ofstream &f, enum trajType);
    void outputMultiData(ofstream &f, int trajNum);
    // Stats Output
    void outputStatsSingle();                                                 // stats for single trajectory at fixed angle
    void outputStatsMany(double initAngle, double finalAngle, double dTheta); // stats for varying angles, multiple trajectories
    // CREATE TRAJECTORY
    void createTrajectory();
    // HELPER FUNCTIONS
    void updateAngle(double value);
};

// Function to Output Multiple Trajectories
int findMaxTrajectory(vector<Trajectory> &trajArray, double &maxAngle,
                      double &maxRange, double &maxHeight, double &maxFlightTime);
