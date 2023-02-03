### 파일 입출력 ###
# "w": write 쓰기
score_file = open("score.txt", "w", encoding = "utf8")  # encoding = "utf8" : 한글정보 꺠지지 않게 해줌
print("수학: 0", file = score_file)
print("영어: 50", file = score_file)
score_file.close()

# "a": append 추가하기
score_file = open("score.txt", "a", encoding="utf8")    # "a": append -> 추가하기
score_file.write("\n과학: 80")      # append 기능은 줄바꿈 하여 작성되지 않아 앞에 \n으로 줄바꿈 명시
score_file.write("\n코딩: 100")
score_file.close()

# "r": read 읽기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

# 한 줄씩 읽기
score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")    # 줄별로 읽기 수행, 한 줄 읽고 다음 줄로 커서 이동
# print(score_file.readline(), end="") 
# print(score_file.readline(), end="") 
# print(score_file.readline(), end="") 

while(True):
    line = score_file.readline()
    if(not line):
        break
    print(line, end="")
score_file.close()

# 리스트에 값을 넣어 처리
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # 모든 값을 가져와 list형태로 저장
for line in lines:
    print(line, end="")
score_file.close()