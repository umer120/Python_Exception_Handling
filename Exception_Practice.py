
try: # defines a block where error might occur
    x=10/0
except ZeroDivisionError as e: # Catches and handles specific or general exceptions
    print(f"Error: {e}")


try:
    z=10/2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else: # Executes when no exceptions occur in the "try" block
    print("No Error, result:",z)
    

try:
    y=14/2
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally: # Always runs
    print("Execution completes!")
    
    


# Handling Multiple Exceptions
try:
    num=int(input("Enter a number: "))
    result=10/num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
    


# Index out of range
numbers = [10,20,30]

try:
    index=int(input("Enter index(0-2): "))
    print("Value:",numbers[index])
except IndexError:
    print("Error: Index Out of range!")



# File not found
try:
    file=open("data.txt","r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("\nError: File not found")

        



