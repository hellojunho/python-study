## 한 줄 for문 ###

# 출석번호가 1, 2, 3, 4 -> 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1,2,3,4,5]
print(students)

students = [i+100 for i in students]    # 리스트의 값(i)를 불러와 i+100을 하여 리스트에 저장해라
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "groot"]
students = [i.upper() for i in students]
print(students)