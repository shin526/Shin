#! /usr/bin/python
# 排序算法


def bubbleSort(nums: list) -> list:
    # 冒泡
    k = len(nums) - 1
    pos = 0
    for _ in range(len(nums) - 1):
        swap = False
        for j in range(k):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swap = True
                pos = j
        k = pos
        if not swap:
            break
    return nums


def selectionSort(nums: list) -> list:
    # 选择
    for i in range(len(nums)):
        min = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min]:
                j = min
        nums[i], nums[min] = nums[min], nums[i]
    return nums


def insertionSort(nums: list) -> list:
    # 插入
    for i in range(1, len(nums)):
        j = i - 1
        tmp = nums[i]
        while j >= 0 and nums[j] > tmp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = tmp
    return nums


def binaryInsertionSort(nums: list) -> list:
    # 折半插入
    for i in range(1, len(nums)):
        left = 0
        right = i - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[i]:
                right -= 1
            else:
                left += 1
        tmp = nums[i]
        for j in range(i, right + 1, -1):
            nums[j] = nums[j - 1]
        nums[right + 1] = tmp
    return nums


def mergeSort(nums: list) -> list:
    # 归并
    def merge(left, right):
        res = []
        i = 0
        j = 0
        le = len(left)
        r = len(right)
        while i < le and j < r:
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        while i < le:
            res.append(left[i])
            i += 1
        while j < r:
            res.append(right[j])
            j += 1
        return res

    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    return merge(mergeSort(left), mergeSort(right))


def main():
    nums = [5864, -12333, 4151, -6239, -10306, 10866, -7013, 13195, -8855, 1150, -560]
    print(bubbleSort(nums))
    print(selectionSort(nums))
    print(insertionSort(nums))
    print(binaryInsertionSort(nums))
    print(mergeSort(nums))


if __name__ == '__main__':
    main()
