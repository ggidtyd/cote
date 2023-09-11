from collections import deque

def solution(bridge_length, weight, truck_weights):
    cur_weight, time = 0, 0
    bridge = deque([0] * bridge_length)
    waiting_trucks = deque(truck_weights)
    while waiting_trucks:
        time += 1
        cur_weight -= bridge[0]
        bridge.popleft()

        if cur_weight + waiting_trucks[0] <= weight:
            cur_weight += waiting_trucks[0]
            bridge.append(waiting_trucks.popleft())
        else:
            bridge.append(0)
        
    return time + bridge_length
