# 백준 1202번 보석 도둑 : https://www.acmicpc.net/problem/1202

import heapq as hq

n, k = map(int, input().split())
gewel = [list(map(int,input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]
sum = 0

bag.sort()
gewel.sort(key = lambda x : (x[0], x[1]))

tmp = []
k = 0

for i in range(len(bag)):
    while k < n and gewel[k][0] <= bag[i]:
        hq.heappush(tmp, -gewel[k][1])
        k += 1
    if tmp: sum += -hq.heappop(tmp)
    
print(sum)

# 알고리즘 : 힙, 그리디
'''
풀이 : 가방에 넣을 수 있는 가장 비싼 보석을 넣는다.
가방과 보석을 각각 가방크기, 보석무게로 오름차순 정렬한다.
가장 작은 가방부터 탐색해서 넣을 수 있는 가장 비싼 보석을 넣는게 가장 좋다고 판단하고 진행한다. (그리디)
힙에 현재 가방에 넣을 수 있는 보석을 전부 담는다.
보석이 현재 가방 크기보다 커지는 시점에 heap에서 pop해서 sum에 누적한다.
힙은 보석의 가격을 내림차순으로 삽입하기 때문에 pop하면 가장 비싼 보석이 나온다.
다음 가방은 지금까지 탐색했던 보석의 다음 보석(k)부터 힙에 담는다.
이러면 다음 가방은 이전 가방에 넣은 보석을 제외한 최대 가격이 담긴다.
'''
