from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

def print_pre(inidx, inlist, istart, iend, postlist, pstart, pend):

    if iend-istart <1 : return

    root = postlist[pend-1]
    iroot = inidx[root]
    pmid = pstart + (iroot-istart)


    print(root, end=" ")
    print_pre(inidx, inlist, istart, iroot, postlist, pstart, pmid)
    print_pre(inidx, inlist, iroot+1, iend, postlist, pmid, pend-1)
    return


n = int(stdin.readline())
inlist = list(map(int, stdin.readline().split()))
postlist = list(map(int, stdin.readline().split()))
inidx = [0]*1000001
for i, node in enumerate(inlist):
    inidx[node] = i


print_pre(inidx, inlist, 0, len(inlist), postlist, 0, len(postlist))