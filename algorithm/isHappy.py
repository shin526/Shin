#!/usr/bin/python
# 判断一个数 n 是不是快乐数:对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
# 然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果 可以变为 1，那么这个数就是快乐数


def isHappy(n: int):
    '''
    def getSum(n):
        sum = 0
        while n:
            sum += (n % 10)**2
            n = n // 10
        return sum
    '''

    table = set()
    # 当出现重复时会陷入无限循环，即不是快乐数
    while True:
        # n = getSum(n)
        n = sum([int(x)**2 for x in str(n)])
        if n == 1:
            return True
        if n in table:
            return False
        else:
            table.add(n)


def main():
    print(isHappy(1090))


if __name__ == '__main__':
    main()
