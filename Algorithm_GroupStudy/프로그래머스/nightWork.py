# 프로그래머스 야근 지수 : https://school.programmers.co.kr/learn/courses/30/lessons/12927

def solution(n, works):
    if sum(works) < n : return 0
    n = -n
    d = len(works)
    workingday = []
    job = 0
    
    for i in works:
        if i != 0:
            job += 1
            workingday.append(i)
            n += i
            
    workingday.sort()
    answer = 0
    
    for i in range(d):
        rem = n // job
        if workingday[i] > rem:
            answer += (rem ** 2)
            n -= rem
        else:
            answer += workingday[i] ** 2
            n -= workingday[i]
        job -= 1
    return answer

# 알고리즘 : 그리디
'''
풀이 : 남은 작업을 최대한 분산시킨다.
처음 입력된 일할 시간(n)을 음수로 전환하여 계산에 편리하게 한다.
남은 일의 작업량이 0이면 야근할 필요가 없으므로 계산에 포함하지 않는다.
남은 일이 있으면 일해야 하는 날(job)에 1을 추가하고, n에 작업 시간을 누적한다.

workingday 배열에도 작업 시간을 저장해두고, 오름차순 정렬한다. 
오름차순 정렬하는 이유는, 적은 작업량을 가진 날을 먼저 계산하기 때문에 남은 날 수에 따라 분배될 작업시간이 늘어나는 것을 고려하기 위해서다.
이는 앞서 작업량이 0이면 계산에 포함하지 않는 이유와 비슷하다. 
분배한 작업할 시간보다 남은 작업량이 적으면 굳이 더 일 할 필요 없다.
'''
