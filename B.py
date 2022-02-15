# 標準入力を受け付ける。
N = int(input())

A = list(map(int, input().split()))

# ピザの切れ込みを入れた角度一覧
slice_list = [0, 360]
# 最後にピザに切れ込みを入れた角度を記録する。
last_slice_angle = 0
for i in range(len(A)):
    # ピザの切れ込みを入れる角度へ移動する。
    last_slice_angle += A[i]
    # 一回転することを考慮する。
    if last_slice_angle > 360:
        last_slice_angle -= 360

    slice_list.append(last_slice_angle)

slice_list.sort()

ans = 0
for i in range(1, len(slice_list)):
    ans = max(ans, slice_list[i] - slice_list[i - 1])

print(ans)


