# 프로그래머스 2021 Dev-Matching:웹 백엔드 개발자(상반기) - 로또의 최고 순위와 최저 순위 : https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    wins = set(win_nums)
    rnum, fnum = 0, 0
    for i in lottos:
        if i in wins: rnum += 1
        elif i == 0: fnum += 1
    answer = [7 - (rnum + fnum) if (rnum + fnum) > 1 else 6, 7 - rnum if rnum > 1 else 6]
    return answer

# 알고리즘 : 구현
'''
풀이 : 중복된 숫자가 없기때문에 win_nums를 집합자료에 넣고, lottos의 숫자들을 탐색한다.
lottos의 숫자가 win_nums에 있으면 rnum을 1씩 올리고, 0이면 fnum을 1씩 올린다.
최고 등수와 최하 등수는 곧, rnum + fnum개의 숫자를 맞춘 등수와 rnum개의 숫자만 맞춘 등수와 같다.
'''
