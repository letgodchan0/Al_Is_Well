#시작 a 경유 b 목적 c
#n-1개의 원반을 a에서 c를 거쳐 b로 이동시킨다.
#맨 아래 있던 원반을 a에서 c로 이동시킨다
#b로 이동시켰던 n-1개의 원반을 b에서 a를 거쳐 c로 이동시킨다
def move(frm, to, mid, n, answer):
    if n == 1:  # 시작지 -> 목적지를 answer에 리스트로 저장한다
        answer.append([frm, to])
        return
    move(frm, mid, to, n - 1, answer)   #1
    answer.append([frm, to])            #2
    move(mid, to, frm, n - 1, answer)   #3

def solution(n):
    answer = []
    move(1, 3, 2, n, answer)
    return answer

print(solution(2))