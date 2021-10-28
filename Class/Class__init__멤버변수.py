class Unit: # class -> 틀과 같은 역할, 객체를 찍어낼 수 있음datetime A combination of a date and a time. Attributes: ()
    def __init__(self, name, hp, damage): # __init__ -> 생성자: 객체 생성시 자동으로 호출되는 부문
        self.name = name
        self.hp = hp
        self.damage = damage # self.--- -> 멤버변수 : class 내에서 정의된 변수
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35) # class 로부터 만들어지는 객체-> 위의 class 의 인스턴스


# 객체를 생성할 때 init 함수의 개수 만큼(self 제외) 값을 설정 해야함.

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마컨당한 레이스
wraith2 = Unit("마컨당한 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
     # class 외부에서 변수를 추가로 할당함. 확장을 한 객체(마컨 레이스)에만 적용이 됌.