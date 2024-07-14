##Latihan Matrix
#1
print("1.")
matriks=([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])
for i in range(4): 
    for j in range(4):
        if i>j: 
            matriks[i][j]=0
        if i<=j:
            matriks[i][j]=j+1
for i in range(4): 
    print(matriks[i])
#2
print("2.")
matriks=([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])
for i in range(4): 
    for j in range(4):
        if i<j:
            matriks[i][j]=0
        if i>=j:
            matriks[i][j]=i+1
for i in range(4): 
    print(matriks[i])
#3
print("3.")
matriks=([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])
for i in range(4): 
    for j in range(4):
        if i==j:
            matriks[i][j]=1
        if i<j: 
            matriks[i][j]=0
        if i>j:
            matriks[i][j]=0
for i in range(4): 
    print(matriks[i])
#4
print("4.")
nilai = [1,2,3,4]
for i in range(len(nilai)):
    nilai[i]=2*i+1 
    print(nilai[i])