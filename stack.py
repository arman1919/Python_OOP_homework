import typing

class Steck():

    def __init__(self) -> None:
        self.steck = []
        self.index = 0
    
    def push(self,element:typing.Any):
        self.steck.append(element)
        self.index +=1
        

    def pop(self):
        temp = self.steck[-1]
        self.steck.pop()
        self.index -= 1
        return temp
    
        
    
    def __str__(self) -> str:
        res = ''
        for i in self.steck:
            res += str(i) + ", "
        return res 
    
    def iter(self):
        self.index = len(self.steck)
        return self

    def next(self,iterator: typing.Iterator):
        if iterator.index == 0:
            raise StopIteration
        
        temp = iterator.steck[iterator.index - 1 ]
        iterator.index -= 1 
        return temp
        


s= Steck()
s.push(15)
s.push("aa")
s.push(25)

a = s.iter()
print(s.next(a))
print(s.next(a))
print(s.next(a))
print(s.next(a))

       