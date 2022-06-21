# #pypy input() 썼을 때 1044ms sys.stdin.readline() 썼을 때 820ms
# #python input() 썼을 때 시간초과 sys.stdin.readline() 썼을 때 1332ms
import sys
n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
for a in sorted(arr):
    print(a)

# #병합정렬 pypy readline() 시간 초과
# import sys

# def divide(lst):    #길이가 1이 될 때까지 나눈다
#     if len(lst)<2:
#         return lst
#     mid = len(lst)//2
#     left = lst[:mid]
#     right = lst[mid:]
#     divide(left)    
#     divide(right)   
#     return merge(divide(left), divide(right))

# def merge(left, right):
#     merged = []
#     left_idx = 0
#     right_idx = 0
#     while True:
#         if left_idx >= len(left):
#             merged += right[right_idx:]
#             break
#         elif right_idx >= len(right):
#             merged += left[left_idx:]
#             break
#         elif left[left_idx] < right[right_idx]:
#             merged.append(left[left_idx])
#             left_idx += 1
#         elif left[left_idx] > right[right_idx]:
#             merged.append(right[right_idx])
#             right_idx += 1
#     return merged

# n = int(sys.stdin.readline())
# arr = [int(sys.stdin.readline()) for _ in range(n)]
# result = divide(arr)
# for r in result:
#     print(r)

# #heapq 사용. python input() 시간초과 readline() 2152ms
# import heapq
# import sys
# n = int(sys.stdin.readline())
# arr = [int(sys.stdin.readline()) for _ in range(n)]
# heapq.heapify(arr)
# while arr:
#     print(heapq.heappop(arr))

