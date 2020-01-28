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
# 执行过程: 如果条件语句为真,则继续执行,否则停止
i = 0
while i < 5 :
    print("i:", i)
    i += 1

# %% [markdown]
# > if [条件语句] :  
# > 可执行语句  
# > else [条件语句] :  
# > 可执行语句  
# 执行过程: 如果条件语句为真,则执行,否则(执行else)/停止
a = 10
if a < 10 :
    print("true")
else :
    print("false")

# %% [markdown]
# # 输入输出
# 用input语句分别输入两个数字,并实现两个数字的相乘  
# input函数输入的为 `字符串`  
# int(x [,base ])         将x转换为一个整数    
# long(x [,base ])        将x转换为一个长整数    
# float(x )               将x转换到一个浮点数    
# complex(real [,imag ])  创建一个复数    
# str(x )                 将对象 x 转换为字符串    
# repr(x )                将对象 x 转换为表达式字符串    
# eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象    
# tuple(s )               将序列 s 转换为一个元组    
# list(s )                将序列 s 转换为一个列表    
# chr(x )                 将一个整数转换为一个字符    
# unichr(x )              将一个整数转换为Unicode字符    
# ord(x )                 将一个字符转换为它的整数值    
# hex(x )                 将一个整数转换为一个十六进制字符串    
# oct(x )                 将一个整数转换为一个八进制字符串   

x = input("x:")
y = input("y:")
print("x * y = ",eval(x) + eval(y))

# %% [markdown]
# 用format分别实现黄金分割比值 0.6180339887保留前3位的浮点数输出已经保留1位小数的百分比输出
# > "[字符串1:修饰符]:{0},[字符串2]:{1}".format(v1,v2)
val = 0.6180339887
print("{0:.3f}".format(val))
print("{0:.1f}".format(val))

# %% [markdown]
# 将以下x处代码补全,并如图实现格式化输出
# for i in [0, 1, 2, 3, 4, 5]:
#     print("x1".format("x2" * (2*i + 1)))

for i in [0, 1, 2, 3, 4, 5]:
    print("{0:_^20}".format("*"*(2*i + 1))) 

# %% [markdown]
# 以下格式是否复合PEP8的格式建议,不符合,请予以修改
# * x*=10
# * * 执行符号两边带空格
# * * x *= 10
# * y = (3-1)/8
# * * 
# * * y = (3-1) / 8
# * t = (1,2,3,4,5)
# * * 列表带空格 
# * * t = (1, 2, 3, 4, 5) 
# * x =          10
# * * 不要无谓的空格
# * * x = 10
# * def fun(x = 1,y = 2):
# * * 参数两边不要空格
# * *  def fun(x=1,y=2):
# * if m >3:
# * print("m大于3")
# * * 内容函数加制表符
# * * if m > 3:
# * *   print("m大于3")

# %%
