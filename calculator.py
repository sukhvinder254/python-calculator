# Simple Calculator - Sukhvinder Kaur (2501010272)
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero not allowed."
    return x / y

print("=== Simple Calculator ===")
print("Operations: 1.Add  2.Subtract  3.Multiply  4.Divide")

while True:
    choice = input("\nEnter choice (1/2/3/4) or q to quit: ")

    if choice == 'q':
        print("Thank you! Bye")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
        except:
            print("Invalid input! Enter numbers only.")
            continue

        if choice == '1':
            print(f"{n1} + {n2} = {add(n1, n2)}")
        elif choice == '2':
            print(f"{n1} - {n2} = {subtract(n1, n2)}")
        elif choice == '3':
            print(f"{n1} × {n2} = {multiply(n1, n2)}")
        elif choice == '4':
            print(f"{n1} ÷ {n2} = {divide(n1, n2)}")
    else:
        print("Invalid choice!")