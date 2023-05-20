class MyMeta:
    def __init__(self) -> None:
        print("new class is created")

    

class MyClass(MyMeta):
    def __init__(self) -> None:
        super().__init__()


newobject = MyClass()
