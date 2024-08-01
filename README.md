# Arithmetic Vertical Arranger

###### Technologies:
<p align="center">
<img src="https://img.icons8.com/color/75/000000/python.png" width="75" height="75" alt="Python" style="margin: 10px 15px 0 15px;" />
</p>

### Try it!

To run the Arithmetic Vertical Arranger application, follow the instructions in the Setup section below.

## Project Structure

- `main.py`: Contains the implementation of the Arithmetic Vertical Arranger function.

## Setup

### Prerequisites

- Python 3 installed

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/creinis/arith-arranger-fcc-scicomp-py-cert.git
   cd arith-arranger-fcc-scicomp-py-cert
   ```

2. Run the Arithmetic Vertical Arranger script:
   ```bash
   python3 main.py
   ```

## Arithmetic Vertical Arranger

### Functionality

The Arithmetic Vertical Arranger arranges arithmetic problems vertically to make them easier to solve, as commonly done by students in primary school. It supports addition and subtraction problems and can optionally display the answers.

### Practical Use Case

The Arithmetic Vertical Arranger is useful for educational purposes, helping students visualize arithmetic problems in a clear and organized manner. This tool can be used by teachers to prepare exercises or by students to check their homework.

### Benefits

- **Error Handling:** Provides meaningful error messages for improperly formatted problems.
- **Flexibility:** Supports both addition and subtraction problems.
- **Optional Answers:** Can display answers if the user requests it.
- **Formatted Output:** Displays problems neatly arranged vertically and side-by-side.

## How to Use

1. Run the `main.py` script:
   ```bash
   python3 main.py
   ```

2. Call the `arithmetic_arranger` function with a list of arithmetic problems. Optionally, pass `True` as the second argument to display the answers.

### Example Usage

#### Without Answers
```python
from main import arithmetic_arranger

problems1 = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems1))
```

Output:
```
   32      3801      45      123
+ 698    -    2    +  43    +  49
-----    ------    ----    -----
```

#### With Answers
```python
from main import arithmetic_arranger

problems2 = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
print(arithmetic_arranger(problems2, True))
```

Output:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

## Rules

The function will return the correct conversion if the supplied problems are properly formatted. Otherwise, it will return a string that describes an error that is meaningful to the user.

### Error Conditions

* **Too many problems:** If there are more than five problems supplied.
  - Returns: **Error: Too many problems.**
* **Invalid operator:** If an operator other than addition or subtraction is used.
  - Returns: **Error: Operator must be '+' or '-'.**
* **Non-digit operands:** If any operand contains non-digit characters.
  - Returns: **Error: Numbers must only contain digits.**
* **Operands too long:** If any operand has more than four digits.
  - Returns: **Error: Numbers cannot be more than four digits.**

### Formatting Rules

* **Operator and operands alignment:** Single space between the operator and the longest of the two operands, operator on the same line as the second operand.
* **Right alignment:** Numbers are right-aligned.
* **Spacing between problems:** Four spaces between each problem.
* **Dashes:** Dashes at the bottom of each problem, running the entire length of the problem.

---
#### This is a FreeCodeCamp Challenge for Scientific Computing with Python Projects Certification.
<p align="center">
<img src="https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg" width="250" height="75" alt="freeCodeCamp" style="margin: 0 15px; opacity: 0.6" />
</p>
