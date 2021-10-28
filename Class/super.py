class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__() 
        # 다중 상속을 받을 때 첫번째 클래스만 받아오게 됌
        Unit.__init__(self)
        Flyable.__init__(self) # 다중 상속 받을 때 각각의 클래스를 명시해 주어야 함.
# 드랍쉽
dropship = FlyableUnit()