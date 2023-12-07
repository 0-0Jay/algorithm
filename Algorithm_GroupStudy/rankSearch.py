# 프로그래머스 - 2021 KAKAO BLIND RECRUITMENT 순위 검색 : https://school.programmers.co.kr/learn/courses/30/lessons/72412

from collections import deque
import heapq as hq
import sys
input = sys.stdin.readline
from bisect import bisect_left

def solution(info, query):
    answer = []
    data = {}
    def insert(d, arr, data):  # 중첩 딕셔너리
        if d == 4:
            data += [int(arr[d])]
            data.sort()
            return
        if arr[d] not in data:
            if d != 3: data[arr[d]] = {}
            else: data[arr[d]] = []   
        insert(d + 1, arr, data[arr[d]])
        
    def select(d, arr, data):  # 카운팅
        tmp = arr[d]
        cnt = 0
        if d == 4: return len(data) - bisect_left(data, int(tmp[0]))
        for s in tmp:
            if s in data:
                cnt += select(d + 1, arr, data[s])
        return cnt
    
    for dt in info:
        dt = dt.split(" ")
        insert(0, dt, data)
    
    opt = [['java', 'python', 'cpp'], ['backend', 'frontend'], ['junior', 'senior'], ['chicken', 'pizza']]
    for com in query:
        com = com.replace('and', '').split()
        idx = 0
        sel = []
        for tmp in com:
            if tmp == '-': sel.append(opt[idx])
            else: sel.append([tmp])
            idx += 1
        answer.append(select(0, sel, data))
                
    return answer

# 알고리즘 : 구현
'''
풀이 : 딕셔너리를 중첩해서 info의 내용을 data에 입력하고, query의 각 항목을 인덱스로 탐색한다.
중첩 딕셔너리를 만들 때, 만약 d가 4가되면 숫자를 입력 받고, 이분탐색을 위해 정렬해준다.
query에서 만약 '-'가 포함되어있다면, opt배열에서 해당 순서의 값을 전부 가져와 계산한다.
'''
