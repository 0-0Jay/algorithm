# 프로그래머스 2022 카카오 TECH 인턴십 - 두 큐 합 같게 만들기 : https://school.programmers.co.kr/learn/courses/30/lessons/118667#

def solution(queue1, queue2):
    goal = sum(queue1 + queue2)
    if goal % 2 == 0: 
        goal //= 2
    else: return -1
    que = (queue1 + queue2) * 2
    left, right = 0, len(queue1)
    now = sum(queue1)
    cnt = 0
    while left < right:
        if now < goal and right < len(que):
            cnt += 1
            now += que[right]
            right += 1
        elif now > goal and left < right:
            cnt += 1
            now -= que[left]
            left += 1
        elif now == goal:
            return cnt
        else:
            break               
    return -1

# 알고리즘 : 투포인터
'''
풀이 : 1번 큐 뒤에 2번 큐를 이어붙이고, 2개의 포인터로 큐 간 숫자 교환을 제어한다.
일단 두 큐의 합이 같게 만드려면 두 큐의 합이 반드시 짝수여야 한다.
따라서 1번 큐의 모든 원소의 합과 2번 큐의 모든 원소의 합을 더했을 때 그 값이 홀수면 바로 -1을 리턴한다.
값이 짝수면 (모든 원소의 합 / 2) 한 값을 목표값으로 설정한다(goal)

문제에서 요구하는대로 큐를 2개 만들고, 주어진 두 개의 배열을 각 큐에 옮겨 직접 시뮬레이션 하게되면 효율적이지 못하다.
따라서 right 포인터를 +1 하면 값을 더하고, left 포인터를 +1하면 값을 빼는 투포인터 기법을 응용한다.
주어진 1번 큐와 2번 큐를 이어붙이고, left 포인터를 0번 인덱스 right 포인터를 1번 큐의 길이와 같은 인덱스에 둔다.
이렇게 하면 1번 큐에 2번 큐의 값을 가져오는 과정을 단순히 right 포인터를 + 1 해주는 것으로 처리할 수 있다.
마찬가지로 1번 큐의 값을 2번 큐로 넘기는 과정 또한 left 포인터를 + 1해주는 것으로 처리할 수 있다.
두 큐 중 하나의 원소합만 goal과 같으면 나머지는 자동으로 goal과 같기 때문에 직접 큐를 만들 필요가 없다.

그러나, 단순히 이 방식으로 진행하면 큐에 들어있는 원소의 순서에 따라 문제가 발생한다.
예를 들어, 1번 큐에서 2번큐로 이동 했다가 다시 1번 큐로 돌아와야하는 경우가 있다.
테스트 케이스 2번의 경우처럼 2번 큐에 있는 1이 1번 큐로 옮겨졌다가 다시 2번 큐로 돌아오는 경우가 그 예시다.
이를 해결하기 위해 간단히 (1번 큐 + 2번 큐)로 만든 배열을 그대로 2배한다.
이렇게 하면 1번큐의 첫번째 값이 2번큐에 넘어가고, 2번 큐의 모든 원소를 다시 1번 큐로 옮겼을 때, 다시 1번큐의 첫번째 값으로 돌아가는 것을 처리할 수 있다.

위에서 설명한 내용을 바탕으로 탐색을 진행하기 전에, 1번 큐의 합을 now에 저장한다.
now가 goal보다 작으면, 1번 큐의 합이 2번 큐의 합보다 작다는 의미이므로 2번 큐의 값을 1번 큐로 가져와야한다. 즉 right 포인터를 +1 한다.
반대의 경우면 left 포인터를 +1 하면 된다.
이렇게하면 now에 left ~ right의 원소의 합이 저장되기 때문에 이 now가 goal과 같아지는 순간 포인터를 움직인 횟수(cnt)를 리턴하면 된다.
right를 (1번 큐 + 2번 큐) * 2 배열의 끝까지 탐색했거나, left가 right를 넘어가는 경우, 더 이상 탐색할 수 없기 때문에 break로 while문을 중지시킨다.
now == goal 조건문을 거치치 않고 while문이 중지되었으면 -1을 리턴하게 처리한다.
'''
