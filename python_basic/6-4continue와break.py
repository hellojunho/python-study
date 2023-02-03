### continue and break ###

# 학교 수업 예시
absent = [2, 5]     # 결석한 학생
no_book = [7]       # 책을 안가져온 학생

for student in range(1, 11):    # 1 ~ 10
    if(student in absent):
        continue

    elif(student in no_book):
        print("오늘 수업은 여기까지. {0}는 교무실로 따라와.".format(student))
        break

    print("{0}, 책을 읽어봐.".format(student))