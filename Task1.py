
def factorial(num):
    """
    calculates the factorial of a given number recursively.

    parameter:
    num(int): a non-negative integer whose factorial is to be calculated 

    Returns:
    int: factorial of the given number

    Examples:
    factorial(5) -> 120
    factorial(0) -> 1
    """

    if num == 0 or num == 1: # base case - factorial of 1 is 1, stops recursion
        return 1
    
    elif num < 0: # handling negative numbers
        return None
    
    else:
        fact = num * factorial(num - 1) # recursive call - multiplying num with factorial of previous number
        return fact # returning the calculated factorial value
    
def main():
    """
    Main function to run the factorial program.

    """
    try:

        num = int(input("enter a number: ")) # taking user input of a number

        if num < 0: # input validation for negative numbers 
            print("Error: Factorial is not defined for negative numbers. ")
        else:
            fact = factorial (num) # storing return value 
            print(f"Factorial of {num} is: {fact}") # printing final result
        
    except ValueError: # handles non -integer inputs 
        print("Error: please enter a valid whole number.")

if __name__ == "__main__":
    main()
