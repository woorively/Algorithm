A, B, x, y = tuple(map(int, input().split()))

# a -> x -> y -> b
# a -> y -> x -> b
# a -> b

ans = min(abs(A - x) + abs(B - y), abs(A - y) + abs(B - x), abs(A - B))
print(ans)