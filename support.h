#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <vector>

using namespace std;

double degreeToRads(double degrees);
void prompt_toggle_Inits(bool &drag, bool &adiabatic, double &C,
                         double &windX,
                         double &T, double &angle,
                         double &v0, double &x0,
                         double &y0, double &dt,
                         double &mass, double &radius, bool compare);