# 프로그래머스 2023 카카오 블라인드 채용 - 미로 탈출 명령어 : https://school.programmers.co.kr/learn/courses/30/lessons/150365

from collections import defaultdict, deque

def solution(n, m, x, y, r, c, k):
    # 문자열 기준 오름차순 : d < l < r < u
    h = r - x
    w = c - y
    dist = abs(h) + abs(w)
    diff = abs(dist - k)
    if diff % 2 != 0 or k < dist: return "impossible"

    # 최단 거리 이동에 사용된 방향 구하기
    tmp = {}
    tmp['l'] = abs(w) if w < 0 else 0
    tmp['r'] = w if w > 0 else 0
    tmp['d'] = h if h > 0 else 0
    tmp['u'] = abs(h) if h < 0 else 0
    
    answer = ''
    answer += 'd' * tmp['d']
    x += tmp['d']
    if diff > 0 and x < n:
        rem = min(n - x, diff // 2)
        answer += 'd' * rem
        tmp['u'] += rem
        diff -= 2 * rem
        
    answer += 'l' * tmp['l']
    y -= tmp['l']
    if diff > 0 and 1 < y:
        rem = min(y - 1, diff // 2)
        answer += 'l' * rem
        tmp['r'] += rem
        diff -= 2 * rem
        
    if diff > 0:
        rem = diff // 2
        answer += 'rl' * rem
        
    answer += 'r' * tmp['r']
    answer += 'u' * tmp['u']
    return answer

# 알고리즘 : 그리디
'''
풀이 : 명령어가 사전 순으로 앞서기 위해 d -> l -> r -> u 순으로 우선순위를 두고 명령어를 완성한다.
먼저 최단 거리로 이동할 때 필요한 각 명령의 수 가로 및 세로의 차이를 이용해 구한다.
만약 h가 음수라면 도착지가 출발지보다 위에 있다는 뜻이므로 u의 개수에 세로 차이를 추가한다.
w도 음수라면 도착지가 출발지보다 왼쪽에 있다는 뜻이므로 l의 개수에 가로 차이를 추가한다.

이 때, 최소 이동 수와 k를 비교하여 불가능 여부를 판별할 수 있다.
1. k가 최소 이동 수보다 작은 경우, 이동 수가 부족하므로 불가능
2. 최소 이동수와 k의 차이(diff)가 2의 배수가 아닌 경우 왕복으로 도착지에 돌아올 수 없기 때문에 불가능
-> 가로 세로로만 이동하기 때문에 도착지점에서 좌우 또는 상하로 2회를 사용해야 최종적으로 도착지에 있을 수 있다.

사전 작업이 모두 완료되었다면, diff를 이용하여 d부터 탐색한다.
tmp['d']에 있는 수만큼 answer에 추가한다.
x를 추가한 만큼 이동시켰을 때, diff / 2와 (n - x)를 비교한다.
만약 diff / 2가 더 작다면, diff / 2 만큼만 아래로 이동 후, 위로 돌아오면 된다.
그러나 (n - x)가 더 작다면 범위 끝까지 내려갔다가, 올라온 후에 좌우 이동으로 남은 k를 소모해야 한다.
더 작은 값(rem)만큼 answer에 d를 추가하고, tmp['u']에도 rem을 더해주고, diff에 rem * 2(상하를 한번에 계산)을 빼준다.
위 과정을 l 에도 똑같이 수행한다.

여기서 주의해야 할 점이 있다.
만약 위 과정을 계속 똑같이 수행하게 되면 자연스럽게 answer가 dddd...lll...rrr...uuu가 된다.
그러나 rrrrrlrl보다 rlrlrrrr이 사전순으로 더 앞선다.
또한, ud로 상하반복을 하는 것보다 rl로 좌우반복 하는 것이 사전 순에서 반드시 더 앞선다.
따라서 r과 u를 추가하기 전에, diff가 남아있다면 rl을 diff / 2만큼 answer에 추가해준다.

마지막으로 answer에 tmp['r']과 tmp['u']만큼 r과 u를 추가해주고 반환한다.
'''
