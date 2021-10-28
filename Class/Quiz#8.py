class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print("{0}년에 완공된 {1}{2}의 {3} 비용은 {4} 입니다."\
            .format(self.completion_year, self.location, self.house_type, self.deal_type, self.price))

houses = []
House1 = House("강남", "아파트", "매매", "10억", 2010)
House2 = House("마포", "오피스텔", "전세", "5억", 2007)
House3 = House("송파", "빌라", "월세", "500/50", 2000)

houses.append(House1)
houses.append(House2)
houses.append(House3)

print("총 {0}개의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()