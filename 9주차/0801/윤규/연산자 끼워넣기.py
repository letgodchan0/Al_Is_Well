


n = int(input())
numbers = list(map(int, input().split(' ')))
cals = list(map(int, input().split(' ')))
maxV = -100000000000000
minV = 100000000000000


def cal(i, s):
    global maxV, minV
    if i == n-1:
        maxV = max(maxV, s)
        minV = min(minV, s)
        return
    else:
        if cals[0] > 0:
            cals[0] -= 1
            cal(i+1, s + numbers[i+1])
            cals[0] += 1

        if cals[1] > 0:
            cals[1] -= 1
            cal(i+1, s - numbers[i+1])
            cals[1] += 1

        if cals[2] > 0:
            cals[2] -= 1
            cal(i+1, s * numbers[i+1])
            cals[2] += 1

        if cals[3] > 0:
            cals[3] -= 1
            if s >= 0:
                cal(i+1, s // numbers[i+1])
                cals[3] += 1
            else:
                cal(i+1, ((s*(-1))//numbers[i+1])*(-1))
                cals[3] += 1

cal(0, numbers[0])

print(maxV)
print(minV)
