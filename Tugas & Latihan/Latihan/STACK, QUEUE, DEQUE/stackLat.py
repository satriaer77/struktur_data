#------ Add Parent Directory using file path
#import sys
#import os
#  
#
#current = os.path.dirname(os.path.realpath(__file__))
#
#parent = os.path.dirname(current)
#  
#sys.path.append(parent)
#-----------------------------------

#Add parent directory
import sys
sys.path.append("..")

from modules import stack as st


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
        st.push(wrl,w)

    for i in range(len(wrl)) :
        wr = st.pop(wrl)
        wrn+=wr

    return wrn

wrd = "aku"
print(reverseWrd(wrd))

def binDes(biner) :
    stBin  = st.stack()
    desTot = -1

    for bi in biner :
        st.push(stBin,int(bi))
    print(stBin)
    for i in range(len(stBin)) :
        #de = stBin.pop()
        #desTot = desTot + (2*de)**i
        desTot+=(2*stBin.pop())**i    
    return desTot

def binDesv2(biner) :
    stBin  = st.stack()
    desTot = 0

    for bi in biner :
        st.push(stBin,int(bi))
    
    for i in range(len(stBin)) :
        popS = st.pop(stBin)

        if popS != 0 :
            desTot+=(2*popS)**i
    return desTot

        

def desBin(desimal) :
    stDes  = st.stack()
    binStr = ""
    while desimal > 0 :
        desimal = desimal//2
        st.push(stDes,desimal%2)

    return stDes


print("""
Biner   = %s
Desimal = %d

        """ % 
 (
    desBin(10),
    binDes("1010")
 )
)
print(type(0.0))
#print("asd ",0**0)
                
