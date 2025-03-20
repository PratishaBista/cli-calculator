from dev1_addition import add
from dev2_subtraction import subtract
from dev3_multiplication import multiply
from dev4_division import divide

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers.")
            return

        if choice == '1':
            print("Result:", add(a, b))
        elif choice == '2':
            print("Result:", subtract(a, b))
        elif choice == '3':
            print("Result:", multiply(a, b))
        elif choice == '4':
            print("Result:", divide(a, b))
    else:
        print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator()
