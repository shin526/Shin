#!/usr/bin/python
# 原地移除所有数值等于 val 的元素，并返回移除后数组的新长度，不需要考虑超出新长度后的元素


def removeElement(nums: list, val: int):
    size = len(nums)
    i, j = 0, 0
    while j < size:
        if nums[j] == val:
            j += 1
        else:
            nums[i] = nums[j]
            i += 1
            j += 1
    return i


def main():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    print(removeElement(nums, 2))


if __name__ == '__main__':
    main()
