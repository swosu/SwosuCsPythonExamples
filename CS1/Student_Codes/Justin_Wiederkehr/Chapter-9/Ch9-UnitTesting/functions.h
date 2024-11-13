#ifndef _ADD_H
#define _ADD_H

#include <cmath>
#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

class randomNum {
    public:
        int min;
        int max;
        int x;
        void chooseADice(std::string choice){
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
            this->x = result;
            return result;
        };
};

#endif
