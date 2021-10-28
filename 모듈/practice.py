# 패키지 : 모듈의 집합, 하나의 디렉토리에 여러 모듈을 모아 놓은 것
# from travel import *
# trip_to = vietnam.VietnamPackage() # __init__ 파일에 __all__ =["---"] 형태로 제공할 파일을 열어둠.
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(travel))