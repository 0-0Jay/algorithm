# 백준 - 스택 2 : https://www.acmicpc.net/problem/28278

import sys
input = sys.stdin.readline

stk = []

for _ in range(int(input())):
    cmd = input().strip()
    if cmd[0] == "1":
        stk.append(cmd[2:])
    elif cmd[0] == "2":
        print(stk.pop() if stk else -1)
    elif cmd[0] == "3":
        print(len(stk))
    elif cmd[0] == "4":
        print(0 if stk else 1)
    elif cmd[0] == "5":
        print(stk[-1] if stk else -1)


# 알고리즘 : 스택
'''
풀이 : 스택을 직접 구현해본다.
'''
