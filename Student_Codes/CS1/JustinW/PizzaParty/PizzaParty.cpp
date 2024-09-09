#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
using namespace std;

bool validInput = false;

void checkInput(){
    if (cin.fail()) {
            cout << "Invalid input! Expected an number! \n";
            // Clear the failbit and ignore the remaining
            // input
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(),'\n');
        }
        else{
            validInput = true;
        }
    return;
}

//A customized main() structure is used to enable system halts.
int main(int nNumberofArgs, char* pszArgs[]){
    int parties;
    float sum;
    int Max;
    int Min;
    
    srand(time(NULL));

    while(!validInput){
        cout << "Please input the # of Pizza Parties that you wish to test against (Higher # = more accurate): ";
        cin >> parties;
        checkInput();
    }
    validInput = false;

    while(!validInput){
        cout << "\nPlease input the Maximum # of expected attendees: ";
        cin >> Max;
        checkInput();
    }
    validInput = false;

    while(!validInput){
        cout << "\nPlease input the Minimum # of expected attendees: ";
        cin >> Min;
        cout <<"\n";
        checkInput();
    }
        validInput = false;
    
    //Dynamically allocates memory for an amount of integers equal to parties + 1.
    int* attendees;
    attendees = new int[parties + 1];

    for (int x = 1; x < parties + 1; x++){
        *(attendees + x) = (rand() % (Max - Min + 1) + Min);
        sum += *(attendees + x);
        cout << "# of Attendees for Party " << x << ": " << *(attendees + x) << "\n";
    }
    
    //Deletes the memory allocated to attendees, and sets the pointer position to null.
    delete[] attendees;
    attendees = nullptr;
    cout << "The average # of attendees for your next party is: " << sum/parties << "\n";

    //The following code halts the .exe file so that the user can read the output.
    system("PAUSE");
    return 0; 
}