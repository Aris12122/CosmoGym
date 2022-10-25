n = int(input())
a = [int(input()) for i in range(n)]
ans = [0] * n
s = 0
for i in range(n - 1):
    if a[i] > a[0] and a[i] + s > a[i + 1]:
        ans[i] = 1
    else:
        ans[i] = 0
    s += a[i]
if a[n - 1] > a[0]:
    ans[n - 1] = 1
else:
    ans[n - 1] = 0
i = n - 1
while ans[i] == 1:
    i -= 1
while i >= 0:
    ans[i] = 0
    i -= 1
if n == 1:
    ans = [1]
for i in range(n):
    print(ans[i])
