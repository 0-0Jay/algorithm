# 프로그래머스 - 바탕화면 정리 : https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    answer = [len(wallpaper), len(wallpaper[0]), 0, 0]

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                if i < answer[0]: answer[0] = i
                if i > answer[2]: answer[2] = i
                if j < answer[1]: answer[1] = j
                if j > answer[3]: answer[3] = j
    answer[2] += 1
    answer[3] += 1
    return answer

# 알고리즘 : x
'''
풀이 : wallpaper를 순회하면서 x의 최소값, 최대값과 y의 최소값, 최대값을 계산한다.
'''
