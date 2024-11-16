# 프로그래머스 2020 카카오 블라인드채용 - 자물쇠와 열쇠 : https://school.programmers.co.kr/learn/courses/30/lessons/60059#

def turnKey(point, sz):
    res = []
    for x, y in point:
        res.append((y, sz-x-1))  # 시계방향 90도 회전
    return res

def checkKey(point, lock_u, lock_n): # 열쇠 돌기, 자물쇠 홈, 자물쇠 돌기
    for key in point:
        for u in lock_u:
            dx = u[0] - key[0]
            dy = u[1] - key[1]
            chk = set()
            for i in point:
                chk.add((i[0] + dx, i[1] + dy))
            if lock_u <= chk and len(chk & lock_n) == 0: return True
    return False
            
def solution(key, lock):
    point = []
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1:
                point.append((i, j))
                
    lock_u = set()  # 홈
    lock_n = set()  # 돌기
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                lock_u.add((i, j))
            else :
                lock_n.add((i, j))
    
    if len(lock_u) == 0 : return True  # 자물쇠가 이미 열려 있으면 True
    if len(point) == 0 : return False  # 자물쇠가 열려있지 않은데 열쇠에 홈이 없으면 False
    
    for i in range(4):
        if checkKey(point, lock_u, lock_n): return True
        if i < 3: point = turnKey(point, len(key))
    
    return False

# 알고리즘 : 구현(시뮬레이션)
'''
풀이 : 열쇠를 90도씩 돌리고 자물쇠의 홈의 좌표를 따라 가로 세로로 이동하며 맞춰본다. 
먼저 자물쇠의 돌기, 홈의 좌표와 열쇠의 돌기 좌표를 각각 분리한다.
이렇게 분리하는 이유는 열쇠의 패턴과 자물쇠의 패턴이 잘 맞물리는지만 확인하면 되므로 전체 2차원 배열을 모두 비교하지 않아도 되기 때문이다.
즉, 열쇠로 자물쇠를 열 수 있는 조건을 정리하면 다음과 같다.
1. 자물쇠의 모든 홈 좌표가 열쇠의 돌기 좌표에 존재한다.
2. 자물쇠의 모든 돌기 좌표가 열쇠의 돌기 좌표에 존재하지 않는다.

탐색에 앞서, 문제 조건에 자물쇠의 모든 홈을 채워 비어있는 곳이 없으면 자물쇠는 열린다고 되어있다.
즉, 자물쇠에 애초에 홈이 없으면 True를 반환한다.
반대로, 자물쇠에 홈이 있음에도 불구하고 열쇠에 돌기가 하나도 없으면 자물쇠를 절대 열 수 없기 때문에 False를 반환한다.

이제 열쇠를 90도씩 돌려가면서(turnKey 함수) 탐색한다.
열쇠의 각 돌기좌표를 하나씩 자물쇠의 홈좌표에 차례대로 대응시켜본다.(checkKey 함수)
첫 번째 열쇠 돌기를 첫번째 자물쇠 홈의 좌표에 맞추고 나머지 열쇠의 돌기 좌표를 가로 세로로 동일하게 움직이면 열쇠 전체를 움직인 것과 같다.
움직인 열쇠 돌기 좌표들과 자물쇠의 돌기, 홈 좌표들과 집합연산하여 열 수 있는지 확인한다.
자물쇠의 돌기 집합이 열쇠 돌기 집합의 부분집합이고, 열쇠 돌기 집합과 자물쇠 돌기 집합의 교집합이 없으면 True를 반환한다.
위 과정들을 모든 (열쇠 돌기, 자물쇠 홈) 경우의 수에 전부 탐색한다.

한 번이라도 checkKey의 결과가 True라면 열 수 있는 자물쇠이므로 True를 반환하고, 그렇지 않으면 False를 반환한다.
'''
