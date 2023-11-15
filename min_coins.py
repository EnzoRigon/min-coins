# Normal

import sys

coins = [9, 6, 5, 1]
m = len(coins)
V = 53


def min_coins(coins, m, V):
    if (V == 0):
        return 0

    res = sys.maxsize
    for i in range(0, m):
        if coins[i] <= V:
            sub_res = min_coins(coins, m, V-coins[i])

            if sub_res != sys.maxsize and sub_res + 1 < res:
                res = sub_res + 1
    return res


def min_coins_top_down(coins, m, V, dp):
    if V == 0:
        return 0
    if dp[V] != -1:
        return dp[V]

    res = sys.maxsize

    for i in range(m):
        if coins[i] <= V:
            sub_res = min_coins_top_down(coins, m, V - coins[i], dp)

            if sub_res != sys.maxsize and sub_res + 1 < res:
                res = sub_res + 1
    dp[V] = res
    return res


def solve_min_coins_top_down(coins, m, V):
    dp = [-1] * (V + 1)
    return min_coins_top_down(coins, m, V, dp)


def min_coins_bottom_up(coins, m, V):
    table = [0 for i in range(V + 1)]
    table[0] = 0
    for i in range(1, V + 1):
        table[i] = sys.maxsize
    for i in range(1, V + 1):         
        for j in range(m):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if sub_res != sys.maxsize and sub_res + 1 < table[i]:
                    table[i] = sub_res + 1

    if table[V] == sys.maxsize:
        return -1

    return table[V]


print(f"(Top down) Minimum coins required is {solve_min_coins_top_down(coins, m, V)}")
print(f"(Bottom up) Minimum coins required is {min_coins_bottom_up(coins, m, V)}")
print(f"(Base)Minimum coins required is {min_coins(coins, m, V)}")
