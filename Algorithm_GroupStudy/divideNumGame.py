# 백준 27172번 수 나누기 게임 : https://www.acmicpc.net/problem/27172

from collections import deque
import sys
input = sys.stdin.readline
import copy

n = int(input())
card = [0] * 1000001
arr = list(map(int, input().split()))
arr2 = copy.deepcopy(arr)
s = 0
for i in arr: 
    card[i] = 1
    if i > s: s = i
score = [0 for _ in range(s + 1)]
arr.sort()

for i in arr:
    for j in range(i * 2, s + 1, i):
        if card[j] == 1:
            score[i] += 1
            score[j] -= 1
                      
for i in arr2:
    print(score[i], end=" ")

# 알고리즘 : 에라토스테네스의 체
'''
풀이 : 에라토스테네스의 체를 응용하여 배수를 판별하고, 배수면 두 참가자의 점수를 조절한다.
입력받은 참가자들을 숫자 크기 오름차순으로 정렬하고 체를 사용해 배수를 찾는다.
배수를 발견하면 현재 참여자에 1점 추가, 상대 참여자에 1점 감소시킨다.
'''
