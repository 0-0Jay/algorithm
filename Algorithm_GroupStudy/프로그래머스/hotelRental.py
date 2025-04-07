# 프로그래머스 - 호텔 대실 : https://school.programmers.co.kr/learn/courses/30/lessons/155651

def solution(book_time):
    chk = [0] * 1450
    answer = 0
    for i in range(len(book_time)):
        st = book_time[i][0]
        ed = book_time[i][1]
        chk[int(st[:2]) * 60 + int(st[3:])] += 1
        chk[int(ed[:2]) * 60 + int(ed[3:]) + 10] -= 1
    for i in range(1, len(chk)):
        chk[i] += chk[i - 1]
        if chk[i] > answer: answer = chk[i]
    return answer

# 알고리즘 : 스위핑
'''
풀이 : 00:00 부터 23:59까지를 분단위로 바꾸고, 시작 시각과 종료 시각에 각각 +1, -1을 체크 한뒤, 스위핑한다.
주어지는 시계열 자료를 분단위 숫자로 바꾸고, 인덱스로 사용한다.
24:00을 분단위로 바꾸면 24 * 60 = 1440이므로 그정도 크기의 chk배열을 생성한다.
book_time에서 시작 시각과 종료 시각을 하나씩 뽑고, 분단위로 변환한 후, 끝시간에만 10을 더한다.
각각을 인덱스로 하여 chk에 +1, -1 한다.
1번 인덱스부터 스위핑하며 chk[i]중 최대값을 찾아 반환한다.
'''
