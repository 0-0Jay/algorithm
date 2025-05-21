# 백준 4587번 이집트 분수 : https://www.acmicpc.net/problem/4587

while True:
    m, n = map(int, input().split())
    if m == n == 0: break
    ans = []
    div = math.ceil(n / m)
    while m > 0:
        res_m : 1
        while True:
            tmpn, tmpm, tmpdiv = n, m, div
            while tmpn > 0:
                tmpdiv, tmpn = tmpn, tmpdiv % tmpn
            res = (n * div) // tmpdiv
            tmpm = m * (res // n) - (res // div)
            res_m = tmpm
            tmpres = res
            while tmpm > 0:
                tmpres, tmpm = tmpm, tmpres % tmpm
            res //= tmpres
            res_m //= tmpres
            if res < 1000000: break  
            div += 1
        m = res_m
        n = res
        ans.append(div)
        if m > 1: div = math.ceil(n / m)
        else: div = n
    print(*ans)

# 알고리즘 : 수학 + 구현 + GCD(유클리드 호제법)
'''
풀이 : 입력 받은 두 수에서 뺄 수 있는 가장 큰 단위분수를 빼고, 남은 값이 100만이 넘는지 검사한다.
가장 큰 단위 분수는 분모 / 분자 한 값을 math.ceil 함수로 1의 자리로 올린 값을 분모로 한 분수이다.
while문을 통해 위에서 구한 단위 분수를 빼보고 그 결과 분수의 분모가 100만이 넘으면 단위 분수의 분모에 1씩 더해본다.
만약 결과 값이 한번이라도 1000000보다 낮아지는 단위분수가 발견되면 break하고 분모와 분자를 갱신한다.
이를 남은 m의 값이 0이 될 때까지 반복한다.

이 때, 분수 간 뺄셈을 계산하기 위해 기존 분수와 단위 분수의 분모간 최소공배수를 구해주어야 한다.
이를 계산하기 위해 두 분모에 GCD 알고리즘(유클리드 호제법)을 사용하여 최대공약수를 먼저 구해준다.
두 분모를 곱한 값에 최대공약수를 나눈 몫이 최소공배수다.
'''
