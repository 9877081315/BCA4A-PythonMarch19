#print triangle pattern

print("Name: Suniti")
print("Roll No: 2210997248")

n = int(input("Enter number of rows: "))
for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end=' ')
    print()
