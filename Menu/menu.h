#pragma once
#include <string>
#include <vector>

using namespace std;
/* PSEUDOCODE
1. A Generic title should pop up with default Text
2. add method to customize title
    a. add method to customize description
3. add method to add options to menu with customizable text
*/
// Aesthetic menu class for all Phys sims
class Menu
{
public:
    void add_title(string newTitle);
    void add_dynamic_desc(string newDesc);
    void add_desc(string newDesc);
    void add_option(string option);

    void display_title();
    void display_desc();
    void display_options();

    int choose();

private:
    vector<string> options;
    string title = "";
    string desc = "";
    int title_char_count = 0;
    int numOptions = 0;
};