## 2.14 LAB: Driving costs

*Major steps outline (Markdown document style)*

### Goal

Read two floating-point inputs:

* **gas_mileage_mpg** (miles per gallon)
* **gas_price_per_gallon** (dollars per gallon)

Then compute and print the **fuel cost** to drive:

* **20 miles**
* **75 miles**
* **500 miles**

All outputs must be formatted to **two digits after the decimal** on a **single line**, separated by spaces.

---

### Inputs

1. Read **gas_mileage_mpg** as a float
2. Read **gas_price_per_gallon** as a float

---

### Core idea

To find the gas cost for a given distance:

1. **Gallons needed**
   [
   \text{gallons} = \frac{\text{miles}}{\text{miles per gallon}}
   ]

2. **Cost**
   [
   \text{cost} = \text{gallons} \times \text{dollars per gallon}
   ]

So, for each distance (20, 75, 500), compute:

* `gallons_needed = distance / gas_mileage_mpg`
* `cost_for_distance = gallons_needed * gas_price_per_gallon`

---

### Step-by-step plan

1. **Read inputs**

   * Store `gas_mileage_mpg`
   * Store `gas_price_per_gallon`

2. **Compute costs for each target distance**

   * For **20 miles**: compute `cost_20`
   * For **75 miles**: compute `cost_75`
   * For **500 miles**: compute `cost_500`

3. **Format output**

   * Print all three costs on one line
   * Use **two decimal places** for each number
   * Ensure spacing matches the example format:

     * `cost_20 cost_75 cost_500`
     * each with `:.2f`

---

### Quick self-check with the sample

Given:

* mpg = 25.0
* price = 3.1599

You should get costs that match:

* 20 miles → **2.53**
* 75 miles → **9.48**
* 500 miles → **63.20**

---

### Output requirements

* One line
* Three values
* Two decimals each
* Spaces between values, no extra text (so the autograder stays happy)
