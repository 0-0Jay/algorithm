# 2024 네이버 신입 공채 - 행복한 식물

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def solution(emotions, orders):
    tmp = [i for i in emotions]
    result = []
    for i in range(len(orders)):
        result.append(result[-1] if result else len(emotions))
        for j in range(len(emotions)):
            if j == orders[i] - 1 and tmp[j] > 0:
                tmp[j] = emotions[j]
            else:
                tmp[j] -= 1
                if tmp[j] == 0:
                    result[i] -= 1
    return result

# 예제 1
print(solution([2,3,1,2], [3,1,2,1,3,1])) # [4,2,2,2,2,1]
# 예제 2
print(solution([5,5,5], [1,2,1,2,3])) # [3,3,3,3,3]
# 예제 3
print(solution([5,5,5], [1,2,1,2,1])) # [3,3,3,3,2]
# 예제 4
print(solution([2,1,3,4,3], [2,2,2,2,5,5,5])) # [5,4,2,1,0,0,0]

# 알고리즘 : 시뮬레이션
'''
풀이 : orders를 1회 순회하여 emotions를 갱신한다.
식물별로 초기 상태를 알고 있어야 하기 때문에, emotions를 그대로 복사한 배열(tmp)로 시뮬레이션을 수행한다.
result 배열을 하나 만들어 각 사이클 당 기분좋은 식물의 개수를 센다.
result 배열이 비어있으면 초기 기분좋은 식물의 개수인 len(emotions)를 삽입한다.
tmp에서 orders에 해당하는 식물의 기분을 초기값으로 갱신한다. 그렇지 않은 식물들은 1씩 기분을 다운시킨다.
만약 해당 식물의 기분이 0이되면 현재 result의 값을 1 내린다.

다음 사이클 부터는 기분이 0인 식물이 존재할 수도 있다.
따라서 tmp[j]가 0보다 큰지 확인하고, 그렇다면 식물을 초기값으로 돌리는 작업을 수행한다.
만약 0이라면 수행하지 않는다.
한 번이라도 0으로 내려갔으면 다시 초기값으로 올라갈 일이 없기때문에 굳이 0으로 유지시키는 과정이 필요없다.
꾸준히 -1로 내려주면 된다.
'''


