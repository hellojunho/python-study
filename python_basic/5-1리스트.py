### 리스트 [] ###

# 지하철 칸 별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

from operator import sub


subway = [10, 20, 30]
print(subway[0], subway[1], subway[2])

subway = ["유재석", "조세호", "박명수"]
# 조세호가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하가 다음 정류장에서 승차함
subway.append("하하")   # .append() : 리스트 맨 뒤에 추가
print(subway)

# 정형돈이 유재석과 조세호 사이에 탐
subway.insert(1, "정형돈")     # .insert() : 리스트 요소 사이에 추가
print(subway)

# 지하철에 타고 있는 사람 뒤에서 부터 꺼냄
print(subway.pop())     # .pop() : 맨 뒤의 요소부터 꺼냄
print(subway)
subway.pop()
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬
num_list = [5,2,4,3,1]
num_list.sort()     # .sort() 작은 수 부터 순서대로 정렬
print(num_list)

# 순서 뒤집기
num_list.reverse()  # .reverse() 역순으로 정렬
print(num_list)

# 모두 지우기
num_list.clear()    # .clear() 리스트의 요소 모두 지우기
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]     # 리스트의 요소는 자료형에 구애받지 않음
print(mix_list)

# 리스트 확장   
num_list.extend(mix_list)   # .extend(list) 하나의 리스트로 합침
print(num_list)
