n = int(input())
nums = list(map(int, input().split()))

# 짝, 홀, 짝, 홀
# 짝수 = 홀수+홀수 혹은 짝수
# 홀수 = 짝수+홀수 혹은 홀수

odd, even = 0, 0
for num in nums:
    if num % 2:
        odd += 1
    else:
        even += 1

ans = 0
while True:
    if ans % 2 == 0:
        if even:
            even -= 1
            ans += 1
        elif odd >= 2:
            odd -= 2
            ans += 1
        else:
            if even > 0 or odd > 0:
                ans -= 1
            break

    else:
        if odd:
            odd -= 1
            ans += 1
        else:
            # ans -= 1
            break
        
print(ans)