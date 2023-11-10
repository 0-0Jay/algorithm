# 백준 2473번 세 용액 : https://www.acmicpc.net/problem/2473

n = int(input())
arr = list(map(int, input().split()))
res = 1e12
tsum = []
ans = [0, 0, 0]

arr.sort()

for i in range(len(arr)):
    l, r = i + 1,n - 1 
    while l < r:
        tmp = arr[i] + arr[l] + arr[r]
        if abs(tmp) < res:
            res = abs(tmp)
            ans = [arr[i], arr[l], arr[r]]
        if tmp > 0: r -= 1
        else: l += 1
            
ans.sort()
for i in ans:
    print(i, end=" ")

# 알고리즘 : 투 포인터
'''
풀이 : 용액 하나를 잡고 나머지 용액들 중 두개를 골라서 더한 값의 절대값을 0에 가깝게 한다.
i번째 용액을 선택하고, i+1번째를 l, n번째를 r로 두고 투포인터로 탐색한다.
값이 0보다 커지면 r을, 0보다 작아지면 l을 이동시킨다.
매 이동마다 합의 절대값을 계산해서 ans와 res를 최신화 해준다.
'''
