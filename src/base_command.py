# %% [markdown] 
# # 数据类型  
# 列表属于__类型,元组属于__类型,字典属于__类型  
# 
# A:序列 B:映射  
# > 列表与元组都属于序列类型,可以通过下标方问,字典属于映射类型,kv形式访问  

# %% [markdown] 
# 集合内元素是否可以重复  
# A 可以 B 不可以
# > 不可以,集合内元素不重复切无序

# %% [markdown] 
# # 变量
# 判断一下变量法命名是否合法,如不合法,请说明理由
# A: _boy B:4stundent C:class D:first number
# 
# > A合法  
# > B 首位不可以为数字
# > c python保留字
# > d 变量中间不可以带有空格

# %% [markdown] 
# 请将1,2,3,4,5 打包赋值给变量 a,b,c,d,e
a,b,c,d,e = 1,2,3,4,5
print(a,b,c,d,e)

# %% [markdown] 
# ## 请分别用下划线命令方式和驼峰体命名方式命名一个变量
first_name = 1
print(first_name)
secondName = 2
SecondName = 3
print(secondName, SecondName)

# %% [markdown]
# # 控制语句
# 分别简述for循环,while循环 和if分支语句的执行过程
# %% [markdown]
# > for 元素 in 可迭代对象:  
# >
# > 可执行语句
# 
# 执行过程: 从可迭代对象中,依次取出来执行,相应处理
for i in [1,2,3,6,5] :
    print("i:", i + 1)

# %% [markdown]
# > while [条件语句] :  
# > 可执行语句  
# 执行过程: 从

# %% [markdown]
# # 输入输出
# 用input语句分别输入两个数字,并实现两个数字的相乘


# %% [markdown]
# 用format分别实现黄金分割比值 0.6180339887保留前3位的浮点数输出已经保留1位小数的百分比输出