# %% [markdown]
# 序列类型: 内部元素有位置关系,能通过位置序号方问其中的元素
# 列表是一个可以使用多种类型元素,可以增删改查操作的序列类型
# 表示方式可以用[] 或者使用list(可迭代对象)
ls = [1, "python", ("good", 2), [3, ("yy", 33)], {"qwe": "world"}]

print(list("hello world"))
print(list(ls)) # 列表转列表
print(tuple(ls)) # 元组转列表
print(list(tuple(ls))) # 元组转列表
print(list({"a", "a", "b", "c"})) # 集合转列表


# %%
# 特殊遍历序列 range(start_num, end_num, step) 类似erlang 中 seq
# 单参数可以直接使用, 多参数需要配合list等使用
print(range(10))
print(list(range(1,5,3)))
print(tuple(range(1,5,2)))
print(list(range(0,5,1)))
print(list(range(-1,-30,1)))
print(list(range(-1,-30,-1)))

# %%
# range 应该等价与  
start = 1 
end = 8
step = 2
tmp = []
while (step > 0 and start < end ) or (step < 0 and start > end) :
    tmp.append(start)
    start += step

print(tmp)

# %% [markdown]
# 列表的特有方法
# 尾部添加待元素,返回None,在源列表中插入
l = ["python", "c++", "R"]
print(l.append("C"))
print(l)
l.append(["OC", "Csci"])
print(l)

# %%
# insert 在相应下标前插入待插入元素
l.insert(2, "B")
print(l)

# %%
# extend 在列表尾部插入另一个列表
l.extend(["g", "p"])
print(l)
# 等价与 List1 + List2

# %%
# pop(删除位置:-1) 默认删除最后一个,并返回删除内容
print(l.pop(-1))

# del l[-1]

# %%
# remove("删除目标元素") 删除第一个出现的目标元素
l.remove("B")
print(l)
# 删除所有"c:
while "C" in l :
    l.remove("C")

# %%
# index 查找目标函数的
l = ["python", "c++", "R"]
print(l.index("python"))
print(l.index("R"))

# %%
# 修改方式:先索引后赋值
print(l)
l[1] = "ObjectC"
print(l)

# %%
# 切片赋值
# list[切片开始index, 结束index] 从开始index插入一组元素,到结束index进行替换
l = ["python", "c++", "R"]
print(l)
l[1:1] = ["s+", "p++"]
print(l)
l[2:3] = ["t+", "o++"]
print(l)
ls = [1,2,3,4,5]
print(ls)
ls[1:2] = [9,8]
print(ls)
ls[1:2] = []
print(ls)
ls[1:2] = (1,2)
print(ls)
ls[1:2] = {"o":"p"}
ls[1:3] = {"1", "2"} # 乱序
print(ls)

# %%
# 复制列表
l = ["python", "c++", "R"]
print(l)
lc1 = l ## 错误,等同取别名
lc2 = l.copy() ## 复制副本, 浅拷贝
lc3 = l[:] ## 全部切片复制
l.pop()
l[1:1] = "is good"
print(l)
print(lc1)
print(lc2)
print(lc3)

# %% [markdown]
# sort排序(永久排序) sorded(临时排序)返回列表
lst = [5,13,1,6,4] 
print(lst)
print(sorted(lst)) # 可以用于任何序列,返回列表
print(sorted(lst, reverse = True)) ## 倒叙
print(sorted(tuple(lst)))
print(lst)
lst = [5,13,1,6,4]
lst.sort()
print(lst)
lst.sort(reverse = True) ## 倒叙
print(lst)

# %%
# resvse 列表反转
lst = [5,13,1,6,4] 
print(lst)
print(lst[::-1]) # 切片法
lst.reverse() # 永久反转,对自身列表处理
print(lst)

# %%
# 元组:一个可以表示多种数据类型,一旦内部元素定义,内部元素不支持增删改  
# 可视为不可变列表
# 可以用作映射中的键
print((40 + 2) == 42) # 数据表达式
print((40, 2)) # 元组内要有逗号
print(type((40,2)))
print(type((40 + 2)))
print(type((40)))

# %%
# 打包解包
num = [2001, 2002, 2003]
name = ["red", "blue", "pink"]
num1 = [20012, 20023, 20034]
print(zip(name, num, num1))
_zip = list(zip(name, num, num1))
print(_zip)
# 每次取一个元组解包赋值
for na, nu, nu1  in zip(name, num, num1) :
    print(na, nu, nu1)
# 解包数据对不上则报错
for na, nu in zip(name, num, num1) :
    print(na, nu, nu1)

#%% 
# 元组的切片还是元组
tup = (1, 4, 9, 3, 8)
print(tup[2:4])
print(tup[::-1])
print(type(tup[1:2]))

# %% [markdown]
# * 映射数据类型:通过键值对映射实现数据存储喝查找的
# * 常规的字典是无需的
# * 字典里的键不能重复,否则以最后出现的为准
# * 字典的键必须为不可变类型,键值可变找不到对应的值
# * 可用键类型:数字,字符串,元组
# * 不可用键类型: 列表,字典,集合
stud = {2001 : "ming", 2002:"red", 2003: "bule", 2002:"orange"}
print(stud)
print(len(stud)) # 打印字典长度
a = 2001
b = "ban"
c = (1,2)
# 键不变
fromlist = [(a, "red"), (b, "blue"), (c, "green")]
# 可通过dict函数生成字典映射
stud2 = dict(fromlist)
print(stud2)
print(stud2[b]) # 通过字典的键获取内容
b=2004
print(stud2)
# print(stud2[b])

# %%
# 新增映射:更新赋值
stud = {2001 : "ming", 2003: "bule", 2002:"orange"}
print(stud)
print(stud[2001])
stud[2001] = "green"
print(stud)
print(stud[2001])
stud[2004] = "new_slot"
print(stud)
print(stud[2004])
# 删除键值对 del
del stud[2001]
print(stud)
# print(stud[2001])
print(stud.pop(2004)) # 删除并获取值
print(stud)
print(stud.popitem()) # (随机,因为字典没有顺序)删除一组键值对,并返回键值对信息

print(2004 in stud) # 检查成员变量(key)
print(2003 in stud)

# %%
# 获取键值信息
s = "牛奶奶找刘奶奶买牛奶"
d = {}
# 统计字符出现次数
for i in s :
    # get(index, default)
    d[i] = d.get(i,0) + 1 
print(d)

# %%
stud = {2001 : "ming", 2003: "bule", 2002:"orange"}
print(stud.keys()) ## 取出所有key
print(list(stud.keys())) ## 取出所有key
print(stud.values()) ## 取出所有value
print(stud.items()) ## 取出所有数据

# %%
# 字典数据库
people = {
    'Alice' : {
        'phone' : '2341'
        ,'addr' : "Foo drive 23"
    }
    , 'Beth' : {
        'phone' : '9102'
        ,'addr' : 'Bar Street 42'
    }
    , 'Cecil' : {
        'phone' : '3158'
        ,'addr' : 'Baz avenue 90'
    }

}
labels = {'phone': 'phone number', 'addr': 'address'} 
name = input('name: ')

# 要查找的电话号码还是地址
request = input('phone number(p) or address (a)')

# 使用正确的键
key = request # 如果request既不是'p' 也不是'a'
if request == 'p' : key = 'phone'
if request == 'a' : key = 'adress'

# 使用get提供的默认值
person = people.get(name, {})
label = labels.get(key, key)
# label = labels.get(key) # 
result = person.get(key, 'not available')

print("{}'s {} is {}.".format(name, label, result))

# %% [markdown]
# 集合:一系列互不相等元素的`无序`集合
# 元素必须为不可变类型:数字,字符串,元组
# 可以看作是没有值,或者值为None的字典
# 底层实现与字典相同
col1 = {"red", "white", "green" }
col2 = {"blue", "pink", "green", "yellow"}
col1

# 可以计算交集等

# %%
# 交集 S & T 返回一个新集合, 包含同时出现在S和T中的元素
col1 & col2

# %%
# 并集 S | T 返回一个新集合, 包含S和T中所有元素
col1 | col2

# %%
# 非交集 S ^ T 返回一个新集合, 包含S与T中不共有元素
print(col1 ^ col2)
print((col1 | col2) - (col1 & col2))

# %%
# 非集 S - T 返回一个新集合, 包含S中非T中的元素
col1 - col2

# %%
