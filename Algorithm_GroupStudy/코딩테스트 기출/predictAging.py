# 노후화 예측하기

import sys
input = sys.stdin.readline

n, q, k = map(int, input().split())
lst = list(map(int, input().split()))
frq = [0] * (lst[-1] + 2)

for _ in range(q):
    s, e = map(int, input().split())
    frq[s] += 1
    if e + 1 <lst[-1]: frq[e + 1] -= 1

key = 0
result = []
for i in range(1, lst[-1] + 1):
    frq[i] += frq[i - 1]
    if i == lst[key]:
        result.append((frq[i], lst[key]))
        key += 1
result.sort(reverse=True)
print(result[k][1])

# 예제 1
'''
입력
6 5 2
3 7 10 13 17 20
1 10
3 9
4 23
12 19
3 15
출력 : 10
'''

# 예제 2
'''
입력
10 6 0
1 5 10 20 29 40 55 64 71 79
7 60
20 77
1 21
5 55
10 71
22 27
출력 : 20
'''

# 알고리즘 : 스위핑
'''
풀이 : 빈도수를 체크할 배열(frq)을 만들고, 각 제품의 범위의 시작(s)에 +1, 끝(e + 1)에 -1을 메모해둔 뒤, 한번에 계산한다.
매 범위마다 반복문을 통해 해당 범위에 +1을 해주는 방식을 사용하면 최악의 경우 10^9의 범위를 제곱으로 탐색하게 된다.
따라서 스위핑 기법을 응용하여 사용 빈도를 체크한다.

설비에 대한 정보만 있으면 되기 때문에 설비 번호 중, 가장 큰 값(오름차순으로 주어지기 때문에 마지막 인덱스의 값)만큼만 frq를 선언한다.
이 후, s와 e를 입력받을 때마다 s에 +1을, e+1에 -1을 저장하여 e까지만 +1이 적용되게 저장해둔다.
q개의 모든 입력을 받았다면, frq를 0번인덱스부터 마지막 인덱스까지 1회 순회하며 누적합을 구한다.
누적합을 구하며 각 설비 번호에 해당하는 인덱스가 나오면, 그 인덱스의 (누적합, 설비번호) 쌍을 result 배열에 저장한다.
이렇게하면 처음 입력된 설비번호와 그 설비가 사용 횟수가 result에 저장된다.
result를 내림차순 정렬하고 result[k][1]을 출력하면, 인덱스 특성상 k + 1번째로 폐기될 설비의 번호가 출력된다.
'''
