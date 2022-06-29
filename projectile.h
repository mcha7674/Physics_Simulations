#pragma once

#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <vector>

using namespace std;

#define PI 3.14159 // directive, defining PI to be its value too a few digits

class Projectile
{
public:
    Projectile(){};                  // Default constructor
    Projectile(double m, double rad) // Parameterized constructor
    {
        mass = m;
        radius = rad;
        areaCrossSection = radius * radius * PI;
    }
    void set_mass(double m) { mass = m; }
    void set_radius(double rad) { radius = rad; }
    void set_CrossSection(double cs) { areaCrossSection = cs; }
    double get_mass() { return mass; }
    double get_radius() { return radius; }
    double get_CrossSection() { return areaCrossSection; }

private:
    double mass = 0.0;
    double radius = 0.0;
    double areaCrossSection = 0;
};