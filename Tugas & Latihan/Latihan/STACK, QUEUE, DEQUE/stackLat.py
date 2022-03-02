import stack as st

data = st.stack()
st.push(data,3)

print(data)

for i in range(3) :
    st.push(data,i)

print(data)

for i in range(2) :
    st.pop(data)

print(data)
print(st.pop(data))
def reverseWrd(wrd) :
    wrl = st.stack()
    wrn = ""
    for w in wrd :
        wrl.append(w)

    for i in range(len(wrl)) :
        wr = st.pop(wrl)
        wrn+=wr

    return wrn

wrd = "aku"
print(reverseWrd(wrd))

def binDes(biner) :
    stBin = st.stack()
    desTot = 0
    for bi in biner :
        st.push(stBin,int(bi))

    
    for i in range(len(stBin)) :
        
        de = (2*stBin.pop())**i
        desTot+=de
        print(de)
    return desTot




print(binDes("10111"))
                
