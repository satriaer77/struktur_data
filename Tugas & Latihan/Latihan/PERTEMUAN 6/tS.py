import sys
sys.path.append("..")

from modules import queueV2 as que

dataProses = {}
for i in range(3) :
    nama = input("=> Masukkan nama : ")
    dataProses[nama] = int(input("=> Masukkan Waktu : "))
    
def taskScheduling(dictTask,limit) :
    print(dictTask)
    queTask   = que.createQueue()
    queTime   = que.createQueue()
    totalTime = 0
    for dt in dictTask.keys() :
        que.enqueue(queTask,dt)
        
    for dtm in dictTask.values() :
        que.enqueue(queTime,dtm)
    
    print(queTask)
    
    #for i in range(que.size(queTask)) :
   #     print(queTask)
     #   que.enqueue(queTask,que.dequeue(queTask))
    
    while que.isEmpty(queTask) :
        print(queTask)

        limitTemp = limit
        task      = que.dequeue(queTask)
        time      = que.dequeue(queTime)
        
        while limitTemp > 0 :            
            limitTemp-=1
            if time > 0 :
                time-=1
                totalTime+=1

        if time > 0 :    
            que.enqueue(queTime,time)
            que.enqueue(queTask,task)
    
    return totalTime
        
print(taskScheduling(dataProses,3))
