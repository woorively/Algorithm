n = int(input())
nums = list(map(int, input().split()))
rev_nums = nums[::-1]

idx_num = 0
for i in range(n - 1):
    if rev_nums[i] < rev_nums[i + 1] and idx_num < rev_nums[i + 1]:
        idx_num = rev_nums[i + 1]
        # print(rev_nums[i + 1])
        break

if idx_num:
    print(nums.index(idx_num) + 1)
else:
    print(0)
