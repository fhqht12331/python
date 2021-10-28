import pickle 
# 프로그램상 데이터를 파일형태로 저장 -> 파일을 데이터로 변환 가능하게 만듬

# profile_file = open("profile.pickle", "wb") # "wb" -> write, binary 피클을 쓰기 위해서는 binary 타입 정의가 필요
# 인코딩 설정 따로 필요하지 않음
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정포를 file에 저장
# profile_file.close() # 피클로 파일형태로 저장

# profile_file = open("profile.pickle", "rb") # 파일 가져오기, 읽기 -> "rb" 사용
# profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기
# print(profile)
# profile_file.close()