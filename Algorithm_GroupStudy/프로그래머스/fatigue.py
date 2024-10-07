# 프로그래머스 - 피로도 : https://school.programmers.co.kr/learn/courses/30/lessons/87946

max_cnt = 0
def solution(k, dungeons):
    def DFS(h, cnt, chk):  
        global max_cnt
        for i in range(len(dungeons)):
            if dungeons[i][0] <= h and chk & (1 << i) == 0:
                DFS(h - dungeons[i][1], cnt + 1, chk | (1 << i))
        max_cnt = max(cnt, max_cnt)    
    DFS(k, 0, 0)
    return max_cnt

# 알고리즘 : 브루트포스 + 비트마스킹
'''
풀이 : 비트마스킹을 통해 탐험한 던전을 체크하며 완전탐색 한다.
DFS로 던전 배열(dungeons)의 0번 인덱스부터 마지막 인덱스까지 탐색한다.
던전 배열에 있는 순서와 탐험 순서는 관계 없으므로 매 탐색마다 0~마지막 까지 탐색해야 한다.
이 때, 이미 중복 탐험을 방지하기 위해 chk 변수에 비트마스킹을 활용했다.
중복 체크 배열을 매개변수로 계속 전달하는 것보다 정수 하나를 전달하는 것이 효율적이기 때문이다.

최대 던전 수는 전역변수로 두고, DFS를 돌면서 계속 갱신해주었다.
'''
