### 지역변수 & 전역변수 ###
# 지역변수 : 함수 내에서만 사용 가능
# 전역변수 : 프로그램 전체에서 사용 가능

gun = 10   # 총 10자루

def checkpoint(soldiers):  # 경계 근무 함수
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers         # 경계 근무 병사 수 만큼 총의 개수가 줄어든다
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun -= soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
#checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))