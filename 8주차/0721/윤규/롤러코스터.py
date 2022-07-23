

r, c = map(int, input().split(' '))
arr = [list(map(int, input().split(' '))) for _ in range(r)]
check = 0
answer = ''




def roll(r, c, answer):
    if not (r % 2) and not (c % 2):
        m = 1000
        position = [-1, -1]
        for i in range(r):
            if i % 2:
                for j in range(0, c, 2):
                    if m > arr[i][j]:
                        m = arr[i][j]
                        position = [i, j]
            else:
                for j in range(1, c, 2):
                    if m > arr[i][j]:
                        m = arr[i][j]
                        position = [i, j]


        answer = 'D' * (r-1) + 'R' + 'U' * (r-1) + 'R'
        answer *= position[1]//2
        x = 2 * (position[1] // 2)
        y = 0
        xbound = 2 * (position[1] // 2) + 1

        while x != xbound or y != r - 1:
            if x < xbound and [y, xbound] != position:
                x += 1
                answer += 'R'
            elif x == xbound and [y, xbound - 1] != position:
                x -= 1
                answer += 'L'
            if y != r - 1:
                y += 1
                answer += 'D'

        answer += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - position[1] - 1) // 2)
        return answer

    # 하나라도 홀수 라면
    else:
        check = 0
        if (r == 1) or (c==1):
            if r == 1:
                answer = 'R' * (c-1)
            elif c == 1:
                answer = 'D' * (r-1)
            return answer
        elif r % 2:
            for i in range(r-1):
                for j in range(c-1):
                    if check == 0:
                        answer += 'R'
                    elif check == 1:
                        answer += 'L'
                if check == 0:
                    check = 1
                elif check == 1:
                    check = 0
                answer += 'D'
            for j in range(c-1):
                answer += 'R'
            return answer
        elif c % 2:
            for i in range(c-1):
                for j in range(r-1):
                    if check == 0:
                        answer += 'D'
                    elif check == 1:
                        answer += 'U'
                if check == 0:
                    check = 1
                elif check == 1:
                    check = 0
                answer += 'R'
            for j in range(r-1):
                answer += 'D'
            return answer


print(roll(r, c, answer))



