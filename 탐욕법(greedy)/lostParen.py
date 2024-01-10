# 백준 1541번 잃어버린 괄호 : https://www.acmicpc.net/problem/1541

from collections import defaultdict, deque
import heapq as hq
import math
import sys
input = sys.stdin.readline

s = input()
ans = 0
arr = []
tmp = 0
for i in s:
    if i != "+" and i != "-" and i != "\n":
        tmp = tmp * 10 + int(i)
    else:
        arr.append(tmp)
        if len(arr) > 2 and arr[-2] == "+":
            arr[-3] += arr[-1]
            arr[-2] = i
            arr.pop()
        else:
            arr.append(i)
        tmp = 0
        
ans = arr[0]      
for i in range(2, len(arr), 2):
    ans -= arr[i]
    
print(ans)

# 알고리즘 : 그리디
'''
풀이 : 모든 덧셈을 먼저 수행한 후, 뺄셈을 수행한다.
괄호를 그렸을 때, 가장 작은 수가 나오려면 덧셈끼리 묶어서 큰 수를 만든 뒤에 빼버리는 방법이 가장 유리하다.
예를 들면 다음과 같다.
1 - 2 + 3 + 4 - 5 + 6 - 7 + 8 + 9 인 경우
1 - (2 + 3 + 4) - (5 + 6) - (7 + 8 + 9) 가 가장 작다.
'''
