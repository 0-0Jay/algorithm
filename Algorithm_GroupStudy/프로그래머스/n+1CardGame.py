# 프로그래머스 2024 카카오 겨울 인턴십 - n + 1 카드게임 : https://school.programmers.co.kr/learn/courses/30/lessons/258707

def solution(coin, cards):
    answer = 0
    n = len(cards)
    now = n // 3
    n += 1
    arr = set(cards[:now])
    deck = set()

    tmp = set()
    for i in arr:  # arr 내의 카드에서 해결가능 한 경우
        if n - i in arr:
            tmp.add(i)
            tmp.add(n - i)

    answer += len(tmp) // 2
    arr -= tmp
    for i in range(answer):
        card1, card2 = cards[now : now + 2]
        now += 2
        deck.add(card1)
        deck.add(card2)

    while True:
        answer += 1
        if now == len(cards): break
        card1, card2 = cards[now : now + 2]
        now += 2
        deck.add(card1)
        deck.add(card2)
        turn = True
        if turn and coin > 0:
            for i in deck:
                if n - i in arr:
                    deck.remove(i)
                    arr.remove(n - i)
                    coin -= 1
                    turn = False
                    break
        if turn and coin > 1:
            for i in deck:
                if n - i in deck:
                    deck.remove(i)
                    deck.remove(n - i)
                    coin -= 2
                    turn = False
                    break
        if turn: break

    return answer

# 알고리즘 : 시뮬레이션(구현)
'''
풀이 : 처음 뽑은 카드와 턴 마다 뽑은카드를 집합을 활용해 매턴마다 기록하며 턴을 진행한다.
매턴마다 카드를 2장씩 뽑는데, 해당 카드가 초기 카드들(arr) 중 하나와 짝지어질 수도 있고, 앞으로 뽑힐 카드와 짝지어질 수도 있다.
이 경우의 수를 모두 탐색하는 것은 사실상 불가능하기 때문에 매턴 마다 뽑히는 카드를 deck에 기록만 해두고, 짝이 지어지면 반영한다.
즉, 뽑히는 카드들을 전부 deck에 넣고, arr과 deck에 있는 카드들 중 n + 1이 만들어지면 deck에서 뽑은 카드의 개수만큼 coin를 차감하는 것이다.

먼저, 처음 뽑은 카드들 중에서 뽑은 카드를 사용하지 않고도 n + 1을 만들 수도 있다.
임시 집합을 하나 만들고(tmp), arr에서 i를 뽑았을 때, n + 1 - i가 arr에 있다면 tmp에 해당 쌍을 추가한다.
tmp는 집합이기 때문에 (a, b)와 (b, a) 처럼 중복되는 경우 자동으로 걸러준다.
이렇게 뽑은 카드의 개수 // 2가 곧, 턴을 소모한 수다. 이를 answer에 추가해준다.

다음으로 뽑은 카드를 사용한 경우를 탐색한다.
while문을 무한반복을 걸어주고 turn 변수를 활용해 턴을 제어한다.
매 턴마다 새로운 카드 두장을 뽑아서 deck에 넣고, now를 2씩 올린다.
뽑은 카드를 사용하는 경우가 곧, 해당 카드를 손에 들어야 한다는 뜻이므로 남은 coin의 개수가 1개 이상인 경우부터 탐색한다.
deck에 있는 카드 1개와 arr에 있는 카드1개가 쌍을 이룰 수 있다면, coin을 1 차감하고, 카드를 갱신해준 다음, 턴을 종료한다.
뽑은 카드 1장을 사용하는 경우를 모두 탐색한 다음, 2장 모두 뽑은 카드에서 사용하는 경우를 탐색한다.
coin 개수가 2개이상일 경우, deck에있는 카드 2장으로 쌍을 만들 수 있다면 coin을 2 차감하고, 카드를 갱신하준 다음, 턴을 종료한다.
이 때, turn을 Ture로 두고, 턴을 수행할 때만 False로 바꿔주면서 탐색한다. 
만약 while문 내의 조건을 다 수행했는데도 True 라면 더이상 진행 할수 없다는 뜻이므로 while문을 종료한다.

모든 탐색이 끝났을 때, answer에 누적된 턴 수를 return 한다.
'''
