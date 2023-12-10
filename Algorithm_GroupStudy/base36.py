# 백준 1036번 36진수 : https://www.acmicpc.net/problem/1036

import sys
input = sys.stdin.readline

n = int(input())
num = {}
result = 0

for i in range(n):
    word = input().strip()
    result += int(word, 36)
    sz = len(word)
    for idx in range(sz):
        if word[idx] not in num:
            num[word[idx]] = (int('Z', 36) - int(word[idx], 36)) * pow(36, sz - idx - 1)
        else: 
            num[word[idx]] += (int('Z', 36) - int(word[idx], 36)) * pow(36, sz - idx - 1)
        
t = int(input())  
num = sorted(num.values(), reverse=True)[:t]
result += sum(num)
    
tmp = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ans = ""
while result > 0:
    ans = tmp[result % 36] + ans
    result //= 36
      
print(ans if ans != '' else 0)
    
# 알고리즘 : 그리디 + 구현
'''
풀이 : Z로 변환했을 때 그 격차를 내림차순 정렬해서, k번째 숫자까지 Z로 변환시킨다.
단어를 입력받을 때마다 다음 두가지를 수행한다.
1. 그 단어를 10진수로 변환했을 때의 값을 result에 누적시킨다.
2. 딕셔너리의 단어의 각 자리 숫자 인덱스에 Z-(자리의 숫자) * 36^(자릿수)를 누적한다.
  2-1. Z로 변환했을 때의 그 격차를 10진수로 해당 숫자 인덱스에 기록해두는 과정이다.

모든 단어에 대한 계산이 끝났다면, 그 격차가 큰 순서대로 내림차순 정렬하고, 바꿀 문자 갯수(t)만큼 슬라이싱한다.
슬라이싱한 배열의 총합을 result에 더해준다.
Z로 변환했을 때의 격차를 저장해두었기 때문에 추가적인 계산을 할 필요 없이 격차만 더해주면 된다.

단, 위 코드는 result가 0보다 클때 while문이 동작하게 해두었기 때문에 만약 result가 0이라면 ans를 빈 문자열('')로 반환한다.
따라서 마지막 출력문에 if문으로 ans가 빈 문자열이라면 0을 출력하게 해주는 코드를 추가했다.
'''
