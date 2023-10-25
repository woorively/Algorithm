n = int(input())
nums = list(map(int, input().split()))

nums.sort()
abs_lst = []
for i in range(n):
    abs_lst.append(abs(nums[i + n] - nums[i]))

print(min(abs_lst))

# 2 5 7 9 10 15
