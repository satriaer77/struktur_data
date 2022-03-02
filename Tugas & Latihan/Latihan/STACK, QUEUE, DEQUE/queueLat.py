import queue as que

q = que.createQueue()

que.enqueue(q,2)

print(q)


def dragonSnake(anak,hitungan) :
    queAnak = que.createQueue()

    for nama in anak 
        que.enqueue(queAnak,nama)

    while len(queAnak) > 1 :
        for i in range(hitungan) :
            que.enqueue(queAnak,que.dequeue(queAnak))

        que.dequeue(queAnak)
    print(queAnak)


print("""

+------------------------------+
     PERMAINAN   ULAR NAGA
+------------------------------+




        """)

listAnak = ["Jaka","Saputra","Henry","Odegaard"]

dragonSnake(listAnak,6)
