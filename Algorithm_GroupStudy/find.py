# 백준 1786번 찾기 : https://www.acmicpc.net/problem/1786

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

T = input()[: -1]
P = input()[: -1]
hsk = 131
sz = (1 << 25) - 1
div = (hsk ** len(P)) % sz

def hashing(word):
    res = 0
    for i in range(len(word)):
        res = (res * hsk + ord(word[i])) % sz
    return res

hash_p = hashing(P)
hash_T = hashing(T[:len(P)])
cnt = 0
point = []
for i in range(len(T) - len(P) + 1):
    if hash_p == hash_T:
        cnt += 1
        point.append(i + 1)
    if i + len(P) == len(T): break
    hash_T = (hsk * hash_T + ord(T[i + len(P)]) - ord(T[i]) * div) % sz

print(cnt)
print(*point)

# 알고리즘 : 라빈-카프 알고리즘(해싱)
'''
풀이 : 문자열 P를 해시값으로 변환하고, 문자열 T에서 슬라이딩윈도우 기법으로 각 구간 문자열 해시값을 비교한다.
가장 먼저 적당한 크기의 해쉬 키값(hsk)과 버킷 수(sz)를 정한다.
이 때, 각 수는 소수인 것이 좋고, sz는 너무 클 경우 메모리 손실이, 너무 작으면 많은 해시값 충돌을 발생시킨다.
또한, hsk를 문자열 P의 길이 만큼 제곱하고, sz로 나눈 나머지를 div로 저장해둔다.
-> div는 후에 슬라이딩 윈도우 기법으로 각 구간의 해시값을 계산할때 불필요한 중복 계산을 완전히 줄여주는 역할을 한다.

다음으로 해시 함수(hashing)을 만든다.
해시 함수는 입력으로 들어온 문자열을 아스키코드의 정수값으로 변환하고, hsk ** (자릿수)한 값을 모두 더한 값을 반환한다.
예를 들어 ABC가 입력된다면, (A * hsk ** 2) + (B * hsk ** 1) + C로 계산한 정수값을 반환한다. 

이를 이용해 문자열 P를 해시값으로 변환한다.(hash_p)
문자열 T에서 문자열 P를 찾는 문제이기 때문에 문자열 P의 길이로만 탐색하면 된다.
따라서 문자열 T에서 0번 인덱스부터 문자열 P의 길이만큼을 슬라이싱하여 해시값으로 변환한다.(hash_T)

모든 입력값 전처리가 완료되었다면, 문자열 T의 0번 인덱스부터 탐색한다.
hash_p와 hash_T의 해시값이 같다면, 나머지 연산의 법칙에 따라 두 문자열은 같은 문자열이다.
따라서 해시값이 같을때마다 1씩 카운팅하고, 해싱 값이 같아진 인덱스를 point에 저장한다.

이제 현재 범위의 부분문자열 hash_T의 검사가 끝났다면 슬라이딩 윈도우로 한칸 이동시켜야한다.
hash_T의 값은 (첫번째 글자 * hsk ** (P의 길이 - 1)) + (두번째 글자 * hask ** (P의 길이 - 2)) + ... + (마지막 글자) 의 결과값이다.
즉,  (첫번째 글자 * hsk ** (P의 길이 - 1))를 빼주고, 다음 글자를 더한 값에 hsk를 한 번 곱해주어야 한다.
그러나 연산을 수행하다보면, 기존 수보다  (첫번째 글자 * hsk ** P의 길이)의 값이 커서 결과값이 음수가 되는 경우가 존재한다.
이를 방지하기위해 계산 순서를 바꾸어야한다.
기존수에 hsk를 한 번 곱해주고, 다음 수를 더한 다음에  (첫번째 글자 * hsk ** P의 길이)를 빼준다.
-> 이 때 계속 반복되는 (첫번째 글자 * hsk ** P의 길이)를 처음에 div로 미리 계산해두어 사용한다.

문자열 T를 모두 탐색했으면, cnt와 point 배열의 값을 출력한다.
'''
