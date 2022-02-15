# 標準入力を受け付ける。
N = int(input())

# Nの桁数を保存する。
NLen = len(str(N))

ans = 0
DIVIDE_VALUE = 998244353

# 数字Nの各桁ごとに処理を行う。
for i in range(NLen):
    # current_digit : 処理を行う現在の桁
    current_digit = i + 1
    # 処理を行う、現在の桁の中での下限の数字
    # 1桁の場合1, 2桁の場合10, 3桁の場合100, ...
    bottom_num = 10 ** (current_digit - 1)

    # 処理を行う、現在の桁が数字Nの桁と等しい場合
    if current_digit == NLen:
        # 桁の上限の数字 + 1
        top_num = N + 1
    else:
        # 桁の上限の数字 + 1
        # 1桁の場合10, 2桁の場合100, 3桁の場合1000, ...
        top_num = (10 ** current_digit)

    middle = (top_num - bottom_num) // 2

    # 桁の個数を数える。
    ans += (top_num - bottom_num + 1) * middle

    # 奇数の場合、真ん中の桁も数える。
    if (top_num - bottom_num) % 2 == 1:
        ans += middle + 1

    ans %= DIVIDE_VALUE

print(ans)
