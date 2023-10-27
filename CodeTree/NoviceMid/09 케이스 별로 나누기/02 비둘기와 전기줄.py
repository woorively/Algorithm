n = int(input())
p = [-1] * 11
ans = 0

for i in range(n):
    c, d = tuple(map(int, input().split()))
    if p[c] >= 0 and p[c] != d:
        ans += 1
    p[c] = d

print(ans)
