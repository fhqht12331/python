gun = 10

def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun 사용 # 전역 변수는 비권장
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun # 처음 gun 값을 받아서 함수 내에서 사용 완료 후 리턴하여 다음 gun에 연결

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("전체 총 : {0}".format(gun))