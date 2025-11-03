#include <cmath>
#include <iostream>
#include <string>
#include <cstdlib>
#include <cassert>
using namespace std;

class randomNum {
    public:
        int min;
        int max;
        void chooseADice(string choice){
            if (choice == "d2") {
                this->min = 1;
                this->max = 2;
            } else if (choice == "d4") {
                this->min = 1;
                this->max = 4;
            } else if (choice == "d6") {
                this->min = 1;
                this->max = 6;
            } else if (choice == "d8") {
                this->min = 1;
                this->max = 8;
            } else if (choice == "d10") {
                this->min = 1;
                this->max = 10;
            } else if (choice == "d12") {
                this->min = 1;
                this->max = 12;
            } else if (choice == "d20") {
                this->min = 1;
                this->max = 20;
            } else if (choice == "d100") {
                this->min = 1;
                this->max = 100;
            } else if (choice == "custom") {
                cout << "Please enter the minimum value of the dice: ";
                cin >> this->min;
                cout << endl << "Please enter the maximum value of the dice: ";
                cin >> this->max;
            }}
        int rollDice(){
            int result = rand() % (this->max - this->min + 1) + this->min;
            return result;
        };
};

int test_chooseADice() {
    randomNum dice;
    int numberofTests;

    dice.chooseADice("d2");
    assert(dice.min == 1);
    assert(dice.max == 2);
    numberofTests++;

    dice.chooseADice("d4");
    assert(dice.min == 1);
    assert(dice.max == 4);
    numberofTests++;

    dice.chooseADice("d6");
    assert(dice.min == 1);
    assert(dice.max == 6);
    numberofTests++;

    dice.chooseADice("d8");
    assert(dice.min == 1);
    assert(dice.max == 8);
    numberofTests++;

    dice.chooseADice("d10");
    assert(dice.min == 1);
    assert(dice.max == 10);
    numberofTests++;

    dice.chooseADice("d12");
    assert(dice.min == 1);
    assert(dice.max == 12);
    numberofTests++;

    dice.chooseADice("d20");
    assert(dice.min == 1);
    assert(dice.max == 20);
    numberofTests++;

    dice.chooseADice("d100");
    assert(dice.min == 1);
    assert(dice.max == 100);
    numberofTests++;

    return numberofTests;
}

int test_rollDice() {
    randomNum dice;
    int numberofTestsA;

    dice.chooseADice("d2");
    int result = dice.rollDice();
    assert(result >= 1 && result <= 2);
    numberofTestsA++;

    dice.chooseADice("d4");
    result = dice.rollDice();
    assert(result >= 1 && result <= 4);
    numberofTestsA++;

    dice.chooseADice("d6");
    result = dice.rollDice();
    assert(result >= 1 && result <= 6);
    numberofTestsA++;

    dice.chooseADice("d8");
    result = dice.rollDice();
    assert(result >= 1 && result <= 8);
    numberofTestsA++;

    dice.chooseADice("d10");
    result = dice.rollDice();
    assert(result >= 1 && result <= 10);
    numberofTestsA++;

    dice.chooseADice("d12");
    result = dice.rollDice();
    assert(result >= 1 && result <= 12);
    numberofTestsA++;

    dice.chooseADice("d20");
    result = dice.rollDice();
    assert(result >= 1 && result <= 20);
    numberofTestsA++;

    dice.chooseADice("d100");
    result = dice.rollDice();
    assert(result >= 1 && result <= 100);
    numberofTestsA++;

    return numberofTestsA;
}

int main(){
    srand(time(NULL));
    randomNum dice;
    string choice;
    int numberofTests = 0;

    numberofTests = test_chooseADice() + test_rollDice();

inputTree:
    cout << numberofTests << " out of " << numberofTests << " tests completed successfully!"<< endl;
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