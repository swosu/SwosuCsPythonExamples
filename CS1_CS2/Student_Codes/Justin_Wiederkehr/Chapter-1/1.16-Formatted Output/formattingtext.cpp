#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

//A customized main() structure is used to enable system halts.
int main(int nNumberofArgs, char* pszArgs[]){
    cout << "  NO PARKING  \n";
    cout << "2:00 - 6:00 a.m. \n";
    
    //The following code halts the .exe file so that the user can read the output.
    system("PAUSE");
    return 0;
}
