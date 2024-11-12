# 프로그래머스 - 풍선 터트리기 : https://school.programmers.co.kr/learn/courses/30/lessons/68646

def solution(a):
    min_val = [[1e12, 1e12] for i in range(len(a))]
    min_val[0][0] = a[0]
    min_val[-1][1] = a[-1]
    for i in range(1, len(a)):
        min_val[i][0] = min(min_val[i - 1][0], a[i])
        min_val[-i - 1][1] = min(min_val[-i][1], a[-i - 1])
        
    answer = len(a)
    for i in range(len(a)):
        if max(min_val[i]) < a[i]: answer -= 1
    
    return answer

# 알고리즘 : 시뮬레이션
'''
풀이 : 각 인덱스별로 왼쪽의 최소값과 오른쪽의 최소값을 구한다.
문제에서 두 풍선 중 작은 풍선을 터트리는 것은 1회만 가능하다는 조건이 있다.
즉, 계속 자신이 더 큰 풍선이다가 마지막에 자신보다 작은 풍선과 둘 만 남았을 때 작은 풍선을 터트리면 된다는 뜻이다.
위 조건을 다시 생각하면 자신을 기준으로 왼쪽과 오른쪽의 최소 풍선 중 자신보다 작은 풍선이 한 개여야 한다.
따라서 min_val 배열을 하나 만들고 양쪽에서 1칸씩 이동하며 각 인덱스별 좌우측의 최소값을 기록한다.
모두 기록 후, 각 인덱스 별로 a[i]의 값이 min_val[i]의 두 값보다 크다면, answer에서 1씩 차감시킨다. 
남은 answer을 반환하면 이 값이 곧 살아남을 수 있는 풍선의 수다.
'''
