def solution(bridge_length, weight, truck_weights):
    answer = 0
    i = 0
    bridge = [0] * bridge_length
    bridge[-1] = truck_weights[i]
    answer += 1
    i = 1
    while len(bridge):
        
        answer += 1
        bridge.pop(0)
        if len(truck_weights)-1 >= i:
            if sum(bridge) + truck_weights[i] <= weight:
                bridge.append(truck_weights[i])
                i += 1
            else:
                bridge.append(0)
    
    return answer




bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,100]
print(solution(bridge_length, weight, truck_weights))

print(truck_weights)

