### if ###
# if 조건:
#     실행 명령문

# print("날씨를 입력하세요>> ")
# weather = input()


# if weather == "비" or "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없어요")

temp = int(input("기온을 입력하시오>> "))
if (30 <= temp):
    print("너무 더워요. 나가지 마세요")
elif (10 <= temp and temp < 30):
    print("괜찮은 날씨네요")
elif (0 <= temp and temp < 10):
    print("쌀쌀해요. 겉옷을 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")