# <方針>
# x and y = a ⏩ aを2進数表記した時の、1となる桁は、x, yを2進数表記した場合に、同じ桁は1となる。 ⏩ x, yの値は必ずa以上になる。
# x + y = s ⏩  a + x` + a + y` = s ⏩  x` + y` = s - 2aとなる。
# またx` + y`の各桁に関して、x xor yが成り立つ。(2進数の各桁が1, 1の場合に0になっている必要があるため。)
# よって、x xor y = s - 2aが成り立つ。(a = x and y)
# s - 2aをs`とした場合、s` < 0は`No`となる。
# x and y, x xor yが成り立つx, yの条件を考える。 ⏩ x, yの各桁が0, 0 0, 1, 1, 0の場合は、問題ないが、1, 1の場合に成り立つと困る。 aをandして条件として組み込む必要がある。
# 参考動画 : https://www.youtube.com/watch?v=Ckuo6w6s_ko

# 標準入力を受け付ける。
T = int(input())

for _ in range(T):
    a, s = map(int, input().split())

    if (s - 2 * a) >= 0 and (s - 2 * a) & a == 0:
        print('Yes')
    else:
        print('No')

