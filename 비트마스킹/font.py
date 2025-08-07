# 백준 9997번 폰트 : https://www.acmicpc.net/problem/9997

n = int(input())
words = [0 for _ in range(n)]
cnt = 0
allsel = (1 << 26) - 1

def DFS(t, d):
    global cnt
    if t == allsel:
        cnt += 1 << n - d - 1
        return

    for i in range(d + 1, n):
        DFS(t | words[i], i)
        
for i in range(n):
    wd = input()
    for j in wd:
        words[i] |= 1 << ord(j) - 97

DFS(0, -1)
print(cnt)


'''
알고리즘 : 브루트포스 + 비트마스킹
풀이 : 각 단어를 입력받고, 단어에 포함된 알파벳을 아스키코드로 바꾸어 OR 연산하여 전부 정수로 바꾼 후, 결과값끼리 한번더 OR 연산한다.
모든 단어를 OR연산으로 words에 정수값으로 전환하여 저장한다.
n개의 단어를 DFS로 완전탐색한다.

이 때, 단순히 모든 단어를 완전탐색하면 재귀재한 및 시간초과의 문제가 발생한다.
이를 방지하기 위해 만약 allsel(모든 자릿수가 1인 값)과 같은 값이 발생한다면, 이 후의 값은 계속 allsel이 될것이다.(비트 or 연산)
즉, 각 단어를 고르거나 고르지 않거나 2경우를 남은 단어 만큼 반복반 횟수를 cnt에 누적한다.(2 ** 남은 단어수)
누적후 return하여 불필요한 재귀호출이 발생하는 일이 없게 해준다.
'''
