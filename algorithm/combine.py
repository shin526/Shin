#! /usr/bin/python
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合


def combine(n: int, k: int):
    res = []
    path = []

    def backtrack(n, k, start):
        if len(path) == k:
            res.append(path[:])

            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(n, k, i + 1)
            path.pop()

    backtrack(n, k, 1)
    return res


def main():
    print(combine(4, 2))


if __name__ == '__main__':
    main()
