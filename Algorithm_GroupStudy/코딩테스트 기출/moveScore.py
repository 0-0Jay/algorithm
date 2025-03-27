# 점수 옮기기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def solution(cap, k, score, m):
    result = 0
    tmp = 0
    chk = 0
    for i in range(m - 1, len(score)):
        if score[i] > k: 
            tmp += score[i] - k
            result += 1
        elif score[i] < k: chk += k - score[i]
    if tmp > chk: return -1
    for i in range(len(score) - 1, m - 1, -1):
        tmp -= k - score[i]
        result += 1
        if tmp <= 0: break
        
    return result

# 예제 1
print(solution(100, 70, [95, 90, 80, 80, 80, 70, 70, 30, 10], 4)) # 3
# 예제 2
print(solution(100, 82, [100, 97, 97, 92, 87, 77, 77, 72, 72], 4)) # 4 
# 예제 3
print(solution(2000, 1998, [2000, 2000, 2000, 2000, 1999], 5)) # -1

# 알고리즘 : 시뮬레이션
'''
풀이 : 위에서 빼야할 점수의 개수와 아래에 더할 수 있는 점수의 개수를 구해 비교한다.
가장 적은 수의 인원만 영향을 주고 싶다면 가장 점수가 낮은 사람부터 점수를 채우면 된다.
score는 내림차순으로 정렬되어 주어지기 때문에  m등을 확인하기 위해 m - 1번 인덱스의 점수부터 확인한다.
만약 score[i]가 내 점수(k)보다 크다면, 해당 인원의 점수를 내 점수까지 낮추어야 내가 m등 안에 들 수 있다.
따라서 내려야할 점수 합(tmp)에 score[i] - k한 값을 누적하며 반드시 내려야하는 인원이기 때문에 영향을 줄 인원 수(result)에 1씩 누적한다.
내점수가 score[i]보다 크다면, 해당 인원의 점수가 내 점수를 넘을 경우 내 순위가 내려가므로 올릴 수 있는 점수 합(chk)에 k - score[i]를 누적한다.

m - 1번 인덱스부터 마지막 인덱스까지 계산하고 나면, tmp와 chk를 비교한다.
내려야할 점수(tmp)보다 올릴 수 있는 점수(chk)가 낮으면, 나보다 위에 있는 점수를 아무리 내려도 나는 m등안에 들 수 없다. 즉 -1을 반환한다.
tmp가 chk보다 작으면, 가장 마지막 인덱스부터 k-socre[i]의 값을 tmp에서 빼서 채운다.
이 때, 한명을 채울 때마다 result에 1씩 누적한다.
만약 tmp가 0 이하라면, 점수 분배가 끝난 것이므로 break로 중단한 후, result를 반환한다.
'''
