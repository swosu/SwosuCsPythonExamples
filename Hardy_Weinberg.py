import math

# ----------------------------
# Hardy-Weinberg Calculator
# ----------------------------

while True:
    print("\n=== Hardy-Weinberg Equilibrium Calculator ===")
    print("1. I know p (dominant allele frequency)")
    print("2. I know q (recessive allele frequency)")
    print("3. I know p² (AA genotype frequency)")
    print("4. I know q² (aa genotype frequency)")
    print("5. I know observed genotype counts (AA, Aa, aa)")
    print("6. I know the % of the population with the recessive trait")

    choice = input("\nSelect an option (1-6): ")

    if choice in ["1", "2", "3", "4", "5", "6"]:
        break

    print("\nInvalid option. Please select a number from 1 to 6.")

# ----------------------------
# Option 1: Know p
# ----------------------------
if choice == "1":

    while True:
        p = float(input("Enter p (0-1): "))

        if 0 <= p <= 1:
            break

        print("p must be between 0 and 1.")

    q = 1 - p

# ----------------------------
# Option 2: Know q
# ----------------------------
elif choice == "2":

    while True:
        q = float(input("Enter q (0-1): "))

        if 0 <= q <= 1:
            break

        print("q must be between 0 and 1.")

    p = 1 - q

# ----------------------------
# Option 3: Know p²
# ----------------------------
elif choice == "3":

    while True:
        p_squared = float(input("Enter p² (0-1): "))

        if 0 <= p_squared <= 1:
            break

        print("p² must be between 0 and 1.")

    p = math.sqrt(p_squared)
    q = 1 - p

# ----------------------------
# Option 4: Know q²
# ----------------------------
elif choice == "4":

    while True:
        q_squared = float(input("Enter q² (0-1): "))

        if 0 <= q_squared <= 1:
            break

        print("q² must be between 0 and 1.")

    q = math.sqrt(q_squared)
    p = 1 - q

# ----------------------------
# Option 5: Know genotype counts
# ----------------------------
elif choice == "5":

    while True:
        AA_obs = int(input("Observed AA: "))
        Aa_obs = int(input("Observed Aa: "))
        aa_obs = int(input("Observed aa: "))

        N = AA_obs + Aa_obs + aa_obs

        if N > 0:
            break

        print("Population size must be greater than 0.")

    p = ((2 * AA_obs) + Aa_obs) / (2 * N)
    q = ((2 * aa_obs) + Aa_obs) / (2 * N)

# ----------------------------
# Option 6: Know recessive phenotype %
# ----------------------------
elif choice == "6":

    while True:
        recessive_percent = float(
            input("Enter percentage with recessive trait (0-100): ")
        )

        if 0 <= recessive_percent <= 100:
            break

        print("Percentage must be between 0 and 100.")

    q_squared = recessive_percent / 100
    q = math.sqrt(q_squared)
    p = 1 - q

# ----------------------------
# Hardy-Weinberg Calculations
# ----------------------------

AA = p ** 2
Aa = 2 * p * q
aa = q ** 2
dominant_phenotype = AA + Aa
recessive_phenotype = aa
# ----------------------------
# Display Results
# ----------------------------

print("\n====================================")
print("Hardy-Weinberg Equilibrium Results")
print("====================================")

print(f"p = {p:.4f}")
print(f"q = {q:.4f}")

print("\nGenotype Frequencies:")
print(f"AA (p²)  = {AA:.4f}")
print(f"Aa (2pq) = {Aa:.4f}")
print(f"aa (q²)  = {aa:.4f}")

# Verify frequencies add to 1
print(f"\nCheck: AA + Aa + aa = {(AA + Aa + aa):.4f}")

# ----------------------------
# Optional Population Counts
# ----------------------------

population = input(
    "\nEnter population size for expected counts (or press Enter to skip): "
)

if population != "":

    population = int(population)

    print("\nExpected Numbers:")

    print(f"AA = {round(AA * population)}")
    print(f"Aa = {round(Aa * population)}")
    print(f"aa = {round(aa * population)}")
    print("\nPhenotype Frequencies:")
    print(f"Dominant Phenotype (A_) = {dominant_phenotype * population:.0f}")
    print(f"Recessive Phenotype (aa) = {recessive_phenotype * population:.0f}")
print("\nCalculation complete.")