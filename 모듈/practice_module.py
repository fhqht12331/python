# import theater_module # 해당 모듈 불러오기, 모듈은 같은 파이썬 라이브러리 or 같은 폴더 내에 있을 때 불러오기 가능
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv # mv 를 사용하여 해당 모듈을 간소화
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import * # from --- import * 을 사용하여 더 간소화
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning # 가져오는 모듈의 일부분만 사용 가능
# price(3)
# price_morning(4)

from theater_module import price_soldier as price # 모듈을 as 로 별칭을 정정하여 이 파일내에서 변형
price(5)