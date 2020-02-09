# %% [markdown]
# if condition :  # condition不为空则为真, None, 空, False, 0 为假
# pass 
ls = []
if ls :
    print("not empty")
else :
    print("is empty")

# %% [markdown]
# 与,或, 非
# 与
print(True and True) # 与运算
print(True and False) # 两边为真才为真
print(False or False) # 或运算
print(True or False) # 其中一边为真则为真
print(not True) # 非运算
print(not False) # 非运算

# %% [markdown]
# 复合运算的运算顺序
# () > 非 > 与 > 或
print(True or True and False)
print(False and True or True)
print((True or True) and False)

# %% [markdown]
# 每次执行一个可选分支,判断为true的是入口
# if condition :
#     pass
# elif condition : # 可选 条件 else + if
#     pass
# else : # 可选
#    pass
age = 35
if age < 10 :
    print("孩子")
elif age < 18 : 
    print("年轻人")
elif age < 30 : 
    print("中年人")
else :
    print("老人")

# %% [markdown]
# 嵌套语句
# 在逻辑逻辑块中嵌套一个逻辑块,用缩进分割

# %% [markdown]
# for 从可迭代对象中依次取出元素迭代
# * 直接迭代:元组(), 列表[], 集合{}, 字符串"""
v = ("a", "d", "b")
for i in v :
    print(v)
# * 变换迭代:字典, 转换为元组迭代对象
d = {"wo": 1, 2:"ta", (2,2):[1,23]}
for k, v in d.items() :
    print(k, v)
for k in d : # 等同与d.keys()
    print(k)
# * range(): 生成序列
for i in range(1, 101, 2) :
    print(i)

# %% [markdown]
# >拓展:列表推导
print([i * i for i in range(0,13,2) if i <6])

# %% [markdown]
# break:终止当前程序块执行 
# continue:跳过当前程序块的当前执行

# %% [markdown]
# while condition : # condition = True 则继续执行
#       pass
# else : 
#   pass

# %% [markdown]
# ## 需要注意的点
# * 避免过多嵌套
# * 避免死循环
# * 封装过于复杂的判断条件/函数