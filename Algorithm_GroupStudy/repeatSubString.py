# 백준 1605번 반복 부분문자열 : https://www.acmicpc.net/problem/1605

import sys
input = sys.stdin.readline

def chkWord(now, mid, arr):
    if len(arr) == 0: return False  # 해당 키에 값이 없으면 False
    for cmp in arr:
        tmp = 0
        for i in range(mid):  # 키의 값들 중 다른 값이 있으면 
            if word[now + i] != word[cmp + i]:
                tmp = 1
                break
        if tmp == 0: return True
    return False

sz = 50001
n = int(input())
word = [0] + list(input().strip())
l, r = 1, n
ans = 0
while l <= r:
    mid = (l + r) // 2
    hash = [[] for _ in range(sz)]
    tmp, k, flag = 0, 1, 0
    for i in range(1, n + 1):
        if i < mid : k = (k * 31) % sz  # 맨 앞글자를 빼기 위한 k값 계산
        if i > mid:
            tmp -= (ord(word[i - mid]) * k) % sz  # 맨 앞글자 빼기
            tmp = (tmp + sz) % sz  # 음수 나오지 않게 치환
        tmp = (tmp * 31 + ord(word[i])) % sz  # 한글자씩 추가
        if i >= mid:
            if chkWord(i - mid + 1, mid, hash[tmp]):
                l = mid + 1
                ans = mid
                flag = 1
                break
            hash[tmp].append(i - mid + 1)
    if flag == 1: continue
    r = mid - 1
    
print(ans)        
        
# 알고리즘 : 해싱 + 이분 탐색 + 슬라이딩 윈도우
'''
풀이 : 이분 탐색으로 문자열 길이를 정하고 전체 문자열에서 해당 길이의 중복된 문자열이 있는지 검사한다.
0 ~ mid 까지의 부분 문자열부터 n-mid ~ n까지의 부분 문자열을 하나씩 해싱하여 hash 배열에 넣는다.
넣다가 만약 이미 같은 부분 문자열이 존재한다면, ans를 정정해주고, 문자열 길이를 늘려주어 더 큰 부분 문자열이 있는지 검사한다.
같은 부분 문자열이 존재하지 않으면 문자열 길이를 줄여서 다시 탐색한다.

이 때, 문자열을 슬라이싱하여 사용하면, 슬라이싱 하는데 사용되는 시간 및 메모리 때문에 제한기준을 초과한다.
따라서 문자열을 word 배열에 넣고, 슬라이딩 윈도우 방식으로 탐색한다.
해당 부분 문자열이 hash배열에 있는지 검사할때도 슬라이싱이 아닌 인덱스를 활용해 검사한다.

요약하면 다음 3단계다.
1. 이분 탐색으로 탐색할 부분 문자열 길이를 정한다.
2. 문자열 길이 만큼 처음부터 끝까지 탐색해 동일한 부분 문자열이 있는지 체크한다.
3. 동일한 문자열이 있으면 길이를 늘려서 탐색하고, 없으면 길이를 줄여서 탐색한다.
'''
