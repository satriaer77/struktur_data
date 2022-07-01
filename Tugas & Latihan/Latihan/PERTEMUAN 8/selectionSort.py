akg    = [9,4,5,2,3,1]

start  = 0
lenAkg = len(akg)

for i in range(1,lenAkg) :
    print(flag,i)
    if akg[flag] > akg[i] :
        flag = i 

akg[flag], akg[start] = akg[start],akg[flag]
print(akg)
print(flag)
    #print(i):
