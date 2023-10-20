n = int(input())
nums_info = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
arr = [0] * 101
ans = 100

for i in range(n):
    temp = nums_info.pop(i)
    for j in range(n):
        for elem in nums_info:
            x1, x2 = elem
            for k in range(x1, x2 + 1):
                arr[k] = k

    for e in arr:
        if e:
            min_arr = e
            break 

    ans = min(max(arr) - min_arr, ans)
    arr = [0] * 101
    nums_info.insert(i, temp)

print(ans)
