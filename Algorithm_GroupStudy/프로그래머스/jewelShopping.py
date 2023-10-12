# 2020 카카오 인턴십 - 보석 쇼핑 : https://school.programmers.co.kr/learn/courses/30/lessons/67258#

def solution(gems):
    opt = set(gems)
    d = {}
    answer = [0, len(gems)]
    st, ed = 1, 0
    for i in gems:
        ed += 1
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
            
        while d[gems[st - 1]] > 1:
            d[gems[st - 1]] -= 1
            st += 1
        if len(d) == len(opt) and ed - st < answer[1] - answer[0]:
            answer = st, ed
    return answer

# 알고리즘 : 투 포인터
'''
풀이 : 시작점과 끝점의 두개의 포인터를 두고, 이동시키면서 조건에 맞는 포인트를 탐색한 후,최단구간인지 계산한다.

1. gems 배열을 처음부터 끝까지 차례대로 1개씩 딕셔너리(d)에 삽입한다. (끝점 +1)
2. 만약 d에서 gems[시작점]의 보석의 갯수가 2개 이상이면, 해당 보석을 뺀다 (시작점 -1)
3. 1~2번의 과정 이후 d에 모든 종류의 보석이 들어있으면 answer 배열에 넣는다.
  3-1. 단, answer배열에 저장되어있는 (끝점 - 시작점)보다 현재 발견한 (끝점 - 시작점)의 크기가 작을 때만 넣어 최단구간을 계산한다.
'''
