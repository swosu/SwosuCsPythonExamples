#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>
#include <stdbool.h>

#define SEEDS_COUNT 4
#define RANGE_COUNT 6
#define MAX_FILENAME 50

int seeds[SEEDS_COUNT] = {5, 14, 24, 42};
int range_magnitudes[RANGE_COUNT] = {1000, 10000, 20000, 30000, 50000, 100000};

void generate_equations(int seed, int range, int *a, int *b, int *c, int *d, int *e, int *f, int *x_real, int *y_real) {
    srand(seed);
    *x_real = rand() % (range + 1);
    *y_real = rand() % (range + 1);
    *a = rand() % 101;
    *b = rand() % 101;
    *c = (*a) * (*x_real) + (*b) * (*y_real);
    *d = rand() % 101;
    *e = rand() % 101;
    *f = (*d) * (*x_real) + (*e) * (*y_real);
}

bool check_file_for_entry(int seed, int range) {
    FILE *file = fopen("results.csv", "r");
    if (!file) return false;
    
    int s, r;
    while (fscanf(file, "%d,%d", &s, &r) != EOF) {
        if (s == seed && r == range) {
            fclose(file);
            return true;
        }
    }
    fclose(file);
    return false;
}

void save_results(int seed, int range, int x, int y, double time_taken) {
    FILE *file = fopen("results.csv", "a");
    if (!file) {
        printf("Error opening results file!\n");
        return;
    }
    fprintf(file, "%d,%d,%d,%d,%f\n", seed, range, x, y, time_taken);
    fclose(file);
}

void find_x_and_y_parallel(int a, int b, int c, int d, int e, int f, int range, int *x_out, int *y_out) {
    int x, y;
    double start_time = omp_get_wtime();
    bool found = false;

    #pragma omp parallel for collapse(2) shared(found)
    for (x = 0; x <= range; x++) {
        for (y = 0; y <= range; y++) {
            if (found) continue;
            if (a * x + b * y == c && d * x + e * y == f) {
                #pragma omp critical
                {
                    *x_out = x;
                    *y_out = y;
                    found = true;
                }
            }
        }
    }
    double end_time = omp_get_wtime();
    save_results(seeds[0], range, *x_out, *y_out, end_time - start_time);
}

int main() {
    FILE *file = fopen("results.csv", "w");
    if (file) {
        fprintf(file, "Seed,Range,X,Y,Time\n");
        fclose(file);
    }
    
    for (int i = 0; i < SEEDS_COUNT; i++) {
        for (int j = 0; j < RANGE_COUNT; j++) {
            int seed = seeds[i];
            int range = range_magnitudes[j];
            if (check_file_for_entry(seed, range)) continue;
            
            int a, b, c, d, e, f, x_real, y_real, x_found, y_found;
            generate_equations(seed, range, &a, &b, &c, &d, &e, &f, &x_real, &y_real);
            find_x_and_y_parallel(a, b, c, d, e, f, range, &x_found, &y_found);
        }
    }
    printf("Results saved to results.csv\n");
    return 0;
}
