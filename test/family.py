class Father :
    def __init__(self):
        print('it is rain today')

    def getmoney(self, money):
        print("money is : %d" % (money))

class Mother:
    def __init__(self):
        print("we dont go out today")

    def cooking(self, food_name):
        print('today we eat %s' % food_name)


class Son(Father, Mother) :

    def __init__(self):
        super().__init__()
        super().cooking("ppp")
        Mother.__init__(self)
        print('ok, we are at home today')


dollor_food = Son()
dollor_food.cooking('egg')
dollor_food.getmoney(1234)
