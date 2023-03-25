n = int(input())

if n % 2 == 0:
  sum = (1 + n) * (n // 2)
elif n % 2 == 1:
  sum = (1 + n) * (n // 2) + (n // 2 + 1)
  
print(sum)