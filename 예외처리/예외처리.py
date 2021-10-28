try: # 정상 실행
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError: # 에러 타입을 예외로 두고 예외의 에러 발생시 아래의 경우를 출력
    print("숫자를 입력해 주세요.")
except ZeroDivisionError as err: # 에러 문장 그대로 출력
    print(err)
except Exception as err: # 설정한 예외가 아닌 모든 에러에 대하여 출력
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)