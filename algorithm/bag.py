#! /usr/bin/python
# 背包问题


def bag1(weights, values, bag):
    dp = [[0 for _ in range(bag + 1)] for _ in range(len(weights))]
    for j in range(weights[0], bag + 1):
        dp[0][j] = values[0]
    for i in range(1, len(weights)):
        for j in range(1, bag + 1):
            if j < weights[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i])
    # return dp[-1][-1]
    print(dp)


def main():
    weights = [1, 3, 4]
    values = [15, 20, 30]
    bag = 4
    # print(backpag(weights, values, bag))
    bag1(weights, values, bag)


if __name__ == '__main__':
    main()
