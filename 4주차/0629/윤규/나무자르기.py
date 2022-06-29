import sys
input = sys.stdin.readline
n, m = map(int, input().split(' '))
treelst = list(map(int, input().split(' ')))
maxtree = max(treelst) # 백만


def bi(start, end):
    while start <= end:
        l = 0
        mid = (start+end)//2
        for tree in treelst:
            if tree > mid:
                l += (tree-mid)
        
        if l >= m:
            start = mid + 1

        elif l < m:
            end = mid - 1
    return end
print(bi(1, maxtree))
