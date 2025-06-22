# 백준 9777번 - birthday Statistics : https://www.acmicpc.net/problem/9777

import sys
input = sys.stdin.readline

arr = [0] * 13

for i in range(int(input())):
    y, d = input().split(" ")
    tmp = tuple(d.split("/"))
    arr[int(tmp[1])] += 1

for i in range(1, 13):
    print(i, arr[i])
    
# 알고리즘 : 구현
'''
풀이 : 월을 인덱스로 쓸 수 있게 배열을 만들고 생일 중 월의 개수를 카운팅한다.
매 입력마다 split을 활용해 생일 중 월에 해당하는 숫자만 찾아내어 arr에 카운팅한다.
'''
