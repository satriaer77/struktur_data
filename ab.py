from Praktikum.Praktikum4.modules import queue as que


def taskScheduling(timeLimit) :
    taskTotal = int(input("==> Masukkan jumlah task = ")) 
    taskData  = que.createQueue()
    
    for i in range(taskTotal) :
        taskName = input("=> Masukkan nama task = ")
        taskTime = int(input("=> Masukkan waktu task = "))
        
        que.enqueue(taskData,[taskName,taskTime])
    
    print("Waktu Proses CPU = ",timeLimit)
    print("Antrian proses beserta waktunya = ",taskData)
    numIteration = 1
    
    while not(que.isEmpty(taskData)) :
        limitTemp = timeLimit
        nowTask = que.dequeue(taskData)
        
        while nowTask[1] > 0 and limitTemp > 0 :
            limitTemp-=1        
            nowTask[1]-=1
        
        if nowTask[1] > 0 :
            print("\nProses %s sedang diproses dan sisa waktu proses = %d" % (nowTask[0],nowTask[1]) )
            print("Data proses yang tersisa = ",taskData)
            que.enqueue(taskData,nowTask)

        else : 
            print("\nProses %s telah diproses" % (nowTask[0]))
            print("Data proses yang tersisa = ",taskData)

taskScheduling(3)
