import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

# https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FCgtFd%2Fbtq3IQAzXrd%2Fk6xGNan4Q3lwNeD58gZ7ik%2Fimg.png


def pre(si, ei, sp, ep):
    if si > ei or sp > ep:
        return

    parent = postorder[ep]
    preorder.append(parent)
    l = index[parent] - si
    r = ei - index[parent]

    pre(si, si + l - 1, sp, sp + l - 1)
    pre(ei - r + 1, ei, ep - r, ep - 1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
preorder = []
index = [0] * (n + 1)

for i in range(n):
    index[inorder[i]] = i

pre(0, n - 1, 0, n - 1)
print(*preorder)
