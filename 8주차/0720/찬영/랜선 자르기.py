K, N = map(int, input().split())

lengths = []
for _ in range(K):
    lengths.append(int(input()))
    
start, end = 1, max(lengths)

while True:
    mid = (start + end) // 2
    if start > end:
        print(mid)
        break
    count = [length // mid for length in lengths]
    if sum(count) < N:
        end = mid - 1
    else:
        start = mid + 1