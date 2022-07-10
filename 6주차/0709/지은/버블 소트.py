#버블 정렬 횟수: 요소들이 왼쪽으로 밀려난 횟수 중 가장 큰 수
#-> 수 정렬하고 기존 인덱스 값과의 차이가 가장 큰 값 출력
import sys
n = int(sys.stdin.readline())
nums = [(int(sys.stdin.readline()), idx) for idx in range(n)]
srtd = sorted(nums, key = lambda x: x[0])
arr = [srtd[i][1] - i for i in range(n)]
print(max(arr)+1)            