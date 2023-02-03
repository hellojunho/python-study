### 기본값 ###
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))
#         # 임의 줄 바꿈 시, 역슬래시(\) 후에 줄 바꿈 하면 된다.

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 수업 -> 기본값 사용
def profile(name, age = 17, main_lang = "파이썬"):
     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang))

profile("유재석")
profile("김태호")
