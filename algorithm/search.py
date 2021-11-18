#! /usr/bin/python
# 二分查找


def search(nums: list, target: int) -> int:
    '''闭区间'''
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] < target:
            left = middle + 1
        elif nums[middle] > target:
            right = middle - 1
        else:
            return middle
    return -1


def main():
    nums = [5, 6, 9, 15, 18, 30, 45, 60, 78, 90]
    print(search(nums, 18))


if __name__ == '__main__':
    main()
