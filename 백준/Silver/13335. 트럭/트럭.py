from collections import deque
import sys
input = sys.stdin.readline

# n 트럭의 수, w 다리의 길이,  L 다리의 최대하중
n, w, L = map(int, input().rstrip().split())

truck_list = list(map(int, input().rstrip().split()))

bridge = deque()  # 첫번째 차량 다리에 추가
bridge.append((truck_list[0], 1))
wating_truck = deque(truck_list[1:])

time = w + 1  # 마지막 차량이 다리를 건너는 시간 + 1으로 초기화

# 기다리고 있는 트럭이 없을떄까지 반복
while wating_truck:
    time += 1

    # 다리위에 차가 있으면
    if bridge:

        # 다리 위에 있는 차의 위치 한칸씩 이동
        for index in range(len(bridge)):
            bridge[index] = (bridge[index][0], bridge[index][1] + 1)

        # 다리 위 첫번째 트럭이 끝까지 오면 나감
        if bridge[0][1] > w:
            bridge.popleft()

        # 다리에 자리가 있으면 무게 체크 후 새로운 트럭 추가
        if len(bridge) < w and sum(x[0] for x in bridge) + wating_truck[0] <= L:
            bridge.append((wating_truck.popleft(), 1))

    else:
        bridge.append((wating_truck.popleft(), 1))


print(time)
