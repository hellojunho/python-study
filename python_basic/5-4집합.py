### 세트(집합) ###
# 중복 불가, 순서 없음
my_set = {1, 2, 3, 3, 3}    
print(my_set)       # {1, 2, 3}만 출력됨

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 출력 (java, python 모두 가능한 사람)
print(java & python)
print(java.intersection(python))

# 합집합 출력
print(java | python)
print(java.union(python))

# 차집합 출력
print(java - python)
print(java.difference(python))

# python 개발자가 늘어남
python.add("김태호")
print(python)

# java를 까먹음
java.remove("김태호")
print(java)