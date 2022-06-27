def solution(bridge_length, weight, truck_weights):
    time = 0
    on_bridge = [0] * bridge_length

    while on_bridge:
        time += 1
        on_bridge.pop(0)
        if truck_weights:
            if sum(on_bridge) + truck_weights[0] <= weight:
                on_bridge.append(truck_weights.pop(0))
            else:
                on_bridge.append(0)
    return time

# def solution(bridge_length, weight, truck_weights):
#     truck_weights=truck_weights[::-1]
#     time = 0
#     on_bridge = [0]*bridge_length

#     while on_bridge:
#         time += 1
#         del on_bridge[0]
#         if truck_weights:
#             if sum(on_bridge) + truck_weights[-1] <= weight:
#                 on_bridge.append(truck_weights.pop())
#             else:
#                 on_bridge.append(0)
#     return time

# 빠르게 만들려고 pop(0)를 안써봤는데 더 빨라진 것도 있고 더 느려진 것도 있다