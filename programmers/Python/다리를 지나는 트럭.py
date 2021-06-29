# 다시하기...
def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length # 다리의 길이 만큼 0의 리스트 저장

    while q:
        time += 1 # 시간 계산
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)

    return 0
