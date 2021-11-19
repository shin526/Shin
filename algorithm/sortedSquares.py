#!/usr/bin/python
# 给一个按 非递减顺序 排序的整数数组 nums，返回每个数字的平方组成的新数组，要求也按 非递减顺序 排序


def sortedSquares(nums: list) -> list:
    '''暴力解法'''
    nums = [x * x for x in nums]
    nums.sort()
    return nums


def sortedSquares2(nums: list) -> list:
    '''双指针法'''
    i, j, k = 0, len(nums) - 1, len(nums) - 1
    res = [-1] * len(nums)
    while i <= j:
        left = nums[i] * nums[i]
        right = nums[j] * nums[j]
        if left < right:
            res[k] = right
            j -= 1
        else:
            res[k] = left
            i += 1
        k -= 1
    return res


def main():
    nums = [-7, -3, 2, 3, 4, 11]
    print(sortedSquares(nums))
    print(sortedSquares2(nums))


if __name__ == '__main__':
    main()
