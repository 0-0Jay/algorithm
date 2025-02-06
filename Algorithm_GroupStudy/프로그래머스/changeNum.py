# 프로그래머스 - 숫자 변환하기 : https://school.programmers.co.kr/learn/courses/30/lessons/154538

from collections import deque

def solution(x, y, n):
    que = deque([(x, 0)])
    chk = set()
    chk.add(x)
    while que:
        a, cnt = que.popleft()
        if a == y: return cnt
        if a > y: continue
        if a + n not in chk:
            que.append((a + n , cnt + 1))
            chk.add(a + n)
        if a * 2 not in chk:
            que.append((a * 2, cnt + 1))
            chk.add(a * 2)
        if a * 3 not in chk:
            que.append((a * 3 , cnt + 1))
            chk.add(a * 3)
    return -1

# 알고리즘 : BFS
'''
풀이 : BFS로 완전탐색한다.
3가지 경우(n을 더하는 경우, 2를 곱하는 경우, 3을 곱하는 경우) 각각을 루트로 하여 BFS 탐색한다.
이 때, 각 경우의 결과값이 이전에 이미 나왔던 값이면, 불필요한 연산을 반복하게 되므로 chk로 중복체크 해준다.
3가지 경우 모두 결과값이 이전 값보다 작아질 수 없기 때문에, 현재값이 y값보다 크면 더 이상 탐색할 필요가 없다.
따라서 continue를 사용해 y보다 커지는 경우는 탐색에서 제외한다.
큐가 빌때까지 y를 만들지 못했다면, -1을 리턴한다.
'''
