class Math:
    @classmethod
    def add(cls, a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        return a * b

    @staticmethod
    def square(x):
        return x ** 2
    

print(Math.add(15,15))
print(Math.multiply(5,4))
print(Math.square(12))