class Stack() :    

    @staticmethod 
    def createStack() :
        stck = []
        return stck

    @staticmethod 
    def push(s,data) :
        s.append(data)

    @staticmethod 
    def pop(s) :
        dt = s.pop()
        return dt

    @staticmethod
    def peek(s) :
        return s[len(s)-1]

    @staticmethod
    def isEmpty(s) :
        return s==[]
    
    @staticmethod
    def size(s) :
        return len(s)

