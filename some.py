"""Task 
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
Input Format

The first line contains the first integer, . The second line contains the second integer, .

Constraints

 

Output Format"""


def calc(a, b):
    functions = {
        "sum": lambda x, y: x + y,
        "diff": lambda x, y: x - y,
        "prod": lambda x, y: x * y,
        "div": lambda x, y: x // y,
        "sub": lambda x, y: x % y,
    }
    for func in functions:
        print(func, ': ', functions[func](a, b))


calc(1, 2)
