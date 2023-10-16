n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

cnt = 0
avg = sum(arr) // n

for elem in arr:
    cnt += abs(elem - avg)

print(cnt // 2)