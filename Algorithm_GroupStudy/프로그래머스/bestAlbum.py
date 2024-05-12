# 프로그래머스 - 베스트앨범 : https://school.programmers.co.kr/learn/courses/30/lessons/42579

import heapq as hq

def solution(genres, plays):
    answer = []
    gen_dict = {}
    play_dict = {}
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        if g not in gen_dict: gen_dict[g] = 0
        gen_dict[g] += p
        if g not in play_dict: play_dict[g] = []
        hq.heappush(play_dict[g], (-p, i))
    
    gen = sorted(gen_dict.items(), key=lambda x: -x[1])
    print(gen)
    for g, v in gen:
        answer.append(hq.heappop(play_dict[g])[1])
        if play_dict[g]: answer.append(hq.heappop(play_dict[g])[1])
    
    return answer

# 알고리즘 : 우선순위 큐 + 해시
'''
풀이 : 장르별 재생 수를 저장할 딕셔너리와, 장르별 노래 고유 번호를 저장할 딕셔너리를 만들어 정렬한다.
우선 가장 재생이 많이 된 장르를 기준으로 정렬해야 하기 때문에 해시 자료구조인 딕셔너리를 활용한다.
gen_dict에 각 장르별 재생 횟수를 누적시키면서 play_dict 장르별 노래 고유 번호와 재생수를 기록한다.
이 때 play_dict의 정렬을 우선순위 큐를 이용하여 불필요한 완전 정렬을 방지했다.

가장 많이 재생된 장르를 찾기위해 gen_dict의 key, value 쌍을 value 를 기준으로 내림차순 정렬한다(gen).
gen 배열을 순회하면서 play_dict의 해당 장르 배열에서 우선순위 큐를 이용해 2번 뽑아 answer에 추가한다.
'''
