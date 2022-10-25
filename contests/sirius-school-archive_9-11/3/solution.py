n = int(input())
a = [0] * (n + 1)
for i in range(1, n + 1):
    j = int(input())
    a[j] = n + 1 - i
for i in range(1, n + 1):
    print(a[i])


