import sys
sys.setrecursionlimit(10**8)    #재귀한도

def preorder(in_start, in_end, post_start, post_end):
    if in_start>in_end or post_start>post_end:
        return

    parent = postorder[post_end]
    print(parent, end = ' ')

    left = pos[parent] - in_start   #왼쪽 인자 개수
    right = in_end - pos[parent]    #오른쪽 인자 개수
    preorder(in_start, in_start + left - 1, post_start, post_start + left - 1)
    preorder(in_end-right + 1, in_end, post_end - right, post_end - 1)

n = int(input())    #정점 개수
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
#inorder나 postorder 순회 결과 하나만 보고 트리를 결정짓는다면 여러 개의 트리가 나온다
#inorder와 postorder 둘 다 활용해서 겹치는 애 찾으면 됨

#후위 순회의 끝 값(부모)이 중위 순회의 어디 인덱스에 위치한지 확인을 위해 중위 순회의 값들의 인덱스값을 저장
pos = [0]*(n+1)
for i in range(n):
    pos[inorder[i]] = i

preorder(0, n-1, 0, n-1)