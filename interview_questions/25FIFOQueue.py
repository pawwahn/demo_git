from collections import deque
from queue import Queue

queue = Queue()
queue.put('a')
queue.put('b')
queue.put('c')
print(list(queue.queue))

rt = queue.get()
print(rt)

print(list(queue.queue))

