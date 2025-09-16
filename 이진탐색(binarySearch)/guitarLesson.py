# 백준 2343번 - 기타레슨 : https://www.acmicpc.net/problem/2343

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
l, r = 0, 0
for i in arr:
    l = max(i, l)
    r += i
ans = r

while l <= r:
    mid = (l + r) // 2
    cnt, tmp = 0, 0
    for i in arr:
        if tmp + i <= mid:
            tmp += i
        else:
            cnt += 1
            tmp = i
    cnt += 1
    # 블루레이 개수가 m보다 크면 크기 늘이기
    if cnt > m:
        l = mid + 1
    else:
        r = mid - 1
        ans = mid
        
print(ans)

# 알고리즘 : 이분 탐색
'''
풀이 : 블루레이의 갯수를 기준으로 이분탐색을 수행한다.
l은 각 영상중 가장 긴 것의 길이, r은 모든 영상 길이의 합으로 설정한다.
왜냐하면 가장 긴 영상보다 짧은 블루레이를 만들면 해당 영상은 어느 블루레이에도 속할 수 없기 때문이다.
r 역시 모든 영상의 길이 합보다 큰 블루레이는 쓸데없는 크기가 발생하므로 이렇게 설정한다.
mid 만큼의 블루레이에 각 영상을 넣고, 초과되면 cnt를 +1하고 새로운 블루레이에 영상을 넣는다.
cnt가 m보다 크다면, 블루레이 크기를 늘려서 더많은 영상을 하나의 블루레이에 담는다.
아니라면, ans에 mid를 갱신해주고 블루레이 크기를 줄여서 탐색해본다.
'''
