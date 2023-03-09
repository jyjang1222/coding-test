A = int(input())
B = int(input())
C = int(input())

res = A * B * C
strRes = str(res)
nums = [0 for _ in range(10)]

for num in strRes:
    nums[int(num)] += 1

for num in nums:
    print(num)