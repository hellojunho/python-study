### 문자열 처리 함수 ###
python = "Python is Amazing"

print(python.lower())   # 문자열을 전부 소문자로
print(python.upper())   # 문자열을 전부 대문자로
print(python[0].isupper())  # 문자열의 0번째가 대문자인지 아닌지

print(len(python))          # 문자열 전체의 길이

print(python.replace("Python", "Java"))     # 앞의 문자열을 뒤의 문자열로 교체

index = python.index("n")
print(index)    # n의 위치 출력

index = python.index("n", index + 1)    # n을 찾은 위치 이후부터 다시 n 검색
print(index)

print(python.find("is"))    # 찾으려는 문자(열)의 첫번째 문자의 인덱스 없으면 -1반환
print(python.count("n"))    # n이 총 몇 번 등장하는지