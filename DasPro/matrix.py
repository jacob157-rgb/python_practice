X = [
    [12,7,3],
    [4 ,5,6],
    [7 ,8,9],
    [7 ,8,9]
]

Y = [
    [5,8,1],
    [6,7,3],
    [4,5,9],
    [4,5,9]
]

result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

for r in result:
   print(r)