lst = [5,6,4,2,1]
idx = len(lst)

while True :
    idx-=1
    for j in range(idx) :
        if lst[j] > lst[j+1] :
            lst[j],lst[j+1] = lst[j+1],lst[j]
        print(lst)
        
    if idx < 1 :
        break

    #print(lst)

print("Bubble Sort : ",lst)
