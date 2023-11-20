# 백준 12100번 2048(easy) : https://www.acmicpc.net/problem/12100

from collections import deque
import sys
input = sys.stdin.readline
import copy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
max_num = 0

def DFS(board, d):
    global max_num
    if d == 5: 
        for i in range(n): 
            for j in range(n): 
                if max_num < board[i][j]:
                    max_num = board[i][j]
        return
    
    # 오른쪽으로 이동
    b = copy.deepcopy(board)
    for i in range(n): # 아래로
        tmp = []
        j = n - 1
        while j >= 0: # 왼쪽으로
            if b[i][j] != 0:
                tmp.append([b[i][j], 0])
            if len(tmp) > 1 and tmp[-2][0] == tmp[-1][0] and tmp[-2][1] == 0 and tmp[-1][1] == 0:
                tmp[-2][0] += tmp[-1][0]
                tmp[-2][1] = 1
                tmp.pop()
            j -= 1
        while len(tmp) < n:
            tmp.append([0, 0])           
        for j in range(n):
            b[i][n - j - 1] = tmp[j][0]         
    DFS(b, d + 1)

    # 위로 이동
    b = copy.deepcopy(board)
    for i in range(n): # 오른쪽으로
        tmp = []
        j = 0
        while j < n: # 아래로
            if b[j][i] != 0:
                tmp.append([b[j][i], 0])
            if len(tmp) > 1 and tmp[-2][0] == tmp[-1][0] and tmp[-2][1] == 0 and tmp[-1][1] == 0:
                tmp[-2][0] += tmp[-1][0]
                tmp[-2][1] = 1
                tmp.pop()
            j += 1              
        while len(tmp) < n:
            tmp.append([0, 0])           
        for j in range(n):
            b[j][i] = tmp[j][0]
    DFS(b, d + 1)
                   
    # 아래로 이동
    b = copy.deepcopy(board)
    for i in range(n): # 오른쪽으로
        tmp = []
        j = n - 1
        while j >= 0: # 위로
            if b[j][i] != 0:
                tmp.append([b[j][i], 0])
            if len(tmp) > 1 and tmp[-2][0] == tmp[-1][0] and tmp[-2][1] == 0 and tmp[-1][1] == 0:
                tmp[-2][0] += tmp[-1][0]
                tmp[-2][1] = 1
                tmp.pop()
            j -= 1               
        while len(tmp) < n:
            tmp.append([0, 0])          
        for j in range(n):
            b[n - j - 1][i] = tmp[j][0]
    DFS(b, d + 1)
    
    # 왼쪽으로 이동
    b = copy.deepcopy(board)
    for i in range(n): # 아래로
        tmp = []
        j = 0
        while j < n: # 오른쪽으로
            if b[i][j] != 0:
                tmp.append([b[i][j], 0])
            if len(tmp) > 1 and tmp[-2][0] == tmp[-1][0] and tmp[-2][1] == 0 and tmp[-1][1] == 0:
                tmp[-2][0] += tmp[-1][0]
                tmp[-2][1] = 1
                tmp.pop()
            j += 1
        while len(tmp) < n:
            tmp.append([0, 0])            
        for j in range(n):
            b[i][j] = tmp[j][0]        
    DFS(b, d + 1)
    
DFS(board, 0)
print(max_num)

# 알고리즘 : BFS + 구현
'''
풀이 : 상하좌우로 움직이는 4가지 경우로 BFS를 수행한다.
이동은 한 줄 씩 이동시키는데, 다음과 같이 수행한다.
1. 이동하려는 방향의 반대방향으로 탐색을 시작해서 숫자를 발견할때마다 tmp배열에 append한다.
   1-1. 이 과정으로 자연스럽게 이동하려는 방향으로 숫자가 정렬된다.
2. 만약 tmp에 두자리 이상 숫자가 찼고, tmp의 마지막 두자리가 모두 합쳐지지 않았고, 숫자가 같으면 숫자를 합친다.
   2-1. tmp를 2차원으로 각 숫자별 0번은 값, 1번은 합쳐졌는지 여부를 기록하여 활용했다.
3. 위 과정을 모든 줄에 반복한 것을 1회 이동으로 둔다.

5회 이동이 완료되면 board의 모든 자리를 max_num과 최대값 비교한다.
'''
