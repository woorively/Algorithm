n = int(input())
seats = list(map(int, input()))
pos = []
pos_loc = []
pos_max = []

for i in range(n):
    if seats[i]:
        pos.append(i)

for i in range(len(pos) - 1):
    x, y = pos[i], pos[i + 1]
    pos_loc.append((x, y))
    pos_max.append(y - x)

a, b = pos_loc[pos_max.index(max(pos_max))]
mid = int((a + b) / 2)
seats[mid] = 1

ans = 1000
cnt = 1
for elem in seats[1::]:
    if elem:
        ans = min(ans, cnt)
        cnt = 1
        continue
    cnt += 1

print(ans)