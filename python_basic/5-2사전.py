### 사전 ###
# key는 중복 불가

cabinet = {3:"유재석", 100:"김태호"}    # 사전의 경우는 중괄호{}로 표현
                                       # 유재석의 key 값 : 3, 김태호의 key 값 : 100
# print(cabinet[3])   # 대괄호[]에 key 값을 넣어줌
# print(cabinet[100])

# print(cabinet.get(3))

# ##print(cabinet[5])
# print(cabinet.get(5, "사용 가능"))   # .get(key, str) 사용 시, key 값이 없는 값이면 None 혹은 str 반환
# print("hi")

# print(3 in cabinet)     # 있으면 True
# print(5 in cabinet)     # 없으면 False

cabinet2 = {"A-3":"유재석", "B-3":"김태호"}
print(cabinet2["A-3"])
print(cabinet2["B-3"])

# 새 손님
print(cabinet2)

cabinet2["C-20"] = "조세호"     # C-20 에 해당하는 값 업데이트
print(cabinet2)

cabinet2["A-3"] = "김종국"      # 기존 key 값의 정보 교체 가능
print(cabinet2)

# 간 손님
del cabinet2["A-3"]             # key 값에 해당하는 정보 삭제
print(cabinet2)

# key 값들만 출력
print(cabinet2.keys())

# value 들만 출력
print(cabinet2.values())

# key:value 쌍으로 출력
print(cabinet2.items())

# 목욕탕 폐점
cabinet2.clear()
print(cabinet2)