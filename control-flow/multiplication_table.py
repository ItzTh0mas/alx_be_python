number = int(input("Enter a number to see its multiplication table: "))

for inc in range(1, 11):
    multi = number * inc
    print(f"{number} * {inc} = {multi}")

