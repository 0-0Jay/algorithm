# 백준 1022번 - 소용돌이 예쁘게 출력하기 : https://www.acmicpc.net/problem/1022

import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
arr = [[0 for _ in range(y2 - y1 + 1)] for _ in range(x2 - x1 + 1)]
cnt = len(arr) * len(arr[0])
d, key, now = 1, 1, 1
x, y = 0, 0
m = 0

while cnt > 0:
    for _ in range(d):
        if x1 <= x <= x2 and y1 <= y <= y2:
            arr[x - x1][y - y1] = now
            cnt -= 1
            m = now
        y += key
        now += 1
    for _ in range(d):
        if x1 <= x <= x2 and y1 <= y <= y2:
            arr[x - x1][y - y1] = now
            cnt -= 1
            m = now
        x -= key
        now += 1
    key *= -1
    d += 1

n = len(str(m))
x, y = len(arr), len(arr[0])
for i in range(x):
    for j in range(y):
        print(str(arr[i][j]).rjust(n), end = " ")
    print()

# 알고리즘 : 구현
'''
풀이 : 주어진 범위에 속할때만 배열에 값을 삽입한다.
기본적으로 이 문제는 주어진 메모리 크기가 128mb로 상당히 작다.
즉, 진짜로 -5000부터 5000까지의 배열을 만들면 반드시 메모리 초과가 발생한다.
따라서 주어진 x1, y1 부터 x2, y2까지의 크기만 만들고, 해당 범위에 들어오는 숫자만 입력하는 방식으로 구현해야한다.

일단, 배열을 (x2 - x1 + 1) * (y2 - y1 + 1) 크기로 만든다.
배열을 만들면서 배열의 칸수를 cnt에 저장한다.
즉, cnt가 빈칸의 개수이므로 cnt가 0이되면 더이상 탐색을 하지 않아도 된다.
다음으로, 거리를 컨트롤할 변수(d)와 방향을 컨트를할 변수(key), 현재 숫자를 나타내는 변수(now)를 선언한다.
x, y 좌표는 0, 0으로 둔다.

모든 기본 설정이 완료되었으면, 반복문으로 숫자를 채워넣는다.
d만큼 가로를 채우고 d만큼 세로를 채운다.
만약 key가 1이면 가로는 오른쪽, 세로는 위로 이동하고, key가 -1이면 가로는 왼쪽, 세로는 아래로 이동한다.
즉, 가로와 세로의 이동을 한 세트로 두고 key만 1과 -1을 계속 스왑하면서 d를 1씩 올려주면 소용돌이로 숫자를 채울 수 있다.
이때, x, y가 처음 주어진 범위 안이라면, 이 좌표를 arr 상의 좌표에 이동시켜 저장한다.

모든 반복이 끝나고, 지금까지 채워진 숫자들 중 가장 큰 수의 길이를 구한다.(n)
이 길이만큼 rjust를 활용해 포맷팅하여 숫자를 출력한다.
'''
