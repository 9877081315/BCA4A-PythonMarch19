# factorial of a number

print("Name: Suniti")
print("Roll No: 2210997248")

num = int(input("Enter a number: "))
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i = i + 1
print(f"Factorial of {num} is {fact}")
