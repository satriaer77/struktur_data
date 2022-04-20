lst = [5,6,4,2,1]
idx = len(lst)
print(idx)

while idx < 1:
    idx-=1
    sts = False
    
    if sts :
        for j in range(idx) :
            print("\nIterasi",j)
            if lst[idx-1] < lst[idx] :
                lst[idx-1],lst[idx] = lst[idx],lst[idx-1]
                print(lst)
        sts = False
        
    else :
        for j in range(idx) :
            print("\nIterasi ",j)
            if lst[j] > lst[j+1] :
                lst[j],lst[j+1] = lst[j+1],lst[j]
                print(lst)
        sts = True
     

print("Bubble Sort : ",lst)

