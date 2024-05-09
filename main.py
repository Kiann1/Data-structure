from src.queue_1 import Queue


q = Queue(10) # (front of queue)[](back of queue)
q.enqueue("ra'na") # ["ra'na"]
q.enqueue("vez") # ["ra'na", "vez"]
q.enqueue("Arya") # ["ra'na", "vez", "Arya"]
print("queue size is: ",q.size())
print(q.dequeue(), "left the queue") # ["vez", "Arya"]
print("front of queue is:",q.front())
q.enqueue("milda") # ["vez", "Arya", "milda"]
removed_item = q.remove_item(1)
print("Removed item: " , removed_item) # ["vez", "milda"]
q.enqueue("Kian") # ["vez", "milda", "Kian"]
print("queue size is: ",q.size())
q.dequeue() # ["milda","Kian"]
print("queue size is: ",q.size())
q.dequeue() # ["Kian"]
print("queue size is: ",q.size())
q.dequeue() # []
print("queue size is: ",q.size())
print("It was a queue")