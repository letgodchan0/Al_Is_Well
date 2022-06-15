n = int(input())
number = list(map(int, input().split()))

def find(number, energy):
    global answer
    if len(number) == 2:
        if energy > answer:
            answer = energy
        return

    else:
        for i in range(1, len(number)-1):
            val = number[i-1] * number[i+1]
            tmp = number.copy(); tmp.pop(i)
            find(tmp, energy + val)
answer = 0
find(number, 0)
print(answer)