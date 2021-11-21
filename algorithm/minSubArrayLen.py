#!/usr/bin/python
# 给定一个含有n个正整数的数组和一个正整数target，找出该数组中满足其和≥target的长度最小的连续子数组，并返回其长度。
# 如果不存在符合条件的子数组，返回0


def minSubArrayLen(target: int, nums: list):
    '''暴力解法'''
    res = float('inf')  # 无穷大
    sum = 0
    # subArrayLen = 0  # 子数组长度
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum >= target:
                # subArrayLen = j - i + 1
                res = min(res, (j - i + 1))
                break

    if res == float('inf'):
        return 0
    else:
        return res


def minSubArrayLen2(target: int, nums: list):
    '''滑动窗口'''
    res = float('inf')
    sum = 0
    i = 0  # 滑动窗口起始位置
    for j in range(len(nums)):
        sum += nums[j]
        # 每次更新起始位置并判断子数组是否符合条件
        while sum >= target:
            res = min(res, (j - i + 1))
            sum -= nums[i]
            i += 1

    return 0 if res == float('inf') else res


def main():
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    print(minSubArrayLen(target, nums))
    print(minSubArrayLen2(target, nums))


if __name__ == '__main__':
    main()
