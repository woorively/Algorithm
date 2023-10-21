n = int(input())
grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

max_coin = 0
for row in range(n):
    for col in range(n):
        if row + 2 >= n or col + 2 >= n:
            continue

        cnt = 0
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if grid[i][j] == 1:
                    cnt += 1

        max_coin = max(max_coin, cnt)

print(max_coin)
