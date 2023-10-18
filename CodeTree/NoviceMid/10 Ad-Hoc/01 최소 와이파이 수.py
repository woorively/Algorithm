n, m = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

ans = 0
i = 0
while n:
    if nums[i]:
        ans += 1
        i += m * 2 + 1
    else:
        i += 1
    if n <= i:
        break

print(ans)
