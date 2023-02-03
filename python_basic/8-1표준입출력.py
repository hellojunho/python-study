 ## 표준 입출력 ###
print("Python", "Java", sep = ",")  # sep = "(문자)" 로 문자열 사이 구분 가능
print("Python", "Java", sep = " vs ")
print("Python", "Java", sep = ",", end = "?")   # end = "(문자)"로 다음 print와 연결
                                                # -> 해당 print문의 끝 부분을 (문자)로 바꿈
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file = sys.stdout)
print("Python", "Java", file = sys.stderr)

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():   # key:value 쌍으로
    #print(subject, score)
    print(subject.ljust(2), str(score).rjust(4), sep = ":")  # .ljust(2) : 4개의 공간을 만들고 왼쪽부터 정렬
                                                  # .rjust(4) : 4개의 공간을 만들고 오른쪽부터 정렬

# 은행 대기 순번표
# 001, 002, 003, ...
for num in range(1,21):     # 1 ~ 20
    print("대기번호 : " + str(num).zfill(3))    # .zfill(3) : 3만큼의 공간을 확보하고, 값이 없는 공간은 0으로 채움

answer = input("아무 값이나 입력하세요 : ")     # input() : str형으로 입력 받음
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")