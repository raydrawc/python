# %% [markdown]
# 函数定义时,默认参数一定放在非默认参数后面
# True, 不然报错
def foo(x, y='def', z) :
    print(x,y,z)

# %% [markdown]
# 函数调用时,关键字参数一定要放在位置参数的后面
# true
def bar(x, y, z) :
    print(x, y, z)
bar(1,z=2,3)


# %% [markdown]
# 下列代码是否会报错,输出何值
# 不报错
# ("a", "b", "c")
# "d"
# {"name":"Sarah", "age":18}
def func(x, *y, **z) :
    print(x)
    print(y)
    print(z)

ls = ["a", "b", "c"] 
d = {"name":"Sarah", "age":18}
func(*ls, "d", **d) # = fun("a", "b", "c", 'd', **d)
# 解得
# fun(x = "a", *y = ("b",'c','d'), **z = {})

# 正确:
# a
# ('b', 'c', 'd')
# {"name":"Sarah", "age":18}

# %% [markdown]
import random


def get_inputs():  
    # 输入原始数据
    while True :
        prob_A = eval(input("请输入运动员A的每球获胜概率(0~1)："))
        if prob_A > 0 and prob_A < 1 :
            break
        print("输入错误,请重新输入")
    prob_B = round(1-prob_A, 2)
    number_of_games = eval(input("请输入模拟的场次（正整数）："))
    print("模拟比赛总次数：", number_of_games)
    print("A 选手每球获胜概率：", prob_A)
    print("B 选手每球获胜概率：", prob_B)
    return prob_A, prob_B, number_of_games


def game_over(score_A, score_B):
    # 单场模拟结束条件，一方先达到21分，比赛结束    

    return (score_A >= 21 or score_B >= 21) and abs(score_A - score_B) >= 2


def sim_one_game(prob_A, prob_B):
    # 模拟一场比赛的结果
    win_A, win_B = 0, 0
    while win_A < 2 and win_B < 2 :
        score_A, score_B = 0, 0
        while not game_over(score_A, score_B):
            if random.random() < prob_A:                # random.random() 生产[0,1)之间的随机小数,均匀分布
                score_A += 1                 
            else:
                score_B += 1

        if score_A > score_B:
            win_A += 1
        else:
            win_B += 1
    return win_A, win_B


def sim_n_games(prob_A, prob_B, number_of_games):
    # 模拟多场比赛的结果
    win_A, win_B = 0, 0                # 初始化A、B获胜的场次
    for i in range(number_of_games):   # 迭代number_of_games次
        score_A, score_B = sim_one_game(prob_A, prob_B)  # 获得模拟依次比赛的比分
        if score_A > score_B:
            win_A += 1
        else:
            win_B += 1
    return win_A, win_B


def print_summary(win_A, win_B, number_of_games):
    # 结果汇总输出
    print("共模拟了{}场比赛".format(number_of_games))
    print("\033[31m选手A获胜{0}场，占比{1:.1%}".format(win_A, win_A/number_of_games))
    print("选手B获胜{0}场，占比{1:.1%}".format(win_B, win_B/number_of_games))
    

def main():
    # 主要逻辑
    prob_A, prob_B, number_of_games = get_inputs()                        # 获取原始数据
    win_A, win_B = sim_n_games(prob_A, prob_B, number_of_games)           # 获取模拟结果
    print_summary(win_A, win_B, number_of_games)                          # 结果汇总输出


if __name__ == "__main__":
    main()

# %%
s = "八百标兵奔北坡,\
    北坡八百炮兵炮.\
    标兵怕碰炮兵跑,\
    炮兵怕把标兵碰."
sums = {}
for i in s :
    sums[i] = sums.get(i, 0) + 1
print(sums)

print(sorted(sums.items(), key= lambda item: item[1], revese=True))