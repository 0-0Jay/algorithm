# SW expert 19118번 언덕길 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=5&contestProbId=AYxCewMqiqwDFASu&categoryId=AYxCewMqiqwDFASu&categoryType=CODE&problemTitle=%EC%96%B8%EB%8D%95%EA%B8%B8

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    arr = tuple(map(int, input().split()))
    LCS = [0]
    for i in arr:
        if LCS[-1] < i:
            LCS.append(i)
        else:
            l, r = 1, len(LCS) - 1
            while l < r:
                mid = (l + r) // 2
                if LCS[mid] < i: l = mid + 1
                else: r = mid
            LCS[l] = i
            
    print("#%d %d" %(test_case, n - len(LCS) + 1))

# 알고리즘 : LCS (가장 긴 증가하는 부분수열)
'''
풀이 : O(nlogn)으로 가장 긴 증가하는 부분수열의 길이를 구한 후, 전체 길이에서 빼준다.
각 테이스 케이스별로 가장 긴 증가하는 부분수열을 구한다. 
최소한의 집을 허물려면 높이 오름차순으로 가장 길게 만들 수 있는 집들을 제외한 나머지 집을 모두 허물면 된다.
이를 위해 LCS의 최대 길이를 구한다.
총 집의 갯수에서 LCS 만큼의 집을 제외한 나머지를 허물면 된다. 
'''
