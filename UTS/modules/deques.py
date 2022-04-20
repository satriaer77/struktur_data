def createDeque() :
    return []


def addFront(d,val) :
    d.insert(0,val)
    return d

def addRear(d,val) :
    d.append(val)
    return d

def removeFront(d) :
    val = d.pop(0)
    return val

def removeRear(d) :
    val = d.pop()
    return val

def isEmpty(d) :
    return d==[]

def size(d) :
    return len(d)
