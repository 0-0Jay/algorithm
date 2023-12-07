# 프로그래머스 순위 : https://school.programmers.co.kr/learn/courses/30/lessons/49191

from collections import deque
import heapq as hq
import sys
input = sys.stdin.readline

def solution(n, results):
    answer = 0
    chk = [[0] * (n + 1) for _ in range(n + 1)]
    row = [0] * (n + 1)
    col = [0] * (n + 1)
    
    for res in results:
        chk[res[0]][res[1]] = 1
        row[res[0]] += 1
        col[res[1]] += 1
              
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if chk[i][j] == 0 and chk[i][k] == 1 and chk[k][j] == 1:
                    chk[i][j] = 1
                    row[i] += 1
                    col[j] += 1
       
    for i in range(1, n + 1):
        if row[i] + col[i] == n - 1 : answer += 1
                
    return answer

# 알고리즘 : 플로이드 워셜
'''
풀이 : 플로이드 워셜로 선수들 간 우열을 판단한다.
처음 주어지는 results대로 chk[승리][패배]를 1로 표시한다.
승패 정보를 표시하면서 row배열과 col 배열의 각 선수 번호에 1의 총 합을 기록한다.
이 후, 플로이드 워셜 알고리즘으로 results로 알 수 있는 추가적인 우열 정보를 추가로 탐색한다.
예를 들면 다음과 같다.
ex) result : 1번 선수가 3번 선수를 이김 / 3번 선수가 2번 선수를 이김.
    -> 1번 선수는 2번 선수를 이긴다는 추가 정보 알 수 있음

이 후, col과 row의 각 선수 번호 인덱스의 값을 더했을 때, n-1이라면, 다른 n-1명과의 우열관계를 정확히 계산할 수 있다는 뜻이므로 answer에 +1 한다.
-> row는 승리 수, col은 패배 수가 되므로 row + col이 n-1이면 승패 기록만 가지고 순위를 판단할 수 있다.
'''
