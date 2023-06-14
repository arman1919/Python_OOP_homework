class repair:
    def fix(car):
        print (f"repaired {car.engine} engine/propeller")
        print (f"repaired {car.wheel} wheels/wings")
        print (f"repaired {car.door} door")


class car:
    def __init__(self,engine = 1,door = 4,wheel = 4,) -> None:
        self.engine = engine
        self.door = door
        self.wheel = wheel
        

class plane:
    def __init__(self,wings = 2,door = 1,propeller = 1) -> None:
        self.wings = wings
        self.door = door
        self.propeller = propeller

class adapter_palne(repair):
    def __init__(self,palne) -> None:
        self.engine = palne.propeller
        self.door = palne.door
        self.wheel = palne.wings

    

    
    


car1 = car()
palne1 = plane()

repair.fix(car1)

# repair.fix(palne1)  AttributeError

adapt_palne = adapter_palne(palne1)

print()

repair.fix(adapt_palne)





