#include <iostream>
#include <fstream>
#include <sstream>
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


void handleFileInputs(string filename, vector<double> &numericInputs,vector<bool> &booleanInputs, string &trajType)
{
    // initiate input filestream
    ifstream ifs(filename);
    string line = "";
    int i = 0;
    while(getline(ifs, line))
    { 
        // line 0 is trajType
        // lines 1 - 10 are numeric
        // lines 11-13 are boolean
        // last 2 lines are also numeric
        string inputName;
        double inputValue;
        stringstream ss(line); // initiate line into string stream
        if (i == 0)
        { // call twice to overwrite label
            string name;
            ss >> name;
            ss >> trajType;
        }
        else if (i > 10 && i <= 13)
        {
            string value;
            string name;
            ss >> name;
            ss >> value;
            if (value == "True")
            {
                booleanInputs.push_back(true);
            }
            else
            {
                booleanInputs.push_back(false);
            }
        }
        else
        {
            double value;
            string name;
            ss >> name;
            ss >> value;
            numericInputs.push_back(value);
        }
        i++;
    }

}