#!/usr/bin/python
# 逆波兰表达式求值,有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式
# 整数除法只保留整数部分,给定逆波兰表达式总是有效的


def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token not in {'+', '-', '*', '/'}:
            stack.append(int(token))
        else:
            num2, num1 = stack.pop(), stack.pop()
            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(num1 * num2)
            else:
                stack.append(int(num1 / num2))  # 题目要求除法保留整数，// 是向下取整，负数时会出错
    return stack.pop()


def main():
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(evalRPN(tokens))


if __name__ == '__main__':
    main()
