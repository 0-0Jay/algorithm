# 백준 11723번 집합 : https://www.acmicpc.net/problem/11723

import sys
input = sys.stdin.readline

n = int(input())
bitmask = 0
for _ in range(n):
    val = 1
    cmd = list(input().strip().split(" "))
    if len(cmd) > 1: val = int(cmd[1])
    tmp = 1 << (val - 1)
    if cmd[0] == "add":
        if bitmask & tmp == 0:  # 비트에 체크되어 있지 않다면 or 연산으로 추가
            bitmask |= tmp
    elif cmd[0] == "remove":
        bitmask &= ~tmp  # 비트에 있는 숫자를 ~tmp와 &연산하여 제거
    elif cmd[0] == "check": 
        print(0 if bitmask & tmp == 0 else 1)
    elif cmd[0] == "toggle":
        if bitmask & tmp == 0:
            bitmask |= tmp
        else:
            bitmask &= ~tmp
    elif cmd[0] == "all":
        bitmask = (tmp << 20) - 1  # 모든 비트에 체크할때는 비트 최대수 + 1만큼 왼쪽 시프트한 결과에서 -1
    else:
        bitmask = 0  # 비트 초기화는 단순히 0을 저장
# 알고리즘 : 비트마스킹
'''
풀이 : 비트연산을 통해 숫자의 유무를 체크한다.
비트마스킹을 구현해보는 문제다.
'''
