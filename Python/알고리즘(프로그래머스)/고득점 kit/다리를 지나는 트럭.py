'''
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

경과 시간	다리를 지난 트럭     다리를 건너는 트럭	  대기 트럭
    0	    []	                []	                [7,4,5,6]
    1~2	    []	                [7]	                [4,5,6]
    3	    [7]	                [4]	                [5,6]
    4	    [7]	                [4,5]	            [6]
    5	    [7,4]	            [5]	                [6]
    6~7	    [7,4,5]	            [6]	                []
    8	    [7,4,5,6]	        []	                []
따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 
이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

* 제한 사항
    - bridge_length는 1 이상 10,000 이하입니다.
    - weight는 1 이상 10,000 이하입니다.
    - truck_weights의 길이는 1 이상 10,000 이하입니다.
    - 모든 트럭의 무게는 1 이상 weight 이하입니다.
'''

'''
* 풀이 아이디어

1. 다리의 길이만큼 큐(bridge)를 0으로 초기화합니다. (예: 다리 길이가 2 → [0,0])

2. 시간(time)을 1초씩 증가시키며 시뮬레이션합니다.
    매초마다 맨 앞 트럭이 다리를 빠져나감(popleft).
    현재 다리 위 무게 + 새 트럭 무게 ≤ 다리 최대 무게라면 새 트럭 진입.
    아니면 새 트럭 못 올라가고 0만 추가.
3. 모든 트럭이 다리를 건너면 종료.
'''


from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)  # 다리 위 상태 (0 = 빈칸)
    time = 0
    total_weight = 0  # 현재 다리 위 무게 합
    truck_weights = deque(truck_weights)  # 대기 트럭 큐

    while bridge:
        time += 1
        # 1. 다리에서 트럭 한 칸 전진 → 맨 앞 요소 빠짐
        total_weight -= bridge.popleft()

        # 2. 대기 트럭이 있다면, 다리에 올릴 수 있는지 확인
        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                total_weight += truck
            else:
                bridge.append(0)  # 못 올라오면 빈칸 채움

    return time


'''
예시1)
import collections

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()

    
예시2)
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step

예시3)
def solution(bridge_length, weight, truck_weights):
    t = 0
    on = []  # (weight, stayed)
    while truck_weights or on:
        for i, e in enumerate(on):
            on[i] = (e[0], e[1] + 1)
        on = list(filter(lambda x: x[1] < bridge_length + 1, on))

        weight_sum = 0
        for e in on:
            weight_sum += e[0]

        if truck_weights:
            if weight_sum + truck_weights[0] <= weight:
                on.append((truck_weights.pop(0), 1))
        t += 1
        # print(str(t)+":"+str(on))
    return t

예시4)
def solution(bridge_length, weight, truck_weights):
    queue = []
    seconds = 1
    total_weights = 0
    for truck in truck_weights:
      if not queue:
        queue.append((truck, seconds))
        total_weights += truck
      else:
        if(total_weights+truck <= weight):
          seconds += 1
          queue.append((truck, seconds))
          total_weights += truck
        else:
          while(total_weights+truck > weight):
            seconds = queue[0][1]+bridge_length
            if(queue[0][1]+bridge_length > queue[-1][1]): seconds = queue[0][1]+bridge_length
            else: seconds = queue[-1][1]+1
            total_weights -= queue[0][0]
            queue.pop(0)
          queue.append((truck, seconds))
          total_weights += truck

    if queue:
      seconds = queue[-1][1]+bridge_length

    answer = seconds

    return answer
'''
