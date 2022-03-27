// to compile the code (make executable files)
// g++ main.cpp -fopenmp
#include <iostream>
#include <omp.h>

using namespace std;

double startingTime = 0.0;

int main() {
    
   cout << "Hello, World!" << endl; // This prints Hello, World!
   std::cout<<"Hello, welcome to the SWOSU determinant code." << std::endl;
   std::cout<<"The goal of this code is to run on a single pi as qucikly as possible." << std::endl;
   

   startingTime = omp_get_wtime();
   

   std::cout<<"Thank you for running the code. That is all." << std::endl;
   return 0;
}