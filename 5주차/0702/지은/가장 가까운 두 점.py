#분할 정복 사용
import sys

n = int(sys.stdin.readline())
sorted_location = []
for _ in range(n):
    x, y = list(map(int, sys.stdin.readline().split()))
    sorted_location.append((x, y))
sorted_location.sort()

def get_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def solution(l, r):
    if l == r:  #점 하나만 있을 때는 거리를 계산할 수 없다
        return float('inf')
    else:
        #중앙을 기준으로 왼,오른쪽으로 나눈 영역에서의 최솟값과 중앙값을 걸쳐서 생성된 영역에서의 최솟값 중 최솟값 반환
        m = (l + r) // 2
        min_dist = min(solution(l, m), solution(m + 1, r))
        target_list = []
        
        #m의 x좌표와의 거리가 min_dist 미만인 점들을 후보로 넣어줌
        for i in range(m, l - 1, -1):
            if (sorted_location[i][0] - sorted_location[m][0]) ** 2 < min_dist:
                target_list.append(sorted_location[i])
            else:
                break

        for j in range(m + 1, r + 1):
            if (sorted_location[j][0] - sorted_location[m][0]) ** 2 < min_dist:
                target_list.append(sorted_location[j])
            else:
                break
                
        #후보점들을 y좌표 기준으로 정렬
        #x좌표는 비슷한 점들을 모았으니 y좌표가 가까운 점들을 비교했을 때 최솟값을 구할 수 있기 때문
        target_list.sort(key=lambda x: x[1])
        for i in range(len(target_list) - 1):
            for j in range(i + 1, len(target_list)):
                if (target_list[i][1] - target_list[j][1]) ** 2 < min_dist:
                    dist = get_dist(target_list[i], target_list[j])
                    min_dist = min(min_dist, dist)
                else:   #y좌표로 정렬되어있어 이후의 값은 지금의 y 좌표와 크거나 같기 때문
                    break
        return(min_dist)

if len(sorted_location) != len(set(sorted_location)):
    print(0)
else:
    print((solution(0, len(sorted_location) - 1)))