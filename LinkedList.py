
class Node:
    def __init__(self,prev = None, data = 0,next = None,link = 0) -> None:
        self.prev = prev
        self.data = data
        self.next = next
        self.link = link



class LinkedList:
    def __init__(self) -> None:
        self.nodes = {}
        self.number = 1
        self.first = 0
        self.last = 0
        
    
    def is_empty(self) -> bool:
        if len(self.nodes) == 0:
            return True
        else:
            return False
    
    def get_link(self):
        link = "key"+str(self.number)
        self.number += 1
        return link

    def prepend(self,data:any ):
        if len(self.nodes) == 0:
            link = self.get_link()
            self.nodes[link] = Node(None,data,None,link)
            self.first = self.nodes[link]
            self.last = self.nodes[link]

        else:
            link = self.get_link()
            new_node = Node(None,data,self.first.link,link)
            self.first.prev = link
            self.nodes[link] = new_node
            self.first = new_node


    def append(self,data:any ):
        if len(self.nodes) == 0:
            link = self.get_link()
            self.nodes[link] = Node(None,data,None,link)

            self.first = self.nodes[link]
            self.last = self.nodes[link]

        else:
            link = self.get_link()
            new_node = Node(self.last.link,data,None,link)
            self.last.next = link
            self.nodes[link] = new_node
            self.last = new_node
    
    
    def insert_after(self,target_data, data):
        for i in self.nodes:
            if  self.nodes[i].data == target_data:
                
                link = self.get_link()

                new_node = Node(self.nodes[i].link,data,self.nodes[i].next,link)
                
                if self.nodes[i].next != None:
                    self.nodes[self.nodes[i].next].prev = link
                else:
                    self.last = new_node

                self.nodes[link] = new_node

                self.nodes[i].next = link

                break

    def insert_before(self,target_data, data):
        for i in self.nodes:
            if  self.nodes[i].data == target_data:
                
                link = self.get_link()

                new_node = Node(self.nodes[i].prev,data,self.nodes[i].link,link)
                
                if self.nodes[i].prev != None:
                    self.nodes[self.nodes[i].prev].next = link
                else:
                    self.first = new_node

                self.nodes[link] = new_node

                self.nodes[i].prev = link

                break

    def delete(self,data):
         for i in self.nodes:
            if  self.nodes[i].data == data:

                if self.nodes[i] is self.first:
                    self.first = self.nodes[self.nodes[i].next]
                    self.nodes[self.nodes[i].next].prev = None
                    del(self.nodes[i])
                    break


                if self.nodes[i] is self.last:
                    self.last =  self.nodes[self.nodes[i].prev]
                    self.nodes[self.nodes[i].prev].next = None
                    del(self.nodes[i])
                    break

                self.nodes[self.nodes[i].next].prev = self.nodes[i].prev
                self.nodes[self.nodes[i].prev].next = self.nodes[i].next
                del(self.nodes[i]) 
                break
        
                
    def display(self):
        
        new_first  = self.first
        while new_first.next != None:
            print(f"prev = {new_first.prev} data = {new_first.data} next = {new_first.next} link = {new_first.link}")
            new_first = self.nodes[new_first.next]
        print(f"prev = {new_first.prev} data = {new_first.data} next = {new_first.next} link = {new_first.link}")




L = LinkedList()


L.prepend(1)
L.prepend(2)
L.append(3)
L.insert_after(1,4)
L.insert_before(1,5)
L.delete(2)

L.display()