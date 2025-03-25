# 2024 네이버 신입 공채 - 서버찾기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def solution(delays, limits):
    result = [0, 0]
    limits[1] *= 1000
    for i in range(len(delays[0])):
        tmp = []
        for j in range(len(delays)):
            tmp.append(delays[j][i])
        tmp.sort()
        l, max_cnt = 0, 1
        for j in range(1, len(tmp)):
            if tmp[l] * limits[0] > tmp[j] and tmp[l] + limits[1] > tmp[j]:
                max_cnt = max(j - l + 1, max_cnt)
            else:
                while tmp[l] * 2 <= tmp[j] or l < j and tmp[l] + limits[1] <= tmp[j]:
                    l += 1
        if max_cnt > result[0]:
            result[0] = max_cnt
            result[1] = i + 1
                
    return result

# 예제 1
print(solution([[2423, 10], [3423, 30], [1, 40], [450, 50], [1200, 60], [2781, 100]], [2, 1])) # [3, 2]
# 예제 2
print(solution([[10, 50000, 100], [1, 100000, 1100], [51, 100000, 2100], [90, 100000, 3100], [73, 50000, 4100]], [10, 4])) # [4, 1]

# 알고리즘 : 시뮬레이션, 정렬, 투포인터
'''
풀이 : 서버별로 각 인원의 딜레이를 모아 정렬한 후, 투포인터를 응용하여 limits의 조건을 적용한 왼쪽 포인터를 오른쪽 포인터와 비교한다.
모든 서버에 대해 다음 과정을 반복한다.
1. 현재 서버의 인원 별 딜레이를 모아 정렬한다.
2. 가장 작은 딜레이를 선택할 포인터(l)와 가장 큰 딜레이를 선택할포인터(j)를 둔다.
3. j를 하나씩 오른쪽으로 옮겨가며 l에 limits[0]을 곱한값보다 작고, l에 limits[1]을 더한 값보다 작은지 검사한다.
4. 3번이 참이면 j만 한칸 옮기고, 현재 l과 j의 간격을 max_cnt와 비교해 더 긴 간격으로 갱신한다.
5. 3번이 거짓이면 3번 조건이 참일때 까지 l을 1씩 더한다.
6. 1~5번과정을 마지막 인원까지 수행했으면, max_cnt와 result[0]을 비교한다. 더 클 경우 result를 [max_cnt, 현재 서버(i + 1)]로 교체한다.

모든 서버에 대한 탐색이 끝났으면, result를 반환한다.
'''
