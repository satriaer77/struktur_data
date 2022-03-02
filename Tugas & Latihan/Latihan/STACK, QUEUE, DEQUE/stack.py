def stack() :
    stck = []
    return stck


def push(s,data) :
    s.append(data)

def pop(s) :
    dt = s.pop()
    return dt

def peek(s) :
    return s[len(s)-1]

def isEmpty(s) :
    return s==[]

def size(s) :
    return len(s)

