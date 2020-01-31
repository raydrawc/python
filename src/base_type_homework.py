# %%
# 1 输出结果为  
# 6 400
x = 20
y = 7 
print(x % y,x ** 2)

# %%
# 2 输出结果为  
# 2.5 2 
# 2 3 x 正确为 (2, 3)
x = 15 
y = 6
print(x/y, x//y)
print(divmod(x,y))


# %%
# 3. 输出结果为: 3.14 3
x = 3.1415926
print(round(x,2), round(x))

# %%
# 操作题
s = "python is a good language"

print(s[:6])
print(s[:-18])

print(s[0].upper() + s[1:])
print(s.count("o"))
print(s.replace("python", "c++"))
s1 = s.split(' ')
print(s1)
print("*".join(s1))

# %%
# 进制转换 
# bin 二进制 oct 八进制 hex 十六进制  
# int(x, 原进制)
val = 255
print(bin(val), int(bin(val), 2))
print(oct(val), int(oct(val), 8))
print(hex(val), int(hex(val), 16))

# %%
# 判断以下输出结果 True or False
a = 10
b = 5
c = "6"
d = "nine"
e = "peppa pig123"

# %% 
# False
(a > 10) and (b < 8)

# %% 
# True
(a > 10) or (b < 8)

# %% 
# 判断继承类型 false
isinstance(a, float)

# %%
# 是否全是数字 true
c.isdigit()

# %%
# 是否全是字符 true
d.isalpha()

# %% 
# 是否数字与字母混合存在 true
d.isalnum()

# %%
