# 백준 9519번 졸려 : https://www.acmicpc.net/problem/9519

import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()
cycle = [''.join(s)]
for k in range(1, n + 1):
    res = []
    stk = []
    for i in range(0, len(s)):
        if i % 2 == 0: res.append(s[i])
        else: stk.append(s[i])
    while stk: res.append(stk.pop())
    s = ''.join(res)
    if cycle[0] == s:
        break
    cycle.append(s)
    
print(cycle[n % len(cycle)])

# 알고리즘 : 구현(시뮬레이션) + 스택
'''
풀이 : 글자 이동 규칙을 역으로 수행하되, 같은 단어가 되는 사이클의 길이를 구한다.
문제에서 제시한 글자 이동 규칙을 역으로 수행하면 다음과 같다.
1. 홀수번 글자는 res 스택에 쌓고, 짝수번 글자는 stk 스택에 쌓는다.
2. res에 stk의 글자를 하나씩 pop해서 쌓는다.

그러나 위 과정을 단순히 n번만큼 반복하면 너무 많은 시간이 소요된다.
위 과정의 특징 상, 반드시 사이클이 존재하기 때문에 사이클 길이만큼만 탐색하며 된다.
먼저 cycle 배열에 0번째에 첫 단어를 저장해두고, 단어 섞는 과정을 반복한다.
cycle[0]과 같은 단어가 탐색되면, 그 이후의 과정은 cycle 배열에 저장된 순서대로 n번 반복하게 된다.
따라서 cycle 배열에서 n을 cycle의 길이만큼 나눈 나머지 인덱스에 존재한 값을 출력한다.
'''

        
