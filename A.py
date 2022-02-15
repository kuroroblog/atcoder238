# 標準入力を受け付ける。
n = int(input())

# pow関数とは? : https://himibrog.com/python-pow/
if pow(2, n) > pow(n, 2):
    print('Yes')
else:
    print('No')
