#include "functions.h"
using namespace std;

int main(){
    srand(time(NULL));
    randomNum dice;
    string choice;


inputTree:
    cout << "Please enter a dice to roll (d2, d4, d6, d8, d10, d12, d20, d100, custom): ";
    cin >> choice;
    dice.chooseADice(choice);
    if (cin.fail() || dice.min < 0 || dice.max < 1 || dice.min > dice.max || choice != "d2" && choice != "d4" && choice != "d6" && choice != "d8" && choice != "d10" && choice != "d12" && choice != "d20" && choice != "d100" && choice != "custom") {
        cout << "Invalid input! Please enter a valid dice.\n";
        goto inputTree;
    }
    cout << endl << "You rolled a(n) " << dice.rollDice() << "!\n";
    system("pause");

}