def logit(func) :
    print('i am logit')
    def wrapper() :
        print('i am wrapper')
        func()

    return wrapper

@logit # @xxx = fun = xxx(fun)
def foo():
    print("i am foo")

# print("test2")
# foo = logit(foo)
print("test1")
foo()



