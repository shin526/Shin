#!/usr/bin/python
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d，
# 使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。


def fourSum(nums: list, target: int):
    nums.sort()
    n = len(nums)
    res = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            p = j + 1
            q = n - 1
            while p < q:
                if nums[i] + nums[j] + nums[p] + nums[q] > target:
                    q -= 1
                elif nums[i] + nums[j] + nums[p] + nums[q] < target:
                    p += 1
                else:
                    res.append([nums[i], nums[j], nums[p], nums[q]])
                    p += 1
                    q -= 1
                    while p < q and nums[p] == nums[p - 1]:
                        p += 1
                    while p < q and nums[q] == nums[q + 1]:
                        q -= 1

    return res


def main():
    nums = [1, 0, -1, 0, -2, 2]  # target = 0
    nums = [1000000000, 1000000000, 1000000000, 1000000000]  # target = 0
    nums = [2, 2, 2, 2, 2]
    print(fourSum(nums, 8))


if __name__ == '__main__':
    main()
