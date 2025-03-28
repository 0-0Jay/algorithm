# 프로그래머스 - 마법의 엘리베이터 : https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(storey):
    cnt = 0
    while storey > 0: 
        tmp = storey % 10
        cnt += 10 - tmp if tmp >= 5 else tmp
        storey //= 10
        if tmp == 5:
            storey += 1 if storey % 10 >= 5 else 0
        elif tmp > 5: storey += 1
    return cnt

# 알고리즘 : 그리디
'''
풀이 : 1의 자리부터 한자리씩 지워가며 카운팅한다.
storey가 0이 될 때까지 다음 과정을 반복한다.
1. storey의 1의자리 숫자를 가져온다(tmp)
2. tmp가 5 이상이면 10 - tmp를, 5 미만이면 tmp를 cnt에 누적한다.
3. storey를 10으로 나누어 1의 자리 숫자를 제거한다.(자릿수를 줄인다.)
4. tmp가 만약 5인 경우, 0으로 만들 때도 5회, 10으로 만들 때도 5회 버튼을 누르기 때문에 바로 위의 자릿수의 숫자를 확인한다.
  4-1. 만약 바로 위의 자릿수가 5이상이면, 1을 더하는 것이 10c 단위로 가는데 유리하므로 1을 더한다.
  4-2. 바로 위의 자릿수가 5미만이면, 내림하는 것이 유리하므로 더하지 않는다.
5. tmp가 만약 5보다 크면, 그냥 storey에 1을 추가한다.
이때, 1을 더하는 것은 현재 현재 숫자를 10으로 만들면 1의 올림수가 발생하는 것을 적용하는 것이다.
모든 카운팅이 끝났다면, cnt를 반환한다.
'''
