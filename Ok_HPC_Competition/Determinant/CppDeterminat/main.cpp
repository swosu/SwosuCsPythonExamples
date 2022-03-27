// in the terminal to compile the code (make executable files)
// g++ main.cpp -fopenmp

// to run the executable
// ./a.out

// in the terminal to pull down a file to test it out
// wget http://morpheus.mcs.utulsa.edu/~papama/hpc/m5000x5000.bin
// wget http://morpheus.mcs.utulsa.edu/~papama/hpc/m0016x0016.bin
// wget http://morpheus.mcs.utulsa.edu/~papama/hpc/m0032x0032.bin
// wget http://morpheus.mcs.utulsa.edu/~papama/hpc/m0125x0128.bin
// wget http://morpheus.mcs.utulsa.edu/~papama/hpc/m0512x0512.bin
// wget http://morpheus.mcs.utulsa.edu/~papama/hpc/m1000x1000.bin
#include <iostream>
#include <omp.h>
#include <math.h>

using namespace std;

double startingTime = 0.0;
double endingTime = 0.0;
double timeToCalculate = 0.0;

// int arraySize = 16;
// int arraySize =  32;
// int arraySize =  64;
// int arraySize =  128;
// int arraySize =  256;
// int arraySize =  496;
// int arraySize =  512;
// int arraySize =  1000;
// int arraySize =  1024;
// int arraySize =  2000;
// int arraySize =  2048;
// int arraySize =  3000;
// int arraySize =  4000;
// int arraySize =  4096;
int arraySize =  5000;

double *matrix = new double[arraySize * arraySize];

int main()
{

    cout << "Hello, World!" << endl; // This prints Hello, World!
    std::cout << "Hello, welcome to the SWOSU determinant code." << std::endl;
    std::cout << "The goal of this code is to run on a single pi as qucikly as possible." << std::endl;

    char f_name[50];
    // Create filename
    sprintf(f_name, "m5000x5000.bin");
    // sprintf(f_name,"m4096x4096.bin");
    // sprintf(f_name,"m4000x4000.bin");
    // sprintf(f_name,"m3000x3000.bin");
    // sprintf(f_name,"m2048x2048.bin");
    // sprintf(f_name,"m2000x2000.bin");
    // sprintf(f_name,"m1024x1024.bin");
    // sprintf(f_name,"m1000x1000.bin");
    // sprintf(f_name,"m0512x0512.bin");
    // sprintf(f_name,"m0496x0496.bin");
    // sprintf(f_name, "m0016x0016.bin");
    // sprintf(f_name,"m0032x0032.bin");
    // sprintf(f_name,"m0064x0064.bin");
    // sprintf(f_name,"m0128x0128.bin");
    // sprintf(f_name,"m0256x0256.bin");
    // sprintf(f_name,"m6000x6000.bin");
    printf("Reading array file %s of size %dx%d\n",
           f_name, arraySize, arraySize);

    // Open file
    FILE *datafile = fopen(f_name, "rb");
    if (!datafile)
    {
        std::cerr << "File could not be opened." << std::endl;
        exit(EXIT_FAILURE);
    }

    // Read elelements
    for (int rowIndex = 0; rowIndex < arraySize; rowIndex++)
    {
        for (int columnIndex = 0; columnIndex < arraySize; columnIndex++)
        {
            fread((matrix + rowIndex * arraySize + columnIndex),
                  sizeof(double), 1, datafile);
        }
    }
    printf("Finished reading array file %s of size %dx%d\n",
           f_name, arraySize, arraySize);

    /* for (int rowIndex = 0; rowIndex < arraySize; rowIndex++)
    {
        for (int columnIndex = 0; columnIndex < arraySize; columnIndex++)
        {
            std::cout << *(matrix + rowIndex * arraySize + columnIndex) << ", ";
        }
        std::cout << std::endl;
    } */

    startingTime = omp_get_wtime();

    for (int columnIndex = 0; columnIndex < arraySize - 1; columnIndex++)
    {
        // pragma omp parallel for //fastest but hard to make work with MPI
        for (int rowToZeroIndex = columnIndex + 1; rowToZeroIndex < arraySize; rowToZeroIndex++)
        {

            double rowReductionMultipier = *(matrix + rowToZeroIndex * arraySize + columnIndex) /
                                           *(matrix + columnIndex * arraySize + columnIndex);

#pragma omp parallel for
            for (int rowAddressIndex = columnIndex + 1; rowAddressIndex < arraySize;
                 rowAddressIndex++)
            {
                *(matrix + rowToZeroIndex * arraySize + rowAddressIndex) =
                    *(matrix + rowToZeroIndex * arraySize + rowAddressIndex) - rowReductionMultipier *
                                                                                   *(matrix + columnIndex * arraySize + rowAddressIndex);
            }
        }
    }

    /* std::cout << "\n\n after getting zeros." << std::endl;
    for (int rowIndex = 0; rowIndex < arraySize; rowIndex++)
    {
        for (int columnIndex = 0; columnIndex < arraySize; columnIndex++)
        {
            std::cout << *(matrix + rowIndex * arraySize + columnIndex) << ", ";
        }
        std::cout << std::endl;
    } */

    double diagonalMultiplyResult = 1;
    double diagonalComponent = 0;
    //#pragma omp parallel for reduction(*:diagonalMultiplyResult)
    for (int diagonalIndex = 0; diagonalIndex < arraySize; diagonalIndex++)
    {
        diagonalComponent = *(matrix + diagonalIndex * arraySize + diagonalIndex);
        diagonalMultiplyResult = diagonalMultiplyResult * diagonalComponent;
    }

    double diagonalLogComponent = 0;
    double diagonalLogResult = 0;
    //#pragma omp parallel for reduction(+:diagonalLogResult)
    for (int diagonalIndex = 0; diagonalIndex < arraySize; diagonalIndex++)
    {
        diagonalComponent = *(matrix + diagonalIndex * arraySize + diagonalIndex);
        diagonalLogComponent = log10(abs(diagonalComponent));
        // printf("diagonalLogComponent %e\n", diagonalLogComponent);
        diagonalLogResult = diagonalLogResult + diagonalLogComponent;
        // printf("diagonalLogResult %e\n", diagonalLogResult);
    }

    endingTime = omp_get_wtime();
    timeToCalculate = endingTime - startingTime;

    printf("The hard work is done.");

    printf("Multiplication Determinant Result %e\n", diagonalMultiplyResult);
    printf("Log Sum Determinant Result %e\n", diagonalLogResult);
    
    std::cout << "OpenMP Time to calculate: " << timeToCalculate << std::endl;

    std::cout << "Thank you for running the code. That is all." << std::endl;

    printf("Side Length\nDet\nlog abs det\ntime\n\n");
    printf("%d\n%e\n%e\n%f\n", arraySize, diagonalMultiplyResult, diagonalLogResult, timeToCalculate);
    return 0;
}
