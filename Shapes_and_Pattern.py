# This code will print shapes as per user input.

row = int(input("Enter the desired number of rows: "))
column = int(input("Enter the desired number of columns: "))
symbol = int(input("Enter the desired type of symbol: "))

for x in range (row):
    for y in range (column):
        print(symbol, end=" ")
    print()

