#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <vector>

using namespace std;

double degreeToRads(double degrees);

void handleFileInputs(string filename, vector<double> &numericInputs,
vector<bool> &booleanInputs, string &trajType);