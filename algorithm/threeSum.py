#!/usr/bin/python
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c
# 使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组


def threeSum(nums: list):
    res = []
    n = len(nums)
    nums.sort()
    for i in range(n):
        if nums[i] > 0:
            return res
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = n - 1

        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum > 0:
                k -= 1
            elif sum < 0:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
    return res


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))


if __name__ == '__main__':
    main()
