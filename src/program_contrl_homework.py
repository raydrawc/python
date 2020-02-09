# %% [markdown]
# 以下条件测试的结果是
# %%
# 条件判断假: None 0/0.0 False 空字典{} 空元组() 空列表[] 空字符串"" ''
# 空的
d = {}
# d = 0.0
if d:
    print("非空")
else:
    print("空的")

# %% [markdown]
# 判断优先级 () > not > and > or
# True
True or False and False
True or (False and False)

# %% [markdown]
# in 判断是否是子元素
# False
# True
foods = ["bread", "fish", "potato"]
"breads" in foods
"tomato" not in foods

# %% [markdown]
# 编写一个程序,实现一个功能
# 从黑箱摸到一个球, 按球的颜色不同颜色分配奖金
# * 黑球 =  0 元
# * 白球 = 10 元
# * 蓝球 = 20 元
# * 粉球 = 30 元
# * 紫球 = 50 元
# * 彩球 = 100 元
color = input("摸到球的颜色")
if color == "black":
    val = 0
elif color == "white":
    val = 10
elif color == "blue":
    val = 20
elif color == "pink":
    val = 30
elif color == "purple" :
    val = 100
else:
    val = -1
    print("不是已定义颜色")
if val != -1 :
    print(val)

# %% [markdown]
# 用两层for嵌套打印99乘法表
# for i in range(1, 10):
#     for j in range(1, 10):
#         print("{:0>2d}".format(i * j), end=" ")
#     print()
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{} x {} = {}".format(i, j, i * j), end=" ")
    print()

# %%
# 创建一个while循环,通过input,动态数据如高三二班学生学号性名和性别
# * 以学号为键值,姓名和性别为值,将学神信息存储在字典students_of_grade3_class2中
# * 当通过input输入字母"Q"或者"q"时, 程序结束,
# * 层序结束后,对学所信息进行遍历输出

students_of_grade3_class2 = {}
s = ["学号", "姓名", "性别"]
l = []
i = 0
while True :
    val = input(s[i])
    # if val == "Q" or val == "q":
    #     break
    if val in ["q", "Q"] :
        break
    l.append(val)
    if len(s) == len(l) : 
        students_of_grade3_class2[l[0]] = (l[1], l[2])
        l = []
        continue
    i = len(l)

for num,(name, sex) in students_of_grade3_class2.items() :
    print("学号为:{} 姓名:{} 性别:{}".format(num, name, sex))

# %% [markdown]
# 以下层序能否正常执行,如果不能,请说明原因
# i = 0
# while i <= 5 :
#     print(i)
# 不能,会无限循环打印,没有退出条件

# 为什么我们不希望嵌套层数过多
# 可读性差,维护复杂

# 如果条件测试过于复杂,通常会如何处理
# 简化判断,或者把判断封装成函数

