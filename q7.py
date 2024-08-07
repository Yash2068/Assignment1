number = int(input("Enter a number to print its multiplication table: "))

i = 1

print(f"Multiplication table for {number}:")
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1
