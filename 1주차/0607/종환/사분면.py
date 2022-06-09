"""
문제: 사분면을 또 사분면으로 나눠서 이전 사분면의 몇 사분면인지를 자릿수로 나타내려 한다
(4사분면의 3사분면은 43, 3사분면의 1사분면의 2사분면은 312 ... ).
주어진 사분면이 오른쪽으로, 위쪽으로 몇 칸 이동했을 경우, 
이동한 사분면의 주소(나타내는 숫자)는 무엇일까?
          424
341->432->431  442  441  x
341에서 441까지는 4번 이동 가능
344에서 444까지도 4번 이동 가능
만약 331이었다면? 441까지 6번

오른쪽 이동 시
2->1->2->1->2 ....
4->3->4->3->4 ....

위쪽 이동 시
1->4->1->4 ...
3->2->3->2 ...

모든 자릿수가 1 또는 4라면, 더 이상 오른쪽으로 이동할 수 없음
모든 자릿수가 1 또는 2라면, 더 이상 위      로 이동할 수 없음
"""
def move_right(now, move):
    while move:
        if ('3' or '2') not in now:
            now = '-1'
            break
        else:
            # 이동 기능
            # 맨 뒷자리 (1의 자리) 부터 확인해서, 2 or 4일 경우 해당 자리만 1 or 3으로 바꾸면 되고,
            # 1 or 3일 경우 그 윗 자리 (10의 자리...) 를 확인해서, 바꾼다.
            for i in range(1, len(now)+1):
                if now[-i] == '2':
                    now[-i] = '1'
                    move -= 1
                    break
                if now[-i] == '3':
                    now[-i] = '4'
                    move -= 1
                    break
                elif now[-i] == '4':
                    now[-i] = '3'
                else:
                    now[-i] = '2'
    return now

def move_up(now, move):
    while move:
        if ('4' or '3') not in now:
            now = '-1'
            break
        else:
            # 이동 기능
            for i in range(1, len(now)+1):
                if now[-i] == '3':
                    now[-i] = '2'
                    move -= 1
                    break
                elif now[-i] == '4':
                    now[-i] = '1'
                    move -= 1
                    break
                elif now[-i] == '2':
                    now[-i] = '3'
                else:
                    now[-i] = '4'
    return now

d, now = map(str, input().split())
now = list(now)
x, y = map(int, input().split())
move_right(now, x)
move_up(now, y)
for i in now:
    print(i, end='')

# 시간 초과