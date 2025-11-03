#include "nutrition.h"
#include <iostream>
#include <string>
using namespace std;

int main() {
    Nutrition nutrition;
    string foodName;

    cout << "Enter the name of the food item: ";
    getline(cin, foodName);

fat_input:
    cout << endl << "Enter the amount of fat in grams: ";
    cin >> nutrition.fat;
    if (cin.fail() || nutrition.fat < 0) {
        cin.clear();
        cin.ignore(1000, '\n');
        cout << "Invalid input. Please enter a positive number." << endl;
        goto fat_input;
    }

carb_input:
    cout << endl << "Enter the amount of carbs in grams: ";
    cin >> nutrition.carbs;
    if (cin.fail() || nutrition.carbs < 0) {
        cin.clear();
        cin.ignore(1000, '\n');
        cout << "Invalid input. Please enter a positive number." << endl;
        goto carb_input;
    }

protien_input:
    cout << endl << "Enter the amount of protien in grams: ";
    cin >> nutrition.protien;
    if (cin.fail() || nutrition.protien < 0) {
        cin.clear();
        cin.ignore(1000, '\n');
        cout << "Invalid input. Please enter a positive number." << endl;
        goto protien_input;
    }

    nutrition.printNutritionInfo(foodName);

    system("pause");
    return 0;

    
}