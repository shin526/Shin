#!/usr/bin/python
# 给定一个整数数组 nums 和一个目标值 target，在该数组中找出和为目标值的两个整数，并返回他们的数组下标。
# 假设每种输入只会对应一个答案。但是，数组中同一个元素不能重复出现。


def twoSum(nums: list, target: int):
    hashmap = dict()
    for index, val in enumerate(nums):
        if target - val in hashmap:
            return [hashmap[target - val], index]
        else:
            hashmap[val] = index
    return []


def main():
    nums = [2, 7, 11, 19]
    print(twoSum(nums, 9))


if __name__ == '__main__':
    main()
