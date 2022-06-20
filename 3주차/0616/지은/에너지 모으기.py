#3 1 2 4 5일 때 반례 발생
# n = int(input())
# weights = list(map(int, input().split()))
# energy = 0
# while len(weights)>2:
#     i = weights.index(max(weights))
#     if len(weights)==3:
#         energy += weights[0] * weights[2]
#         break
#     elif (i-2>-1 and i+2<len(weights) and weights[i-2] <= weights[i+2]) or i+2<len(weights):
#         energy += weights[i] * weights[i+2]
#         del weights[i+1]
#     elif (i-2>-1 and i+2<len(weights) and weights[i-2] > weights[i+2]) or i-2>-1:
#         energy += weights[i] * weights[i-2]
#         del weights[i-1]
# print(energy)

# def choose(weights):
#     ms = []
#     global energy
#     if len(weights)==2:
#         return energy
#     for i in range(1,len(weights)-1):
#         ms.append(weights[i-1]*weights[i+1])
#     energy += max(ms)
#     idx = ms.index(max(ms)) + 1
#     weights.pop(idx)
#     choose(weights)
#     return energy
# n = int(input())
# energy = 0
# weights = list(map(int, input().split()))
# print(choose(weights))

def select(num):
    global energy
    if len(weights)==2:
        energy = max(energy, num)
        return
    
    for i in range(1, len(weights)-1):
        m = weights[i-1]*weights[i+1]
        p = weights.pop(i)
        select(num+m)
        weights.insert(i,p)

n = int(input())
weights = list(map(int, input().split()))
energy = 0
select(0)
print(energy)