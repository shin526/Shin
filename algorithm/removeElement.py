#!/usr/bin/python
# 原地移除所有数值等于 val 的元素，并返回移除后数组的新长度，不需要考虑超出新长度后的元素


def removeElement(nums: list, val: int):
    size = len(nums)
    k = 0
    for i in range(size):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


def main():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    print(removeElement(nums, 2))


if __name__ == '__main__':
    main()
