# 프로그래머스 2022 카카오 블라인드채용 - 양과 늑대 : https://school.programmers.co.kr/learn/courses/30/lessons/92343?language=python3

import sys
sys.setrecursionlimit(100000)
    
answer = 1

def solution(info, edges):
    # edges는 항상 (부모, 자식 형태)
    global answer
    chk = set({0})
    
    def DFS(w, s):
        global answer
        if w >= s: return
        answer = max(answer, s); 
        
        for parent, child in edges:
            if parent in chk and child not in chk:
                chk.add(child)
                if info[child] == 0:
                    DFS(w, s + 1)
                else:
                    DFS(w + 1, s)
                chk.remove(child)
                
    DFS(0, 1)
    
    return answer

# 알고리즘 : DFS
'''
풀이 : 모든 간선을 탐색하면서 양과 늑대의 개수를 센다.
굉장히 DP스러운 문제다.
chk에 이미 방문한 정점을 체크해두고, 다음 DFS에서 현재 정점의 간선이 아닌, 전체 간선을 돌면서 늑대와 양의 개수를 센다.
이렇게하면 루트 노드부터 리프 노드까지 한단계씩 내려가면서 DFS를 탐색할 수 있다.
매 탐색마다 양의 최대 개수를 answer에 갱신하면서 탐색하고, 모든 탐색이 끝나면 answer를 리턴한다.
'''
