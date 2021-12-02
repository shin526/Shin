#!/usr/bin/python
# 给定四个包含整数的数组列表 A,B,C,D,计算有多少个元组(i,j,k,l)，使得A[i] + B[j] + C[k] + D[l] = 0。
# 例如：输入: A = [1, 2] B = [-2,-1] C = [-1, 2] D = [0, 2] 输出: 2
# (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

from typing import Counter


def fourSumCount(A: list, B: list, C: list, D: list):
    # hashmap = dict()
    # for a in A:
    #     for b in B:
    #         if a + b in hashmap:
    #             hashmap[a + b] += 1
    #         else:
    #             hashmap[a + b] = 1

    # count = 0
    # for c in C:
    #     for d in D:
    #         if -c - d in hashmap:
    #             count += hashmap[-c - d]
    # return count

    hashmap = Counter(a + b for a in A for b in B)
    return sum(hashmap.get(-c - d, 0) for c in C for d in D)


def main():
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(fourSumCount(A, B, C, D))


if __name__ == '__main__':
    main()
