# 프로그래머스 섬 연결하기 : https://school.programmers.co.kr/learn/courses/30/lessons/42861?language=python3#

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n + 1)]
    def find(parent, x):
        if parent[x] == x: return x
        parent[x] = find(parent, parent[x])
        return parent[x]

    costs.sort(key = lambda x : x[2])
    for a, b, c in costs:
        rootA = find(parent, a)
        rootB = find(parent, b)
        if rootA != rootB:
            parent[rootB] = rootA
            answer += c
    return answer

# 알고리즘 : 크루스칼 알고리즘
'''
풀이 : 모든 다리를 건설 비용을 기준으로 오름차순 정렬한 뒤, 가장 작은 비용부터 union/find를 통해 연결한다.
연결할 수 있는 가장 작은 다리부터 연결하는 것이 최소 비용을 만드는데 유리하다.
일반적인 크루스칼 알고리즘과 크게 다르지 않은 문제다.
'''
