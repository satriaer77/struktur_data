import sys
import os
  

current = os.path.dirname(os.path.realpath(__file__))

parent = os.path.dirname(current)
  

print(sys.path.append(parent))
  
from modules import queue as que

q = que.createQueue()

que.enqueue(q,2)

 

def dragonSnake(anak,hitungan) :
    queAnak = que.createQueue()

    for nama in anak : 
        que.enqueue(queAnak,nama)

    while len(queAnak) > 1 :
        for i in range(hitungan) :
            a = que.enqueue(queAnak,que.dequeue(queAnak))
            print(a)
        que.dequeue(queAnak)
    print(queAnak)


print("""

+------------------------------+
     PERMAINAN   ULAR NAGA
+------------------------------+



        """)

listAnak = ["Jaka","Saputra","Henry","Odegaard"]

dragonSnake(listAnak,6)
