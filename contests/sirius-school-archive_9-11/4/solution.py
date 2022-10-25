n = int(input())
l = 0
r = 10 ** 9 + 1
while r != l + 1:
    m = (l + r) // 2
    if m * m < n:
        l = m
    else:
        r = m
k = l
if n - k ** 2 <= k + 1:
    x = k + 1
    y = n - k ** 2
else:
    x = (k + 1) ** 2 - n + 1
    y = k + 1
if k % 2 == 0:
    print(x, y)
else:
    print(y, x)
