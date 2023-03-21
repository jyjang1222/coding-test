chess = [1, 1, 2, 2, 2, 8]
answer = [0 for _ in range(6)]
piece = list(map(int, input().split()))

for i in range(len(piece)):
  answer[i] = chess[i] - piece[i]

for i in answer:
  print(i, end=" ")