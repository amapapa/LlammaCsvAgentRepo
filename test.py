import pandas as pd


def add_numbers(a, b):
    return a + b


# Example usage
num1 = 5
num2 = 7
result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is {result}")
print("This is a test file.")

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df.head()
