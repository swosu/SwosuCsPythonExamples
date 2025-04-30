# Text-based visualization of AI usage growth (2019–2024)
years = [2019, 2020, 2021, 2022, 2023, 2024]
ai_usage = [10, 18, 30, 45, 65, 80]

print("AI Usage Growth (2019–2024)\n")
print("Year | AI Usage (%) | Visual Representation")
print("-------------------------------------------")

for year, usage in zip(years, ai_usage):
    bar = '#' * (usage // 2)  # ASCII bar, scaled down
    print(f"{year} | {usage:>11}% | {bar}")

