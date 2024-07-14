def seqSearch(data, key):
    i=0
    pos = i + 1 
    while(i<len(data)):
        if data[i] == key: 
            break
        i+=1
        pos=i+1
    if pos <= len(data):
        print('data', key, 'ditemukan di posisi', pos)
    else:
        print('data tidak ditemukan') 
        return pos
data=[10, 4, 9, 1, 7, 15] 
seqSearch(data,15)