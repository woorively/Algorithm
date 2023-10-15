n = int(input())
seat = list(map(int, input()))

# 가장 가까운 두 사람의 거리를 구하는 함수
def min_dist():
    dist = n
    pos = []
    for i in range(n):
        if seat[i]:
            pos.append(i)

    for i in range(len(pos) - 1):
        dist = min(dist, pos[i + 1] - pos[i])

    return dist

ans = 0
for i in range(n):
    if not seat[i]:
        seat[i] = 1
        ans = max(ans, min_dist())
        seat[i] = 0

print(ans)