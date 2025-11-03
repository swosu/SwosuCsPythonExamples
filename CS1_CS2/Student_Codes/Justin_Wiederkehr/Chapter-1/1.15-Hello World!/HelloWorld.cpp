#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

//A customized main() structure is used to enable system halts.
int main(int nNumberofArgs, char* pszArgs[]){
    cout << "Hello, World! \n"; //The newline character is used to create seperation between the output and the halt message.

    //The following code halts the .exe file so that the user can read the output.
    system("PAUSE");
    return 0;
}
