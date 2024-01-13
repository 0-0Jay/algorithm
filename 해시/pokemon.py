# 백준 1620번 나는야 포켓몬 마스터 이다솜 : https://www.acmicpc.net/problem/1620

import sys
input = sys.stdin.readline

def hashing(word):
    global sz, r
    key = 0
    for i in range(len(word)):
        now = (ord(word[i]) - 96)
        key += now * (r ** i)
    return key % sz

n, m = map(int, input().split())
sz = 50009  # 임의의 적당한 크기의 소수
r = 31  # 알파벳 26개 보다 큰 가장 작은 소수
index = [0] * (n + 1)
pokemon = [[] for _ in range(sz)]
for i in range(1, n + 1):
    index[i] = input().strip()
    key = hashing(index[i])
    pokemon[key].append([index[i], i])

for i in range(m):
    q = input().strip()
    if q.isdigit():
        print(index[int(q)])
    else:
        key = hashing(q)
        for po in pokemon[key]:
            if po[0] == q:
                print(po[1])

# 알고리즘 : 해싱
'''
풀이 : 각 포켓몬을 인덱스 배열에 저장하면서, 문자열 해싱을 이용해 pokemon 배열에도 저장해준다.
pokemon배열에 저장할 때는 [포켓몬, 인덱스] 형태로 저장한다.
질문이 들어오면 정수값인지 문자열인지 판단하고, 정수면 index에서 해당 인덱스를 출력한다.
문자열이면 해시함수로 key를 찾아 해당 포켓몬의 인덱스를 출력한다.
'''
