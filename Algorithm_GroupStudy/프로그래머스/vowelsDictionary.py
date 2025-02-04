# 프로그래머스 - 모음사전 : https://school.programmers.co.kr/learn/courses/30/lessons/84512

lst = []
answer = 0
def solution(word):
    global lst, answer
    def DFS(w, goal):
        global lst, answer
        if w == goal: answer = len(lst)
        if len(w) == 5: return
        for i in ('A','E','I','O','U'):
            lst.append(w + i)
            DFS(w + i, goal)
    DFS("",word)
    return answer

# 알고리즘 : 완전탐색(DFS)
'''
풀이 : DFS로 'A'부터 차례대로 배열에 누적하며 word와 같아지는 순간을 찾는다.
단어를 계속 누적시킬 배열(lst)을 하나 만들고, 빈 문자열부터 시작해 DFS로 A, E, I, O, U를 하나씩 추가해가며 단어가 생성되는 족족 lst에 추가한다.
DFS 특성상 A 다음엔 AA, AA 다음엔 AAA가 들어가기때문에 문제에서 제시한 사전순대로 lst에 단어가 저장된다.
계속 단어를 쌓다가 word와 같아지는 순간 lst의 길이를 반환하면 해당 word가 사전에서 몇번째 단어인지 알 수 있다.
'''
