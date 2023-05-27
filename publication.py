class publication():
    
    def __init__(self,title:str,price:int):
        self.title = title
        self.price = price

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        self._title = new_title
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        self._price = new_price

    
    
    
    


    

class book(publication):
    def __init__(self, title: str, price: int,count_of_pages: int):
        super().__init__(title, price)
        self.count_of_pages = count_of_pages
    
    
    def getdata(self):
        return f"Title - {self.title} Price - {self.price} Count of page - {self.count_of_pages}"
    
    
    def setdata(self,new_title,new_price,new_count_of_pages):
        self.title = new_title
        self.price = new_price
        self.count_of_pages = new_count_of_pages



    
class Tape(publication):
    def __init__(self, title: str, price: int,playing_time: int):
        super().__init__(title, price)
        self.playing_time = playing_time

    
    def getdata(self):
        return f"Title - {self.title} Price - {self.price} Count of page - {self.playing_time}"
    
    
    def setdata(self,new_title,new_price,new_playing_time):
        self.title = new_title
        self.price = new_price
        self.playing_time = new_playing_time




book1 = book("Python tasks",156,1574)

tape1 = Tape("Python song",56,15)

print(book1.getdata())




