# 数字类型

# %% 
a = bin(25) # 二进制 0b
b = oct(25) # 八进制 0o
c = hex(25) # 十六进制 ox
print(a, b, c)

# %%
# 浮点数通常带有不确定小数,所以需要round(x,n)来取精度  
print(0.1 + 0.2)
print(0.4 + 0.2)
print(round(0.4 + 0.2, 2))

# %% [markdown]
# 虚数表示方式: a + bj (pow(j,2) = -1 )  
a = 1 + 2j
print(pow(a, 2))

# %% [markdown]
# 数字类型简单操作  
# 
# | 类型 | 含义 |
# | --- | --- |
# | + - * / | 加减乘除 |
# | - | 取反 |
# | ** | 乘方 |
# | //  % | 求整数商 求余数 | 

print(2 ** 3)
x,y = 14,5
print(x // y, x % y)


# %%
# 操作函数
#
# | 类型 | 含义 |
# | --- | --- |
# | abs(x) | 绝对值 | 
# | pow(x,n) | 幂次方 |
# | pow(x,n,m) | x幂n次方m余数 |
# | round(x,n) | 四舍五入(python中) |
# | divmod(x,y) | 整除商模(返回二元组(x//y, x%y),更快捷)
# | max(x),min(x) | 最大最小 |
# | sum(x) | 求和 |

# round py3.x中取靠近偶数的
print(round(0.5))
print(round(1.5))

divmod(13, 5)

print(max(1, 2, 3, 4, 5))
print(min([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5]))

# %% 
# 使用第三方库 math/scipy/numpy
import math 
import numpy as np
import scipy

math.sqrt(4)

np.std([1, 2, 3, 4, 5])

# %% 
# 字符串: 由"/'括起来的字符  
# `\`转义符 或者 行尾换行链接符 
print("hello world")
print("hello 'world'")
print('hello "world"')

# %%
# 序列运算
# * 索引
# * * 正向索引,从0开始索引至n-1,反向索引,从-1开始到-n
# * 切片
# * * [start:end:step] 
# * * 切片开始索引与结束索引成对
# * * 切片步长不可为0,可为负数,自右向左遍历

val = "hello world"
print(val[6])
print(val[-3])
print(val[1:10:2])
print(val[1:-1:2])
print(val[10:1:-1])
print(val[-1:-10:-1])
print(val[-1:-10:0])

# %%
# 序列相加 
# 可以拼接序列类型(列表,元组,字符串),通常不可以拼接不同类型的序列
lst = [1, 2, 3, 4, 5]
tup = (1, 2, 3, 4, 5)
string = "hello world"
print(lst + [6, 7])
print(tup + (6, 9))
print(string + " is good")
print(lst + tup)

# %%
# 序列相乘
# 重复相同序列n次来形成新的序列   
# * 空列表 复制还是空
# * 表示还没添加任何东西初始化可以使用None

string = "hello world"
val1 = []
val2 = [None]
print(string * 3)
print(val1 * 3)
print(val2 * 3)

# %%
# 成员资格检查 in
# 一个序列是否一个全集的子集(一个连续切片是该全集的一个子集)
# for in
str1 = "hello world"
print("o w" in str1)
print("po" in str1)

for i in str1 :
    print(i)

# %% [markdown]
# 常见的字符串/序列类型处理函数
# 
# | 函数 | 意义 | 
# | --- | --- | 
# | len(s) | 返回序列长度 |
# | max(s) | 序列中最大 |
# | min(s) | 序列最小 | 


# %%
# 常用字符串处理
# str.split(sep=None, maxspilt=-1) : 处理分割目标字符串,返回一个新列表,原字符串不变
# 分割符也被去掉
word = "hello world"
print(word)
print(word.split())
print(word.split(' '))
print(word.split('o'))
print(word.split('o',1))

# %%
