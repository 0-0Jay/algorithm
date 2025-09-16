# 백준 2447번 - 별 찍기 10 : https://www.acmicpc.net/problem/2447

n = int(input())
field = [['*' for _ in range(n)] for _ in range(n)]

def star(x, y, n):
    now = n // 3
    if now == 0 : return
    for i in range(x + now, x + now * 2):
        for j in range(y + now, y + now * 2):
            field[i][j] = ' '
    for i in range(x, x + n, now):
        for j in range(y, y + n, now):
            star(i, j, now)

star(0, 0, n)
for i in range(n):
    for j in range(n):
        print(field[i][j], end='')
    print()

# 알고리즘 : 재귀
'''
풀이 : 정사각형을 3 * 3으로 계속 나누어 생각한다.
문제에 주어진 27 * 27 의 정사각형을 예로 들어보자.
9 * 9의 정사각형이 가로 3개 세로 3개로 총 9개로 배치되어 있다고 생각한다.
이 중 가운데 위치한 정사각형은 빈칸(' ')으로 채우고, 그 외에는 한 번 더 재귀탐색한다.
이를 더이상 나눌 수 없는 3 * 3 정사각형이 될 때까지 반복하여 수행한다.
'''
