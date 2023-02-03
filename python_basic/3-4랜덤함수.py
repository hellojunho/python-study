### 함수 ###

print(abs(-5))      # 절댓값
print(pow(4, 2))    # 4^2 = 16
print(max(5, 12))   # 최댓값
print(min(5, 12))   # 최솟값
print(round(3.14))  # 소수점 반올림
print(round(4.99))

from math import *  # math의 메소드 전부 사용

print(floor(4.99))  # 소수점 내림
print(ceil(3.14))   # 소수점 올림
print(sqrt(16))     # 제곱근

from random import *

print(random())             # 난수 출력 0.0 이상 ~ 1.0 미만
print(random() * 10)        # 0.0 ~ 10.0 미만의 난수 값
print(int(random() * 10))   # 0 ~ 10 미만의 정수형 난수값
print(int(random() * 10) + 1)   # 1 ~ 10 이하의 정수형 난수


print(int(random() * 45) + 1)   # 1 ~ 45 이하의 값 출력
print(randrange(1, 46))         # 1 ~ 46 미만의 정수 값 출력
print(randint(1, 45))           # 1 ~ 45 이하의 정수형 난수 출력
