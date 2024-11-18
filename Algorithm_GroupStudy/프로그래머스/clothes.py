# 프로그래머스 - 의상 : https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    wear = {}
    for name, part in clothes:
        if part not in wear: wear[part] = []
        wear[part].append(name)
    tmp = 1
    for k, v in wear.items():
        tmp *= len(v) + 1
    return tmp - 1

# 알고리즘 : 해싱, 수학
'''
풀이 : 의상의 종류를 키값으로 하여 의상의 이름을 분류한다.
의상을 분류할 딕셔너리(wear)를 만들고, clothes의 옷을 분류한다.

각 종류에서 1개씩 옷을 뽑거나 뽑지않았을 때의 가능한 경우의 수를 구하면된다.
wear에 분류된 옷들의 각 개수에 + 1한 값들의 곱을 구한다.
+1 하는 이유는 해당 종류의 옷을 입지않는 경우를 계산에 포함시키기 위해서다.
모두 곱한 후, 결과값에서 옷을 하나도 입지 않는 경우 1을 빼준 값을 반환한다.
'''
