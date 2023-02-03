###  자료구조의 변경 ###
# 커피숍
menu = {"커피", "우유", "주스"}     # 집합으로 표현
print(menu, type(menu))     # 'set'형으로 되어있다고 출력

menu = list(menu)           # 리스트로 변환
print(menu, type(menu))     # 'list'형으로 되어있다고 출력

menu = tuple(menu)          # 튜플로 변환
print(menu, type(menu))     # 'tuple'형으로 되어있다고 출력

menu = set(menu)            # 집합으로 변환
print(menu, type(menu))