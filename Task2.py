import math

def calculate_math(num):
    """
    calculates square root, logarithm and sine of a given number.

    parameter:
        num(int/float): a positive number for calculations
    Returns:
        None: prints the calculated values
    
    Examples:
        calculate_math(9) -> suare root: 3.0, Logarithm: 2.197, Sine: 0.412

    """
    square_root = math.sqrt(num) # evaluatig square root of num

    logarithm = math.log(num) # evaluating logarithm of num

    sine_of_num = math.sin(num) # evaluating sine of num

    print(f"Square root: {square_root}")

    print(f"Logarithm: {logarithm}")

    print(f"Sine: {sine_of_num}")



def main():
    """
    Main function to run the math calculations program.
    """
    try:
        num = int(input("enter a number: ")) # taking user input of a number

        if num <= 0: # input validation -log and sqrt not defined for negative numbers and zero

            print("Error: Please enter a positive number greater than 0.")
        else:
            calculate_math(num) # calling calculate_math function
    
    except ValueError:
        print("Error: Please enter a valid whole number.")

if __name__=="__main__": # runs only when files executed directly
    main()







