# 프로그래머스 - 연속된 부분 수열의 합 : https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    tmp = sequence[0]
    answer = [1e12, 0, 0]
    flag = False
    chk = [0, 0]
    while True:
        if k < tmp:
            tmp -= sequence[chk[0]]
            chk[0] += 1
        elif k > tmp and chk[1] < len(sequence) - 1:
            chk[1] += 1
            tmp += sequence[chk[1]]
            if flag:
                tmp -= sequence[chk[0]]
                chk[0] += 1
        elif k == tmp and chk[1] - chk[0] < answer[0]:
            answer = [chk[1] - chk[0], chk[0], chk[1]]
            flag = True
            if chk[0] < chk[1]:
                tmp -= sequence[chk[0]]
                chk[0] += 1
        else: return answer[1:]

# 알고리즘 : 투포인터
'''
풀이 : 투포인터를 활용해 연속된 부분수열의 합이 K가 되는 지점을 찾고, 두 포인터의 거리를 줄여보면서 옮겨본다.
기존의 투포인터 탐색에서 flag를 사용해 더이상 거리가 멀어지는 경우를 배제한다.
우선 부분수열의 합을 계산할 변수(tmp)와 두개의 포인터를 저장할 배열(chk)을 만든다.

목표값(k)가 현재 합(tmp)보다 작으면, tmp에서 값을 빼야하기 때문에 tmp에서 왼쪽포인터의 값을 빼고 왼쪽 포인터를 한칸 오른쪽으로 옮긴다.
반대로, k가 현재 합보다 크면, tmp에 값을 더해줘야하기 때문에 tmp에서 오른쪽포인터를 한칸 오른쪽으로 옮기고 해당 위치의 값을 더한다.
k가 현재 합과 같으면, 두 포인터의 거리를 계산하고, answer[0]에 저장된 거리와 비교해 더 작을때만 answer를 [더 짧아진 거리, 왼쪽 포인터, 오른쪽 포인터]로 갱신한다.

이 때, answer가 한 번이라도 갱신되었다면 flag를 True로 전환시켜준다.
이 flag가 True가 되었다는 뜻은, 연속된 부분수열의 합이 k인 두 지점이 한번이라도 발견되었다는 뜻이다.
즉, flag가 True가 된 순간부터는 answer[0]에 저장된 거리 이상 떨어진 지점은 탐색할 필요가 없다는 뜻이다.
따라서 answer가 갱신한 후에 바로 tmp에서 sequence[chk[0]]값을 빼고 chk[0]에 1을 더해 두 포인터의 거리를 줄인다.
flag가 True가 되고 나서는 처음 k와 tmp의 값을 비교해 포인터를 조정하는 부분에도 변화가 필요하다.
k보다 tmp의 값이 더 커서 포인터의 간격을 줄이는 경우은 그대로 두어도 괜찮지만, k가 tmp보다 큰 경우는 두 포인터의 간격을 벌려선 안되기 때문에 두개의 포인터를 함께 1칸씩 오른쪽으로 옮겨주어야한다.

이 방식으로 chk[0]과 chk[1]이 마지막 숫자까지 도달했다면, answer에서 거리를 저장했던 0번 인덱스를 제외하고 answer를 반환시킨다.
'''
