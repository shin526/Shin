#! /usr/bin/python


class Seqlist:
    __slots__ = ('size', 'length', 'data')

    def __init__(self, size=10) -> None:
        self.size = size
        self.length = 0
        self.data = [None] * size

    def display(self):
        for i in range(0, self.length):
            print(f'{self.data[i]} ', end="")
        print("")

    def isEmpty(self):
        return self.length == 0

    def isFull(self):
        return self.length == self.size

    def clear(self):
        self.__init__()

    def insert(self, index: int, data: int):
        '''指定位置插入元素，从1开始'''
        if self.isFull():
            print("顺序表已满，无法插入")
            return
        if index < 1 or index > self.length + 1:
            print("插入位置超出范围")
            return

        for i in range(self.length, index - 1, -1):
            self.data[i] = self.data[i - 1]
        self.data[index - 1] = data
        self.length += 1

    def append(self, data: int):
        '''尾部添加元素'''
        if self.isFull():
            print("顺序表已满，无法插入")
            return
        self.data[self.length] = data
        self.length += 1

    def delete(self, index: int):
        '''删除指定位置元素，从1开始'''
        if self.isEmpty():
            print("顺序表为空")
            return
        if index < 1 or index > self.length:
            print("位置错误")
            return

        for i in range(index - 1, self.length):
            self.data[i] = self.data[i + 1]
        self.length -= 1

    def find(self, data: int):
        '''查找元素位置'''
        for i in range(self.length):
            if self.data[i] == data:
                return i + 1
        return -1  # 元素不存在返回-1

    def index(self, index: int):
        '''查找指定位置元素'''
        if index < 1 or index > self.length:
            return None
        return self.data[index - 1]

    def update(self, index: int, data: int):
        '''修改指定位置元素'''
        if index < 1 or index > self.length:
            print("位置错误")
            return
        self.data[index - 1] = data

    def reverse(self):
        '''反转'''
        i, j = 0, self.length - 1
        while i < j:
            self.data[i], self.data[j] = self.data[j], self.data[i]
            i += 1
            j -= 1


def reverseSeqlist(list: Seqlist):
    '''反转顺序表，不改变原表，返回反转后的新表'''
    newList = Seqlist(list.size)
    for i in range(list.length):
        newList.data[i] = list.data[list.length - i - 1]
        newList.length += 1
    return newList


def mergeSeqlist(l1: Seqlist, l2: Seqlist):
    '''合并两个有序顺序表，不改变原表，返回新表'''
    newList = Seqlist(l1.size + l2.size)
    i, j = 0, 0
    while (i < l1.length and j < l2.length):
        if l1.data[i] <= l2.data[j]:
            newList.append(l1.data[i])
            i += 1
        else:
            newList.append(l2.data[j])
            j += 1

    while i < l1.length:
        newList.append(l1.data[i])
        i += 1
    while j < l2.length:
        newList.append(l2.data[j])
        j += 1

    return newList


def main():
    l1 = Seqlist(5)
    l2 = Seqlist(5)
    l1.append(1)
    l1.append(3)
    l1.append(3)
    l2.append(2)
    l2.append(4)
    l2.append(6)
    l2.append(8)
    l2.append(10)
    l3 = mergeSeqlist(l1, l2)
    l3.display()


if __name__ == '__main__':
    main()
