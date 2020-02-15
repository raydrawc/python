# %% [markdown]
# 为什么要用函数
# * 提高代码的复用性-抽象出来,封装为函数
# * 将复杂的大问题分解为一系列的小问题,分而治之-模块化设计的思想
# * 利于代码的维护和管理

# %% [markdown]
# 函数的三要素 参数 函数体 返回值
# def function (param) :
#   函数体
#   return 返回值

# %% [markdown]
# 参数传递
# 形参:(形式参数) 函数定义时的参数,实际上是变量名
# 实参:(实际参数) 函数调用时的参数,实际上时变量的值
# * 位置参数:严格按照位置顺序,用实参对形参进行赋值
# * 关键字参数:打破位置限制,直呼其名进行传递(形参=实参)
# * * 位置参数可以与关键字参数混合使用
# * * 位置参数必须放在关键字参数前面
# * * 不能为同一个形参重复传值
# 默认参数:在定义阶段给形参赋值
# * 默认参数必须在非默认参数后面
# * 位置形参必须放在默认形参前面
# * 默认参数应该被(最好被)设置为不可变类型(数字,元组,字符串)
# * 让参数变成可选
def test(x, y, z) :
    print(x, y, z)

test(1, 2, 3)
test(1, 3, z= 2)

# %% [markdown]
# 位置参数 可变长参数 *args
# * 不知道传过来多少参数
# * 该形参必须放在参数列表最后
# * 原子类型直接赋值,组合类型转义为元组赋值
# * 可以通过*来解包 组合类型(列表,元组,字符串)转义为元组
def foo(x, y, *args) :
    print(x, y)
    print(args)

foo(1,2,3,4,5,6)
foo(1,2,[3,4,5,6])
foo(1,2,*[3,4,5,6])
foo(1,2,(3,4,5,6))
foo(1,2,*(3,4,5,6))
foo(1,2,{3,4,5,6})
foo(1,2, *{3,4,5,6})
foo(1,2,"hello")
foo(1,2, *"hello")
# %% [markdown]
# * 实参位置可变
# 关键字参数 可变长参数 **kwargs
# 通过** 进行打散
def foo1(x, y, **kwargs) :
    print(x, y)
    print(kwargs)

foo1(1,2, a=2, c=3, z=1)
foo1(1,2, **{"t":1,"z":2,"g":3})


# %% [markdown]
# 变量
# * 局部变量:仅在函数体内定义和发挥作用
# * 全局变量:外部定义的都是全局变量
# 全局变量可以在函数体内直接使用  
# 通过global在函数体内定义全局变量

# %% [markdown]
# 返回值
# 单个返回值:原样返回
# 多值返回值:以元组形式返回
# 多个return:其中一个执行则返回/函数结束
# 没有return:返回值None

# %% [markdown]
# 建议
# * 函数及其参数命名参数变量的命名
# * 应该包含简要阐述函数功能的注释,注释紧跟函数定义后面
# * 函数定义前后各空两行

# %% [markdown]
# 函数式编程
# * 模块化编程思想
# * * 自顶而下,分而治之
