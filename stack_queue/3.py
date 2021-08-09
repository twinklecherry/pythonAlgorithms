#https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3
from collections import deque 
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    
    while trucks: #while문이 끝나면 마지막 트럭까지 다리 위에 올라온 상태
        currTruck = trucks.popleft()

        if sum(bridge) + currTruck <= weight:
            bridge.popleft() #한 칸씩 앞으로 당기고
            bridge.append(currTruck) #현재 트럭을 맨 뒤에 추가 
            answer += 1 

        else:
            sumBridge = sum(bridge)
            #현재 트럭을 다리에 올릴 수 있을 때까지 
            while sumBridge + currTruck > weight:
                popTruck = bridge.popleft() # 한 칸씩 앞으로 당김 
                bridge.append(0) #queue의 길이 보존을 위해 appened로 추가
                answer += 1 
                sumBridge -= popTruck #while문에서 sum을 여러번 계산하지 않기 위해

            #현재 트럭을 맨 뒤에 위치시킴
            bridge[-1] = currTruck 
    #마지막 트럭이 다리를 끝까지 건너려면 bridge_length만큼의 시간이 소요됨     
    return answer + bridge_length

# 1) 다리를 1만큼 건널때 1초 소요
# 2) 가장 앞에 있는 트럭 꺼냄
# 3) 다리에 있는 트럭 확인
# 4) 다리에 트럭이 없거나 꺼낸 트럭과 다리에 있는 트럭의 합이 weight 이하면 다리를 트럭에 넣음

print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))