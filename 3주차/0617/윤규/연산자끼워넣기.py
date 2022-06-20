n = int(input())
arr = list(map(int, input().split(' ')))
cal = list(map(int, input().split(' ')))


def seq(cal, result):
    global maxV, minV
    if sum(cal) == 0:
        res = arr[0]
        for i in range(len(result)):
            if result[i] == 0:
                res += arr[i+1]
            elif result[i] == 1:
                res -= arr[i+1]
            elif result[i] == 2:
                res *= arr[i+1]
            elif result[i] == 3:
                if res < 0:
                    res = ((res * (-1))//arr[i+1])*(-1)
                else:
                    res //= arr[i+1]
        if res > maxV:
            maxV = res
        if res < minV:
            minV = res
        return
    else:
        for i in range(4):
            if cal[i]:
                cal[i] -= 1
                result2 = result[:]
                result2.append(i)
                seq(cal, result2)
                cal[i] += 1
maxV = -99999999
minV = 999999999
seq(cal, [])
print(maxV)
print(minV)