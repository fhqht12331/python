# def profile(name, age, mail_lang):
#     print("이름 : {0}\t나이 : {1}\t언어 : {2}"\
#         .format(name, age, mail_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은반 같은 수업.

def profile(name, age=25, mail_lang="인도네시아어"):
     print("이름 : {0}\t나이 : {1}\t언어 : {2}"\
         .format(name, age, mail_lang))

profile("김정호")
# profile("김태호")