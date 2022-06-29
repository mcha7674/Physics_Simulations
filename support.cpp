#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <vector>
#include "trajectory.h"
#include "projectile.h"

using namespace std;

double degreeToRads(double degrees)
{
    double convert = degrees * (PI / 180.0);
    return convert;
}

void prompt_toggle_Inits(bool &drag, bool &adiabatic, double &C,
                         double &windX,
                         double &T, double &angle,
                         double &v0, double &x0,
                         double &y0, double &dt,
                         double &mass, double &radius, bool compare)
{
    if (!compare)
    {
        drag, adiabatic = false;
        char choice;
        cout << "Introduce drag? (y/n): ";
        cin >> choice;
        if (choice == 'y')
        {
            drag = true;
            cout << "Introduce Adiabatic Height Variation? (y/n): ";
            cin >> choice;
            if (choice == 'y')
            {
                adiabatic = true;
            }
        }
        if (drag)
        {
            cout << "Enter Drag Coefficient: ";
            cin >> C;
            cout << "Enter wind velocity in x direction (in m/s): ";
            cin >> windX;
        }
        if (adiabatic)
        {
            // do not repeat air density question common to drag also
            cout << "Enter atmospheric temperature (in Kelvin): ";
            cin >> T;
        }
    }
    else // include options that encapsulate, drag, no drag, and drag with hight dependence
    {
        cout << "Enter Drag Coefficient: ";
        cin >> C;
        cout << "Enter wind velocity in x direction (in m/s): ";
        cin >> windX;
        cout << "Enter atmospheric temperature (in Kelvin): ";
        cin >> T;
    }
    // General prompts scenario
    cout << "Initial x-position of projectile (in meters): ";
    cin >> x0;
    cout << "Initial y-position of projectile (in meters): ";
    cin >> y0;
    cout << "Initial trajectory Angle (in degrees): ";
    cin >> angle;
    cout << "Initial velocity of projectile (in m/s): ";
    cin >> v0;
    cout << "Radius of shell (in meters): ";
    cin >> radius;
    cout << "Mass of shell (in kg): ";
    cin >> mass;
    cout << "Time step for the simulation (dt): ";
    cin >> dt;
}