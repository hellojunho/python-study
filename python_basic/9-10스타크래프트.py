### 스타크래프트 전반전 ###

# 일반 유닛
from random import *
from time import sleep

class Unit:     # 부모 클래스
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if(self.hp <= 0):
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격 유닛
class AttackUnit(Unit):     # 자식 클래스
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
    
# 마린 클래스
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 일정 시간 동안 이동 속도 및 공격 속도 증가, 자기 체력 10 소모
    def stimpack(self):
        if(self.hp > 10):
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크 클래스
class Tank(AttackUnit):
    # 시즈모드 : 탱크 지상에 고정 -> 이동 불가
    seize_developed = False     # 시즈모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False
    
    def set_seize_mode(self):
        if(Tank.seize_developed == False):
            return

        # 현재 시즈모드가 아닐 때 -> 시즈모드로 전환
        if (self.seize_mode == False):
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        # 현재 시즈모드일 때    -> 시즈모드 해제
        else:
            print("{0} : 시즈모드로 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


# 비행 기능 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 스피드 = 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

# 레이스 클래스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False    # 클로킹 모드 (해제 상태)

    def clocking(self):
        if(self.clocked == True):   # 클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드로 전환합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")


# 게임 진행
game_start()

# 마린 3개 생성
m1 = Marine()
sleep(1)
m2 = Marine()
sleep(1)
m3 = Marine()
sleep(1)

# 탱크 2개 생성
t1 = Tank()
sleep(1)
t2 = Tank()
sleep(1)

# 레이스 1개 생성
w1 = Wraith()
sleep(1)

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

sleep(2)
# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

sleep(2)
# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if(isinstance(unit, Marine)):   # isinstance() : 지금 만들어진 객체가 어떤 클래스의 인스턴스인지 확인
        unit.stimpack()
    elif(isinstance(unit, Tank)):
        unit.set_seize_mode()
    elif(isinstance(unit, Wraith)):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21))    # 공격은 랜덤으로 받음 (5 ~ 20)

# 게임 종료
game_over()