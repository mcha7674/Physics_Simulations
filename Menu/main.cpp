#include <iostream>
#include <string>
#include <vector>
#include "menu.h"

using namespace std;

int main()
{
    Menu menu;
    string title = "Physics Simulation Collection with Analyses";
    string desc = "Description asdf asdf asdfasdafsd asdfasfd sadfasdfasdfasdf asdfs";
    menu.add_title(title);
    menu.add_desc(desc);
    // menu.add_dynamic_desc(desc);
    menu.display_title();
    menu.display_desc();
    menu.add_option("Option 1 Pls.");
    menu.add_option("Another one for the record.");
    menu.add_option("One more for good measure.");
    menu.display_options();
    system("pause");
    return 0;
}