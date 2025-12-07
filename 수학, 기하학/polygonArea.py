# 백준 2166번 : 다각형의 넓이

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = [(list(map(int, input().split()))) for _ in range(n)]
arr.append(arr[0]) # 신발끈 이론

a = 0
b = 0
for i in range(n):
    a += arr[i][0] * arr[i + 1][1]
    b += arr[i][1] * arr[i + 1][0]
    
print("%.1f" % (abs(a - b) / 2))

# 알고리즘 : 신발끈 정리
'''
풀이 : 신발끈 정리 공식을 이용한다.
다각형의 면접 = 
(((현재 꼭지점의 x좌표) * (다음 꼭지점의 y좌표))의 총합 +
((현재 꼭지점의 y좌표) * (다음 꼭지점의 x좌표))의 총합)의 절댓값 / 2
'''
