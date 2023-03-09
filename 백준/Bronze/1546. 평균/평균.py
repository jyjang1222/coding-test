subjectCount = int(input())
scores = list(map(int,input().split()))
max = max(scores)

total = 0
for score in scores:
  changedScore = score / max * 100
  total += changedScore

avg = total / subjectCount

print(avg)