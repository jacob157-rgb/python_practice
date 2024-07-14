def BubbleSort(X):
    for i in range(len(X)-1,0,-1):
        Max=0
        for l in range(1,i+1):
            if X[l]>X[Max]: 
                Max = l
        temp = X[i] 
        X[i] = X[Max] 
        X[Max] = temp
        print(X)
Hasil = [26,2,17,45,12,28] 
BubbleSort(Hasil) 
print(Hasil)