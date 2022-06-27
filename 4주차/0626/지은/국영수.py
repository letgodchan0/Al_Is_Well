import sys

n = int(sys.stdin.readline())
scores = []

for _ in range(n):
    tmp1 = sys.stdin.readline().split()
    tmp2 = list(map(int, tmp1[1:]))
    scores.append((tmp1[0], *tmp2))
answer = sorted(scores, key=lambda x:(-x[1], x[2], -x[3], x[0]))

for ans in answer:
    print(ans[0])