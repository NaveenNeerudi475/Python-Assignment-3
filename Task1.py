
def factorial(num):
    if num == 1: # base case - factorial of 1 is 1, stops recursion
        return 1
    else:
        fact = num * factorial(num - 1) # recursive call - multiplying num with factorial of previous number
        return fact # returning the calculated factorial value
    
num = int(input("enter a number: ")) # taking user input of a number

fact = factorial(num) # storing the return value of factorial function

print(f"Factorial of {num} is: {fact}") # printing the final result
