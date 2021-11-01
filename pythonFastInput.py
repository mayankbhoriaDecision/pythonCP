
[n, q] = map(int, input().split())
a = list(map(int, input().split()))
while q > 0:
    q -= 1
    i = int(input()) - 1
    ans = -2
    for j in range(i + 1, n):
        if a[i] < a[j] and sum(map(int, str(a[i]))) > sum(map(int, str(a[j]))):
            ans = j
            break
    print(ans + 1)
