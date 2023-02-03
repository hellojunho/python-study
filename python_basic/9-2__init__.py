### __init__ ###
# 파이썬에서 사용되는 생성자

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0} 공격력: {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
tank2 = Unit("탱크", 150, 35)
wraith1  = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True     # 외부에서 객체에 추가로 변수를 만들어 사용 가능

if(wraith2.clocking == True):
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))