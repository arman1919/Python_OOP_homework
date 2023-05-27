class Vector:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    
    def __neg__(self):
        return(Vector(-self.x,-self.y))
    
    def print_vec(self):
        print("X =",self.x)
        print("Y =",self.y)
        

    def __pos__(self):
        return(Vector(self.x,self.y))

    def __abs__(self):
        return(self.x ** 2 + self.y ** 2) ** 0.5
    
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __ne__(self, other):
        return (self.x != other.x or self.y != other.y)
    
    def __lt__(self, other):
        return self.__abs__() < other.__abs__() 
    
    def __gt__(self, other):
        return self.__abs__() > other.__abs__()

    def __le__(self, other):
        return self.__abs__() <= other.__abs__()
    
    def __ge__(self, other):
        return self.__abs__() >= other.__abs__()

    def __add__(self, other):
        return Vector(self.x + other.x , self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x , self.y - other.y)
    
    def __mul__(self, other):
        return(self.x * other.x + self.y * other.y)
    
    def __truediv__(self, other):

        raise TypeError("The division of vectors is not defined")


    def __floordiv__(self, other):
        raise TypeError("The division of vectors is not defined")
    
    def __mod__(self, other):
        raise TypeError("The division of vectors is not defined")
    
    def __divmod__(self, other):
        raise TypeError("The division of vectors is not defined")
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
    
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y

    def __imul__(self, other):
        raise TypeError("the product of vectors is a number")
    
    def __itruediv__(self, other):
        raise TypeError("The division of vectors is not defined")
    
    def __ifloordiv__(self, other):
        pass

    def __imod__(self, other):
        pass

    
    def __str__(self):
        return("("+str(self.x)+","+str(self.y)+")")
    
    def __repr__(self):
        return("("+str(self.x)+","+str(self.y)+")")
    
    def __format__(self, format_spec):
        pass

    def __len__(self):
        return(self.x ** 2 + self.y ** 2) ** 0.5
    
    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __contains__(self, item):
        pass


vec1 = Vector(3,4)    
vec2 = Vector(5,6)











