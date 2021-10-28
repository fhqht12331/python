# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file)) # with 문을 탈출하며 자동으로 종료 -> close()로 닫아줄 필요가 없음

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read()) 

# 파일을 저장하거나 읽어 들일 때 close 를 할 필요가 없게끔 함.