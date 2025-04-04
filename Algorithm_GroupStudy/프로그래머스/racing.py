# 프로그래머스 - 달리기 경주 : https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    answer = []
    rank = {"first" : ["",players[0]], players[0]: ["first", players[1]], players[-1] : [players[-2], False]}
    for i in range(1, len(players) - 1):
        rank[players[i]] = [players[i - 1], players[i + 1]]
      
    for i in range(len(callings)):
        now = callings[i]
        high = rank[now][0]
        rank[rank[high][0]][1] = now
        if rank[now][1]: rank[rank[now][1]][0] = high
        rank[high], rank[now] = [now, rank[now][1]], [rank[high][0], high]
        
    nx = rank["first"][1]
    while nx:
        answer.append(nx)
        nx = rank[nx][1]
    return answer

# 알고리즘 : 연결리스트
'''
풀이 : 딕셔너리에 각 인원별 [앞사람, 뒷사람] 쌍을 저장하고, 순위 변동이 발생할때마다 앞사람과 뒷사람을 변동한다.
순위 변동이 발생할때마다 배열을 슬라이싱하고 순위를 바꾸어 다시 합치는 방식은 굉장히 비효율적이다.
또한, callings에 인덱스가 아닌, 이름이 주어지기 때문에 해싱을 사용해야만 한다.
따라서 해싱을 사용 하되, 배열을 건드리지 않는 방법으로 [앞사람, 뒷사람] 쌍을 이용한다.

먼저 딕셔너리(rank)를 만들고 "first"키의 값에 현재 1등 인원을, 현재 꼴등 인원 키의 값에 [바로 앞 사람, False]를 저장한다.
이렇게 하면 후에 answer에 인원 순대로 값을 추가할때 무조건 first로 시작하여 False로 끝나게 하여 간단하게 로직을 짤 수 있다.
first에 현재 1등 인원을 넣었다면, 1등 인원 키의 값도 ["first", 다음 사람] 쌍을 저장한다.
만약 1등이 교체되는 경우, first에도 1등을 교체해주어야 하기때문이다.

rank에 [앞사람, 뒷사람] 쌍을 모두 저장했다면, callings를 하나씩 탐색한다.
현재 호명된 인원(now)을 뽑고, 추월할 앞사람(high)을 rank에서 찾는다.
now와 high의 위치가 바뀌기 때문에 high 앞사람의 뒷사람 정보를 now로 바꾼다.
마찬가지로 now 뒷사람의 앞사람 정보도 high로 바꿔주어야 한다.
ex) a -> b -> c -> d 의 경우 high는 b고 now는 c라고 가정하자.
    두 사람이 바뀌면 a의 뒷사람 정보를 b에서 c로, d의 앞사람 정보를 c에서 b로 바꿔야한다. a -> c -> b -> d
이 때, now가 꼴지였을 경우, 뒷사람이 존재하지 않으므로 꼴지가 아닐 때만 뒷사람 정보를 바꿔준다.
high의 앞사람과 now의 뒷사람에 대한 정보 갱신이 완료되었다면, 이제 high와 now의 정보를 갱신한다.
high의 앞사람이 now가 되고, 뒷사람은 now의 뒷사람이 된다.
now의 앞사람이 high의 앞사람이 되고, 뒷사람은 high가 된다.

모든 callings에 대한 정보 갱신이 완료되었다면,
rank["first"][1]의 인원을 뽑고(nx), answer에 차례차례 넣는다.
만약 nx가 False라면, 현재 뽑은 인원이 꼴지라는 뜻이므로 반복문을 중단한다.
반복문이 중단되면 answer를 반환한다.
'''
