# 프로그래머스 - 기사단원의 무기 : https://school.programmers.co.kr/learn/courses/30/lessons/136798

def solution(number, limit, power):
    cnt = [0] * (number + 1)
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            cnt[j] += 1
    answer = 0
    for i in range(1, number + 1):
        if cnt[i] <= limit: answer += cnt[i]
        else: answer += power
    return answer

# 알고리즘 : 완전탐색
'''
풀이 : 이중반복문으로 약수의 개수를 카운팅한다.
배열(cnt)을 하나 생성하여 약수의 개수를 센다.
1부터 해당수의 배수에 해당하는 인덱스에 1씩 누적시키는 방법을 사용한다.
cnt를 1부터 탐색하여, 만약 해당 숫자의 약수의 개수가 limit보다 높다면 power를, 아니면 cnt[i]를 answer에 누적한다.
'''
