### Simple String Calculator 

A String calculator built using Test-Driven-Development(TDD) approach, as part of the Incubyte recruitment process.

It contains a  ```StrignCalculator``` class with single method 
```python
add(input : string) -> int 
```
 It takes a string containing numbers(seperated by delimeters) and returns sum of the numbers.

------------------------------------------------------------------------

### Development Approach :  

To implement the desired method, I followed the Test-Driven Development (TDD) methodology, which follows the Red-Green-Refactor cycle. For each incremental feature:

- I first wrote a **failing test (Red)** to define the expected behavior,

- Then implemented the minimal code required to **pass the test (Green)**,

- And finally **refactored the code for clarity**, efficiency, and maintainability (Refactor/Purple).

This disciplined approach ensured that each feature was tested, robust, and built incrementally.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Technologies Used : 
 - **Programming Language**: Python
 - **Testing** : ```unittest``` Module for writing unit tests.
 - **Design-paradigm** : Object-Oriented Programming

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Included Test Cases : 

| Test Case Description                                      | Input                         | Expected Output              | Status |
|------------------------------------------------------------|-------------------------------|------------------------------|--------|
| Returns 0 for empty string                                 | `""`                          | `0`                          |  Pass |
| Returns number itself for single value input               | `"1"`                         | `1`                          | Pass |
| Returns sum for two numbers                                | `"1,2"`                       | `3`                          | Pass |
| Returns sum for multiple numbers                           | `"1,2,3,4"`                   | `10`                         | Pass |
| Supports newline as delimiter (mixed with comma)           | `"1\n2,3"`                    | `6`                          | Pass |
| Handles newline-delimited input                            | `"5\n2"`                      | `7`                          | Pass |
| Handles multiple newlines                                  | `"5\n1\n5"`                   | `11`                         | Pass |
| Supports custom delimiter `;`                              | `"//;\n1;2"`                  | `3`                          | Pass |
| Supports custom delimiter with more numbers                | `"//;\n1;2;1"`                | `4`                          | Pass |
| Raises error for single negative number                    | `"-1"`                        | Exception with message       | Pass |
| Raises error for multiple negative numbers                 | `"-1,-2,3"`                   | Exception with message       | Pass |
| Ignores numbers greater than 1000                          | `"1000,1,2000"`               | `1001`                       | Pass |
| Returns 0 when all numbers > 1000                          | `"1001"`                      | `0`                          | Pass |
| Supports custom delimiter with multiple characters         | `"//[***]\n2***2***2"`        | `6`                          | Pass |
| Supports multiple custom delimiters `*` and `%`            | `"//[*][%]\n3%1*3"`           | `7`                          | Pass |
| Supports multi-length custom delimiters `***` and `%`      | `"//[***][%]\n3%1***3"`       | `7`                          | Pass |

-------------------------------------------------------------------------------------------------------------------------------------------------

### How to Run :
1. Clone the Repository : ```git clone https://github.com/ArchanSureja/Incubyte_TDD_Assesment.git```
2. Change Directory to src : ```cd src```
3. Using StringCalculator :
     ```python
     from string_calc import StringCalculator
     print(StringCalculator.add("1,2,2")) # print 5 
     ```
4. Running Tests : ```python3 test.string_calc.py```
-------------------------------------------------------------------------------------------------------------------------------------------------
### Screenshot :

![image](https://github.com/user-attachments/assets/3aeb23ee-ae2b-4f7a-9344-26dba1416e41)

### Refrences : 
- [Three laws of TDD by Uncle Bob](https://www.youtube.com/watch?v=qkblc5WRn-U)
- [Detailed TDD Task Description](https://osherove.com/tdd-kata-1/)
- [Unit Testing in python](https://www.freecodecamp.org/news/an-introduction-to-testing-in-python/) 




