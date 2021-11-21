#!/usr/bin/python
# 螺旋矩阵，给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。


def generateMatrix(n: int):
    matrix = [[0] * n for _ in range(n)]
    left, right, up, down = 0, n - 1, 0, n - 1
    num = 1  # 待填充的数字

    while left < right and up < down:

        # 从左到右
        for x in range(left, right):
            matrix[up][x] = num
            num += 1

        # 从上到下
        for y in range(up, down):
            matrix[y][right] = num
            num += 1

        # 从右到左
        for x in range(right, left, -1):
            matrix[down][x] = num
            num += 1

        # 从下到上
        for y in range(down, up, -1):
            matrix[y][left] = num
            num += 1

        # 收缩边界
        left += 1
        right -= 1
        up += 1
        down -= 1

    # n为奇数时中间另外填充
    if n % 2 == 1:
        mid = n // 2
        matrix[mid][mid] = n**2

    return matrix


def main():
    res = generateMatrix(4)
    for i in range(len(res)):
        print(res[i])


if __name__ == '__main__':
    main()
