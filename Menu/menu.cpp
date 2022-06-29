#include <iostream>
#include <string>
#include <vector>
#include "menu.h"

using std::string;
using std::vector;

void Menu::display_title()
{
    cout << title << endl;
}

void Menu::display_desc()
{
    cout << "Description:" << endl;
    cout << desc << endl;
}

void Menu::display_options()
{
    // border
    cout << "Choose an option (type number):" << endl
         << endl;
    // null case
    if (numOptions == 0)
    {
        cout << "[No Options]" << endl;
    }
    // else add options to a numbered list
    for (int i = 0; i < numOptions; i++)
    {
        // single line option
        cout << i + 1 << ". " << options[i] << endl;
    }
    // border
    for (int i = 0; i < title_char_count; i++)
    {
        cout << "=";
    }
    cout << endl;
}

void Menu::add_title(string newTitle)
{
    title_char_count = newTitle.size();
    // capitalize all letters
    for (auto &letter : newTitle)
    {
        letter = toupper(letter);
    }
    // add title with border dashes
    int title_length = newTitle.size();
    for (int i = 0; i < title_length; i++)
    {
        title += "-";
    }
    title += "\n" + newTitle + "\n";
    for (int i = 0; i < title_length; i++)
    {
        title += "-";
    }
}

void Menu::add_dynamic_desc(string newDesc)
{
    desc = ""; // reset
    int maxLineLength = title_char_count;
    desc += "|"; // add border
    // if desc is shorter than title
    if ((int)newDesc.size() < maxLineLength)
    {
        desc += newDesc + "|";
    }
    else // if desc is longer than title
    {
        for (int i = 0; i < (int)newDesc.size(); i++)
        {
            desc += newDesc[i];
            if ((i % (maxLineLength - 2) == 0) && (i != 0))
            {
                desc += "|";  // add End border
                desc += "\n"; // start new line
                desc += "|";  // start New line border
            }
        }
    }
}

void Menu::add_desc(string newDesc)
{
    desc = ""; // reset
    desc += "\n";
    desc += newDesc;
    desc += "\n";
    for (int i = 0; i < title_char_count; i++)
    {
        desc += "=";
    }
}

void Menu::add_option(string option)
{
    options.push_back(option);
    numOptions = (int)options.size();
}

int Menu::choose()
{
    int ChosenOption = 1;
    string buffer;
    cout << "Choice: ";
    cin >> ChosenOption;
    getline(cin, buffer); // grabs newline char
    while (ChosenOption > numOptions || ChosenOption <= 0)
    {
        cout << "Enter a choice from 1 to " << numOptions << "!" << endl;
        cout << "Choice: ";
        cin >> ChosenOption;
    }
    cout << "You chose menu option " << ChosenOption << ": " << options[ChosenOption - 1] << endl;

    return ChosenOption;
}