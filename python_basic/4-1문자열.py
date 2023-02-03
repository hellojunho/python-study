# ### 문자열 ###

sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고, 
파이썬은 쉬워요
"""
print(sentence3)

jumin_num = "990120-1234567"

print("성별: " + jumin_num[7])
print("연: " + jumin_num[0:2])  # 0 부터 2 직전까지
print("월: " + jumin_num[2:4])  # 2 부터 4 직전까지
print("일: " + jumin_num[4:6])  # 4 부터 6 직전까지

print("생년월일: " + jumin_num[0:6])
#print("생년월일: " + jumin_num[:6])    #처음부터 6 직전까지

print("뒤 7자리: " + jumin_num[7:14])
#print("뒤 7자리: " + jumin_num[7:])    # 7 부터 끝까지

print("뒤 7자리 (뒤에부터): " + jumin_num[-7:])     # 맨 뒤에서 7번째부터 까지
# 인덱스가 뒤부터 시작할 때는 0이 아니고 -1부터 시작하여 -1, -2, -3 ...  순이다