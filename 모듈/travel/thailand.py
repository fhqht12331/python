class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 (야시장 투어) 50만원")
    
if __name__ == "__main__": # if __name__ == 구문을 이용하여 모듈 내부에서 직접 실행 가능
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail
else:
    print("Thailand 외부에서 모듈 호출")
# if __name__ == 구문을 이용하면 모듈 내외 실행을 구분 가능