### for 반복문 ###
for waition_num in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waition_num))

for waition_num in [0, 1, 2, 3, 4]:
    print("대기번호 : " , waition_num)

# randrange()
for waition_num in range(5):    # 0, 1, 2, 3, 4
    print("대기번호 : {0}".format(waition_num))
    
for waition_num in range(1, 6):    # 1, 2, 3, 4, 5
    print("대기번호 : {0}".format(waition_num))

# 스타벅스
starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0} 손님, 커피가 준비되었습니다.".format(customer))