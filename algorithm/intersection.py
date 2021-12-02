#!/usr/bin/python
# 给定两个数组,编写一个函数来计算它们的交集,输出结果中的每个元素一定是唯一的,可以不考虑输出结果的顺序


def intersection(nums1: list, nums2: list):
    return list(set(nums1).intersection(set(nums2)))


def main():
    nums1 = [4, 9, 5]
    nums2 = [9, 8, 3, 4, 4]
    print(intersection(nums1, nums2))


if __name__ == '__main__':
    main()
