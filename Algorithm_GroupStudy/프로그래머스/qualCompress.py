# 프로그래머스 월간 코드 챌린지 시즌 1 - 쿼드압축 후 개수 세기 : https://school.programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    answer = [0, 0]
    def dac(arr, n):
        zero = 0
        one = 0
        for i in arr:
            zero += i.count(0)
            one += i.count(1)
        if zero == 0:
            answer[1] += 1
        elif one == 0:
            answer[0] += 1
        else:
            n //= 2
            dac([[arr[i][j] for j in range(n)] for i in range(n)], n)
            dac([[arr[i][j] for j in range(n, n * 2)] for i in range(n)], n)
            dac([[arr[i][j] for j in range(n)] for i in range(n, n * 2)], n)
            dac([[arr[i][j] for j in range(n, n * 2)] for i in range(n, n * 2)], n)
    dac(arr, len(arr))
    return answer

# 알고리즘 : 분할 정복
'''
풀이 : 재귀함수를 이용해 top-down 방식으로 배열을 쪼갠다.
1. 입력받은 배열에서 1의 개수와 0의 개수를 센다
2. 최종 결과(answer)에 1이 0개면 0의 수를 +1, 0이 0개면 1의 수를 +1한다.
3. 0과 1이 모두 존재하면, n // 2를 기준으로 4분할하여 재귀함수를 호출해 인수로 건내준다.
4. 1-3을 0 또는 1만 있는 2차원 배열이거나 1칸만 남을때까지 재귀호출 하며 answer에 값을 누적한다.
'''
