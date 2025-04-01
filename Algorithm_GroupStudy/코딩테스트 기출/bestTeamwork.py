# 최고의 팀워크

from collections import deque
from functools import cmp_to_key
import sys
input = sys.stdin.readline

n, k, m = map(int, input().split())
box = [0] + [tuple(map(int, input().split())) for _ in range(n)]
result = 0
for _ in range(k):
    que = deque([(0, 0, 0, 0)]) # 현재 인덱스, 가치, 무게, 쓴 박스
    max = [0, 0, 0] # 무게, 최고가치, 사용 보급품
    while que:
        now, val, gram, chk = que.popleft()
        flag = True
        for i in range(now + 1, len(box)):
            if gram + box[i][0] <= m:
                flag = False
                que.append((i, val + box[i][1], gram + box[i][0], chk | 1 << i))
        if flag and (max[1] < val or max[0] <= gram and max[1] == val):
            max = [gram, val, chk]
    
    result += max[1]
    tmp = []
    for i in range(1, len(box)):
        if 1 << i & max[2] == 0: 
            tmp.append(box[i])
    box = [0] + tmp
print(result)

# 예제 1
'''
입력
5 2 5
4 5
3 4
2 1
5 7
1 1
출력 : 13
'''

# 예제 2
'''
입력
10 3 7
4 5
3 4
2 1
5 7
1 1
7 8
8 6
3 3
4 3
5 4
출력 : 25
'''

# 알고리즘 : BFS + 비트마스킹
'''
풀이 : BFS를 통해 보급품을 하나씩 넣어보며 최대 무게 m을 넘지 않으면서 가치가 더 높을 때마다 max를 갱신한다.
문제에서 주어진 k가 최대 3이고, n과 m이 50을 넘지 않기 때문에 k회 반복하면서 사용한 박스들을 뺀다.

큐를 하나 만들고, 초기값으로 인덱스, 가치, 무게, 사용한 박스 정보를 모두 0으로한 임의의 시작값을 넣어 BFS를 수행한다.
중복된 박스를 사용하지 않기 위해 탐색할 때 현재 인덱스 + 1부터 마지막 인덱스까지를 범위로 두고 탐색한다.
만약 다음 인덱스(i)의 박스 무게 + 현재까지의 무게를 한 값이 무게 한도(m) 이하라면, 현재 값들에 해당 박스의 값을 추가하여 que에 새로 삽입한다.
삽입할 때, 이번에 박스를 넣었음을 표시하기위해 비트마스킹을 사용한다.
비트마스킹을 통해 해당 박스가 사용되었으면 해당 인덱스에 비트에 1로 체크시킨다.
이 때, 한번이라도 다음 박스를 추가했다면, flag를 false로 내린다.
for문을 1회 순회하고 나서 flag가 true면 더이상 박스를 넣을 수 없기 때문에 max에 더 높은 가치인지 확인해서 더 높은 가치의 조합으로 교체한다.

que의 내용을 모두 탐색했다면, result에 max에 저장된 가치를 추가한다.
임의 배열(tmp)를 하나 만들고, 비트마스킹한 결과값(max[2])을 검사하여 1로 체크된 인덱스의 박스를 제외한 박스들을 담는다.
box를 tmp로 갱신하여 이번에 담은 박스들을 제외시킨다.
위 과정들을 k회 반복한 후, result에 저장된 보급품 가치를 출력한다.
'''
