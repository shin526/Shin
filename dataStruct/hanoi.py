#! /usr/bin/python

i = 1


def hanoi(num: int, A, B, C):
    global i
    if num == 1:
        print(f'第 {i} 步：{num} 号从 {A} 移动至 {B}')
        i += 1
    else:
        hanoi(num - 1, A, C, B)
        print(f'第 {i} 步：{num} 号从 {A} 移动至 {B}')
        i += 1
        hanoi(num - 1, C, B, A)


def main():
    hanoi(4, 'A', 'B', 'C')


if __name__ == '__main__':
    main()
