# 프로그래머스 - 전령망을 둘로 나누기 : https://school.programmers.co.kr/learn/courses/30/lessons/86971

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA <= rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB
        
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def solution(n, wires):
    answer = 1e12
    for i in range(n - 1):
        parent = [k for k in range(n + 1)]
        for j in range(n - 1):
            if i == j: continue
            a, b = wires[j]
            if find(parent, a) != find(parent, b):
                union(parent, a, b)
                
        group = {}
        for j in range(1, n + 1):
            now = find(parent, j)
            if now not in group: group[now] = 0
            group[now] += 1
        tmp = list(group.items())
        answer = min(answer, abs(tmp[0][1] - tmp[1][1]))
            
            
    return answer

# 알고리즘 : 유니온/파인드 + 브루트포스
'''
풀이 : 와이어를 하나씩 끊어가며 유니온 파인드로 두 그룹을 찾는다.
0번 인덱스의 와이어부터 n - 1번 인덱스의 와이어까지 하나씩 선택한다.
선택한 와이어를 제외하고 나머지 와이어 연결 정보를 이용해 union/find로 parent 배열을 갱신한다.
반복문을 돌면서 group에 각 group의 루트 송전탑과 해당 전력망에 포함된 송전탑의 개수를 센다.
group에 있는 두 전력망의 송전탑 수의 차를 구해 절대값을 취한 후, answer와 비교하여 더 작은 값으로 교체한다.
모든 와이어를 한 번 씩 끊어봤다면, answer를 return 한다.
'''
