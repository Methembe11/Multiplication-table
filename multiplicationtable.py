def multiplication_table(number, limit=20):
    print(f"\nMultiplication Table for {number} (up to {limit}):\n")
    
    for i in range(1, limit + 1):
        print(f"{number} × {i} = {number * i}")

try:
    num = int(input("Enter a number: "))
    
    if num < 0:
        print("Please enter a positive number.")
    else:
        multiplication_table(num)

except ValueError:
    print("Invalid input. Please enter a number.")