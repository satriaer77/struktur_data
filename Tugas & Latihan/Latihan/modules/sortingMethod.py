def mySort(lst) :
    n = 0
    lstnw = []
    while True :
        for ls in lst :
            n = ls 
            for ls2 in lst :
                if(n > ls2) :
                    n = ls2

            if len(lst) > 0 :
                print(lst)
                lst.remove(n)
                lstnw.append(n)

            
        if len(lst) <= 0 :
            break

           
    return lstnw

def bubbleSort() :
