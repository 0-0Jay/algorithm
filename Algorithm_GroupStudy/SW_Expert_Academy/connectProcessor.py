# 1767. [SW Test 샘플문제] 프로세서 연결하기 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf

dt = [[0, 1], [1, 0], [-1, 0], [0, -1]]
t = int(input())

for test in range(1, t + 1):
    n = int(input())
    arr = []
    core = []
    min_sum = 200
    max_core = 0
    
    for i in range(n):
        tmp = list(map(int, input().split()))
        arr.append(tmp)
        for j in range(n):
            if 0 < i < n - 1 and 0 < j < n - 1 and tmp[j] == 1:
                core.append((i, j))
                
    def chkLine(tx, ty, dir):  # 전선 연결 가능한지 
        line = 0
        while 0 < tx < n - 1 and 0 < ty < n - 1:
            tx += dt[dir][0]
            ty += dt[dir][1]
            if arr[tx][ty] == 1:
                return 0
            else:
                line += 1        
        return line
                
    def DFS(d, s, c):  # 백트래킹 탐색
        global min_sum
        global max_core
        if d == len(core):
            if max_core > c: return  # 최대 코어 수 보다 작으면 배제
            elif max_core == c:  # 최대 코어 수와 같으면 최소 거리로 교체
                min_sum = min(min_sum, s)
            else:  # 최대 코어수보다 크면 최소 거리, 최대 코어수 교체
                max_core = c
                min_sum = s
            return
        if max_core > c + len(core) - d:  # 만약 남은 코어를 모두 사용한다 해도 최대 코어수보다 적으면 리턴
            return
        
        for i in range(4):  # 4방향 탐색
            x, y = core[d]
            px, py = x, y
            a = chkLine(x, y, i)
            if a:
                while 0 < px < n - 1 and 0 < py < n - 1:
                    px += dt[i][0]
                    py += dt[i][1]
                    arr[px][py] = 1
                DFS(d + 1, s + a, c + 1)
                while 0 < x < n - 1 and 0 < y < n - 1:
                    x += dt[i][0]
                    y += dt[i][1]
                    arr[x][y] = 0
                    
        DFS(d + 1, s, c)  # 코어 4방향이 모두 막힌경우 코어 갯수 증가 없이 이동
        
    DFS(0, 0, 0)
    
    print('#%d %d' %(test, min_sum))

# 알고리즘 : 백트래킹 + 구현
'''
풀이 : 각 코어당 4방향을 탐색한다. 만약 4방향 모두 불가능한 코어일 경우 사용하지 않는다.
코어 정보 중, arr의 가장자리에 위치한 코어는 arr에 표시는 하되, 사용할 코어에 포함하지 않는다.
필요한 정보는 전선의 길이기 때문에 이미 연결된 코어는 계산에 넣지 않는게 효율적이다.

모든 코어를 d라는 index 변수를 이용해 하나씩 탐색한다.
chkLine 함수와 dt배열을 활용해 해당 각 4방향으로 전선을 연결할 수 있는지 탐색한다.
만약 연결할 수 있다면 사용한 코어(c)로 카운팅하고 다음 재귀를 호출한다.
연결할 수 있는 전선이 없다면, c에 카운팅하지 않고 d만 +1하여 재귀를 호출한다.
문제에 주어져 있는 조건인 전원이 연결되지 않는 코어가 존재할 수 있기 때문이다.

만약 모든 코어를 탐색했다면, 문제조건에 맞게 최대 코어 수와 최소 전선 길이를 교체한다.
앞으로 탐색할 코어 수 + 현재 사용한 코어 수가 현재 최대 코어 수보다 작다면, 더 이상 탐색할 필요가 없다.
문제 조건에 코어를 가장 많이 연결할 수 있는 방법 중 가장 짧은 전선 길이를 요구하기 때문이다.

그 외에는 다른 부분은 다른 백트래킹처럼 풀면 된다.
주의할 점은 단순히 최소 전선 길이가 짧다고 해서 답을 정하면 안된다는 것이다.
코어의 개수가 늘어나면 최소 전선 길이에 상관없이 교체해야한다.
'''
