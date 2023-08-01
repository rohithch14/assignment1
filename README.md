# Assignment1

## Fermat's Last Theorem Near Miss Finder
### Description
This program finds near misses for Fermat's Last Theorem. A 'near miss' is defined as a relatively small difference between x^n + y^n and z^n. The program prompts the user for two inputs: n (the power to use in the equation) and k (which limits the range of x and y possibilities to test).

### Requirements
Python 3.x
Installation
Ensure you have Python installed on your system.
Download the fermat_near_miss.py file.
### Usage
Open a terminal or command prompt.
Navigate to the directory where fermat_near_miss.py is located.
Run the command python fermat_near_miss.py.
Follow the on-screen prompts to input values for n and k.
### Output
The program will display the current best combination of x, y, z values every time a new smallest relative miss is found. The final output will be the best combination that results in the smallest relative miss.

Notes
The program may experience performance issues for very large values of n and k due to the computational complexity of the calculations.
