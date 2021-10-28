# print("Python", "Java", sep=",", end="?") # sep : 문자열을 구분, end : 프린트 끝 부분 처리 및 두 문장 한 줄로 연결
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout) # 표준 출력으로
# print("Python", "Java", file=sys.stderr) # 표준 에러로

# scores = {"수학":0, "영어": 50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, socres)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")
#     # ljust() : ()칸의 공간확보 후 왼쪽 정렬, rjust() : ()칸의 공간확보 후 오른쪽 정렬

# 대기 순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3)) # zfill() : ()자리수의 빈공간을 0으로 처리

answer = input("아무 값이나 입력하세요 : ") 
# input() : 사용자 입력, 사용자 입력 사용시 문자열(int) 형태로 저장, 숫자형태 출력 필요시 str() 사용
print(type(answer))
print("입력하신 값은 " + answer +"입니다.")