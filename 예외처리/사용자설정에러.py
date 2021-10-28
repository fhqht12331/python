class BigNumberError(Exception): # 에러 코드를 사용자 임의로 생성
    def __init__(self, msg): # 에러 메세지 생성
        self.msg = msg

    def __str__(self): # 에러 메세지 반환
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >=10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # 의도적으로 제한하여 해당 에러를 생성, 에러 메세지 내용
    print("{0} / {1} = {2}". format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally: # try 문이 정상 실행이건 실행이 되지않던 무조건 실행되는 구문
    print("계산기를 이용해 주셔서 감사합니다.")