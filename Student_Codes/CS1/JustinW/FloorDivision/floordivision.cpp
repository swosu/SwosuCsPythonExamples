#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
using namespace std;

//A customized main() structure is used to enable system halts.
int main(int nNumberofArgs, char* pszArgs[]){
    float num;
    float div;
    cout << "Please input a number to divide: ";
    cin >> num;
    cout << "\nPlease input a number to divide by: ";
    cin >> div;
    cout << "\n" << floor(num/div) << " " << floor((num/div)/div) << " " << floor(((num/div)/div)/div) << "\n";
    
    //The following code halts the .exe file so that the user can read the output.
    system("PAUSE");
    return 0;
}
