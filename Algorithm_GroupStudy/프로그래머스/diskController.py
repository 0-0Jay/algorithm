# 프로그래머스 - 디스크 컨트롤러 : https://school.programmers.co.kr/learn/courses/30/lessons/42627#

import heapq as hq

def solution(jobs):
    jobs.sort()
    que = []
    time = 0
    total = 0
    key = 0
    while key < len(jobs) or que:
        if not que: 
            hq.heappush(que, (jobs[key][1], jobs[key][0]))
            key += 1
        while key < len(jobs) and jobs[key][0] <= time:
            hq.heappush(que, (jobs[key][1], jobs[key][0]))
            key += 1
        b, a = hq.heappop(que)
        if a > time: time = a
        time += b
        total += time - a

    return total // len(jobs)

# 알고리즘 : heap
'''
풀이 : 우선순위 큐를 이용해 짧은 작업 시간을 가진 것부터 수행한다.
먼저 입력값으로 주어지는 jobs가 정렬되어 있다는 조건이 없기 때문에 요청시간을 기준으로 정렬한다.
다음으로 대기열로 사용할 우선순위 큐와, 경과시간(time), 반환시간의 합(total)을 저장할 변수를 하나 생성한다.

key를 이용해 jobs를 처음부터 끝까지 탐색한다.
만약에 대기열이 비어있다면, que에 jobs[key]를 즉시 넣는다.
다음으로 time과 jobs의 요청시간을 비교해서 time보다 빠른 작업들을 모두 que에 넣어준다.
que는 실제 수행시간이 가장 짧은 것을 우선순위로 출력하는 큐이다.
따라서 while문에서의 삽입과정으로 인해 여러 작업이 들어와도 가장 짧은 작업시간부터 꺼낸다.

time과 꺼낸 작업의 요청시간을 비교하여 time을 업데이트 해주고,
꺼낸 작업의 수행시간을 time에 더해준다.
이 후, time에서 요청시간을 빼면 반환시간을 계산할 수 있고, 이를 total에 더해준다.

모든 작업이 끝난 후, total을 작업 개수만큼 나눠주면 반환시간의 평균을 계산할 수 있다.
'''
