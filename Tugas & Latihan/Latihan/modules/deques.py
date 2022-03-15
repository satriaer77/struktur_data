def createDeque() :
    return []


def addFront(d,val) :
    d.insert(0,val)


def addRear(d,val) :
    d.append(val)
    return d

def removeFront(d) :
    return d.pop(0)

def removerRear(d) :
    return d.pop

def isEmpty(d) :
    return d==[]

def size(d) :
    return len(d)
