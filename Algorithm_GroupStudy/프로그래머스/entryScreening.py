# 프로그래머스 - 입국심사 : https://school.programmers.co.kr/learn/courses/30/lessons/43238?language=python3#

def solution(n, times):
    l, r = 0, max(times) * n
        
    while l <= r:
        mid = (l + r) // 2
        tmp = 0
        for i in times:
            tmp += mid // i
        if tmp < n: l = mid + 1
        else: r = mid - 1
  
    return l

# 알고리즘 : 이분 탐색
'''
풀이 : 심사에 필요한 시간을 탐색값으로 잡고 이분탐색을 수행한다.
l은 0분, r은 times의 시간 중 가장 긴 시간 * n한 값으로 둔다.
mid 시간안에 n명의 사람을 모두 심사할 수 있다면(tmp), 더 작은 시간으로도 가능한지 r을 줄여서 탐색한다.
만약 tmp가 n보다 작으면, 시간이 너무 짧다는 의미이므로 l을 mid위로 올려서 탐색한다.
'''
