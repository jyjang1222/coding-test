h, m = map(int, input().split())

total = h * 60 + m

if total - 45 < 0:
    total += 24 * 60

total -= 45

print(total // 60, total % 60)