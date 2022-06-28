import sys
input = sys.stdin.readline


def find(i, j, a):
    global r, c, ans

    for (di, dj) in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ni, nj = di + i, dj + j
        if 0 <= ni < r and 0 <= nj < c and not used[ord(arr[ni][nj]) - 65]:
            used[ord(arr[ni][nj]) - 65] = 1
            find(ni, nj, a + 1)
            used[ord(arr[ni][nj]) - 65] = 0

    if a > ans:
        ans = a


r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
ans = 1

used = [0] * 26
used[ord(arr[0][0]) - 65] = 1

find(0, 0, 1)
print(ans)
