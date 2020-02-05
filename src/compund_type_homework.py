# %% [markdown]
# # 列表
# 生产由100以内偶数构成的列表
lst = list(range(2, 101, 2))
print(lst)

# %%
ls = ['a', 'b', 'c', 'd', 'e']
# 分别用正向索引和反向索引获得元素'c'
print(ls[2])
print(ls[-3])

# 用正向切片获得['b', 'd']
print(ls[1::2])

# 用反向切片实现ls的反向列表
print(ls[::-1])

# %% [markdown]
# 新增"CHERY"在头部
cars = ["CHERY", "BYD", "GEELY"] # 对列表cars依次执行以下列表操作:
# 在列表结尾增加元素 "TOYOTA"
cars.append("TOYOTA")
print(cars)

# 在列表结尾增加["BMW", "BENZ"]中的元素
cars.extend(["BMW", "BENZ"])
print(cars)

# 删除列表中最后一个元素和第四个元素
cars.pop()
print(cars)
cars.pop(3) # 删了后面执行不了
print(cars)

# 删除元素 "Geely"
cars.remove("GEELY")
print(cars)

# 查找元素"BMW"在列表中的位置索引
print(cars.index("BMW"))

# 将元素"CHERY"修改为"QQ"
if "CHERY" in cars :
    cars[cars.index("CHERY")] = "QQ"
print(cars)

# 用两种方法进行复制
cars1 = cars.copy()
cars2 = cars[:]
print(cars1)
print(cars2)

# 对列表分布进行永久排序和临时排序
cars3 = sorted(cars)
print(cars3)
cars.sort()
print(cars)

# 对列表反转
cars.reverse()
print(cars)

# 对列表进行遍历, 并按下格式进行输出 
# My first car is BYD
for i in cars:
    print("My first car is {}".format(i))

# %% [markdown]
# 元组为什么被称为"不可变列表"
# * 除了内部数据不可变外,其他操作基本与列表一致

foods = ["bread", "fish", "pototo"]
prices = [2.4, 9.8, 0.9]
# 按照以下格式输出:
# The price of bread is 2.4
for food, price in zip(foods, prices) :
    print("The price of {} is {}".format(food, price))

# %% [markdown]
# # 字典
# 判断以下字典定义是否合法,如果不合法,指明原因
# A:{(1,2):3} B:{[1,2]:3} C: {"price":2.4} D:{1:"first"}
# B:键值不可为可变类型:列表

# %% [markdown]
favorite_fruits = {"Judy" : 'watermelon', "Jen": "banana", "Sarah": 'orange'}
print(favorite_fruits)

# 获取字典长度
print(len(favorite_fruits))

# 获取Jen最爱的水果名
print(favorite_fruits["Jen"])

# 增加"Tom"最爱的水果"peach", "Bob" 最爱的水果 "tomato"
favorite_fruits["Tom"] =  "peach"
favorite_fruits["Bob"] =  "tomato"
print(favorite_fruits)

# 删除"Judy"及其最爱的水果名
del favorite_fruits["Judy"]
print(favorite_fruits)

# 随机删除一个键值对,并捕获被删除的值 
print(favorite_fruits.popitem())
print(favorite_fruits)

# 将"Sarah" 的最爱修改为"watermelon
favorite_fruits["Sarah"] = "watermelon"

# 遍历字典 favorite_fruits, 并按下列格式进行输出
# Sarah' favorite fruit is watermelon
for name, favorite in favorite_fruits.items() :
    print("{} favorite fruit is {}".format(name, favorite))

# 统计下列绕口令中字符出现的频次:
s = "八百标兵奔北坡,\
    北坡八百炮兵炮.\
    标兵怕碰炮兵跑,\
    炮兵怕把标兵碰."
sums = {}
for i in s :
    sums[i] = sums.get(i, 0) + 1
print(sums)

# %% [markdown]
# # 集合
vegetables = {"tomato", "cabbage", "cucumber", "meat"}
fruits = {"banana", "orange", "tomato", "cucumber"}
print(vegetables)
print(fruits)
print("----------------")

# 将集合中的 vegetables 中的 "meat" 删除
vegetables.remove("meat")
print(vegetables)

# 将"eggplant" 加入到集合vegetables中
vegetables.add("eggplant")
print(vegetables)

# 两个集合中,哪些即属于蔬菜又属于水果
print(vegetables & fruits)

# 两个集合中,所有的蔬菜和水果有哪些
print(vegetables | fruits)

# 两个集合中,哪些只属于蔬菜或者只属于水果
print(vegetables ^ fruits)

# 两个集合中,哪些只属于蔬菜
print(vegetables - fruits)


# %%
