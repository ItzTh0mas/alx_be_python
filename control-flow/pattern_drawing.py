patsize = int(input("Enter the size of the pattern:"))

row = 0

while row < patsize:
    for col in range(patsize):
        print("*", end="")
    print()
    row += 1
