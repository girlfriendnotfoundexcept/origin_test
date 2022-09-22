"""
Project: Project
Creator: huminghuan
Create time: 2021-10-11 14:41
IDE: PyCharm
Introduction:
"""



def qishui(m):
    # **********Program**********
    n = m
    s = 0
    # 瓶数大于2
    while n >= 2:
        # 拿两个空瓶换1瓶汽水
        n = n - 2
        # 增加1个空瓶
        n += 1
        # 瓶子换的汽水 增加1个
        s += 1
    return m + s
    # **********  End  **********


def main():
    print("【请分别三次计算问题：】")
    for n in range(1):
        print("【第%d次：】" % (n + 1))
        m = int(input("【请输入钱数m（正整数）：】"))
        s = qishui(m)
        print("【钱数为", m, "元,最多可以喝】", s, "【瓶汽水】")


if __name__ == '__main__':
    main()

