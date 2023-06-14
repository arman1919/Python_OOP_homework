import typing

class Queue():
    def __init__(self) -> None:
        self.queue = []
        self.index = 0

    def Enqueue(self,element : typing.Any):
        self.queue.append(element)
        self.index += 1
        
        
    def Dequeue(self):
        temp = self.queue[0]
        self.queue.pop(0)
        self.index -= 1

        return temp
    
    def __str__(self) -> str:
        res = ""
        for i in self.queue:
            res += i + ", "
        return res
    
    
    def iter(self):
        self.index = len(self.queue)
        return self

    def next(self,iterator: typing.Iterator):
        if iterator.index == 0:
            raise StopIteration
        
        temp = iterator.queue[iterator.index - 1 ]
        iterator.index -= 1 
        return temp
    


q = Queue()

q.Enqueue("Human 1")
q.Enqueue("Human 2")
q.Enqueue("Human 3")
print(q)
print("out of the queue",q.Dequeue())
print(q)
q.Enqueue("Human 4")
print(q)

i = q.iter()
print(q.next(i))
print(q.next(i))
print(q.next(i))
print(q.next(i))

