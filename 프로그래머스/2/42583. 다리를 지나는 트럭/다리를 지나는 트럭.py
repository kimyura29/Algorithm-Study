from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque(truck_weights) # 출발
    # 다리 위 상태를 관리하는 큐 필요
    bridge= deque([0] * bridge_length) # [0, 0]
    time = 0 # 처음 시간
    bridge_weight = 0 # 현재 다리 위 무게
    # 큐가 비고, 다리 위 무게가 0이되면 멈춤
    while queue or bridge_weight > 0: # 다리 위에 트럭이 남아있을 수도 있으니까
            # 시간 1초 추가
            time += 1
            # 1초가 지날 때 마다 맨 앞 트럭 다리에 빠져나감
            bridge_weight -= bridge.popleft() # 다리 위 무게 - 나간 트럭 무게를 빼겠다
            # queue가 있다면
            if queue:
                # 새 트럭을 올릴 수 있다면
                if bridge_weight + queue[0] <= weight:
                        truck = queue.popleft() # 큐에서 트럭 빼주고
                        bridge.append(truck) # 다리 상태 관리 큐에 트럭 넣어주고 
                        bridge_weight += truck # 현재 다리 위 무게에 트럭 더해주기
                else:
                      bridge.append(0) # 못올라가면 빈칸 (0) 추가해줘야 시간 계산
                
    return time