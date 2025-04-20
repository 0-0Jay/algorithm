# 정올 - STL Queue : https://jungol.co.kr/problem/8074?cursor=OCwxLDY=

import sys
input = sys.stdin.readline

que = [0] * 10000
st, ed = 0, 0

n = int(input())
for _ in range(n):
    cmd = list(input().strip().split(" "))
    if cmd[0] == 'i':
        que[ed] = (cmd[1], cmd[2], cmd[3])
        ed += 1
    elif cmd[0] == 'o':
        if st >= ed: print("empty")
        else:
            print(*que[st])
            st += 1
    elif cmd[0] == 'z':
        if st >= ed or que[st][2] != cmd[1]: print("no")
        else: print("yes")
    elif cmd[0] == 'c':
        print(ed - st)

  # 알고리즘 : 큐
  '''
  풀이 : 큐를 직접 구현해본다.
  두 개의 키 st(front)와 ed(rear)를 사용하여 자료구조를 호출없이 구현한다.
  삽입 명령이 들어오면 que[st]에 입력된 값을 넣고 st를 한칸 올린다.
  인출 명령이 들어오면 que[ed]의 값을 출력하고 ed를 한칸 올린다. 단, ed와 st의 값이 같으면 빈 큐임으로 empty를 출력한다.
  z 명령이 들어오면 큐의 내용을 확인한다.
  c 명령이 들어오면 큐의 길이를 출력한다.

  z 명령의 경우, 구조체를 사용하기 위한 명령인데, 큐를 직접 구현하면 구조체를 사용하지 않고도 만들 수 있다.
  구조체를 사용하게 되더라도 튜플대신 구조체를 삽입하면 되기 때문에 차이는 없다.
  '''
