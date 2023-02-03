### 튜플 ###
#변경되지 않는 목록 사용 시, 튜플 사용 -> 리스트보다 속도 빠름

# 돈가스 집이 있다고 가정
menu = ("돈가스", "치즈가스")
print(menu[0])
print(menu[1])

menu.add("생선가스")    # 튜플은 값 추가 불가

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)