# 🧮 Functions for "Varied Amount of Input Data" Program

## 1. `parse_input()`
- **Purpose:** Collect the raw input from the user (a line of numbers).
- **Output:** A list of floats (e.g., `[14.25, 25.0, 0.0, 5.75]`).
- needs to accept numbers. 
Needs to reject non numbers
needs to ask user to correct anything that is not a number.
needs to ask user if the list is complete.
needs to ask user if they want to add more numbers.
ask user if they are ready to proceed past the parsing input phase.

---

## 2. `calculate_max(values)`
- **Purpose:** Find the maximum number in the list.
- **Input:** A list of floats.
- **Output:** A single float (the largest number).
be able to identify if there is a tie

---

## 3. `calculate_average(values)`
- **Purpose:** Compute the average of all numbers in the list.
- **Input:** A list of floats.
- **Output:** A single float (the average value).
be able to round this to the appropriate number of significant digits

---

## 4. `format_results(max_val, avg_val)`
- **Purpose:** Format the maximum and average values so they display with **two digits after the decimal**.
- **Input:** Two floats.
- **Output:** A formatted string (e.g., `"25.00 11.25"`).

---

## 5. `main()`
- **Purpose:** Tie it all together.
- **Steps:**
  1. Call `parse_input()` to get the numbers.
  2. Call `calculate_max()` to get the max.
  3. Call `calculate_average()` to get the average.
  4. Call `format_results()` to prepare the output.
  5. Print the result.

---
