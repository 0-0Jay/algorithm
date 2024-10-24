# 백준 5670번 휴대폰 자판 : https://www.acmicpc.net/problem/5670

import sys
input = sys.stdin.readline

class Node:
    def __init__(self, now):
        self.now = now
        self.child = {}
        self.chk = False
        
class Trie:
    def __init__(self):
        self.parent = Node('')
    
    def add(self, word):
        node = self.parent
        for w in word:
            if w not in node.child:
                now = Node(w)
                node.child[w] = now
                node = now
            else:
                node = node.child[w]
        node.chk = True
        
    def find(self, word):
        cnt = 0
        node = self.parent
        for w in word:
            node = node.child[w]
            if len(node.child) > 1 or node.chk == True:
                cnt += 1
        return cnt

while True:
    try: n = int(input())
    except: break

    arr = []
    trie = Trie()
    for i in range(n):
        word = input().strip()
        arr.append(word)
        trie.add(word)
    res = 0
    for word in arr:
        res += trie.find(word)
    print('%.2f' %(res / n))

# 알고리즘 : 트라이
'''
풀이 : 트라이 자료구조와, 노드 클래스를 구현한다.
먼저 노드 클래스를 구현한다.
노드 클래스는 현재 문자(now), 현재 문자 뒤에 올 수 있는 문자들(child), 단어의 마지막 문자 여부(chk)의 필드를 갖는다.

다음으로 트라이 자료구조를 구현한다.
기본적으로 빈문자열을 루트로 갖게 생성자를 두고, 트라이에 값을 추가하는 메서드(add)와 값을 찾는 메서드(find)를 구현한다.
add 함수는 다음과 같이 동작한다.
1. 먼저 루트인 빈 문자열을 parent로 둔다.
2. 현재 문자를 Node화 하여 parent 문자의 child에 추가한다. 이 때, 현재 문자가 이미 parent에 있다면 추가하지 않는다.
3. 방금 문자를 parent로 갱신한다.
4. 2~3을 입력된 단어의 첫 문자부터 마지막 문자까지 반복한다.
5. 마지막 문자의 chk를 True로 바꿔준다.
이렇게 하면 후에 find 함수를 탐색할 때, chk 여부에따라 카운팅을 할지 안할지 결정할 수 있다.

find 함수는 원래 값을 찾는 용도지만, 현재 문제에서는 자판을 몇번 눌러야하는지를 요구하기 때문에, 요구에 맞게 구현한다.
1. 먼저 루트인 빈 문자열을 node로 둔다.
2. node의 child에서 현재 문자의 Node를 가져와 node를 갱신한다.
3. 만약 node의 자식이 1개 이상이거나, node가 마지막 문자가 아니라면, 1회 카운팅한다.(cnt)
4. 2~3을 입력된 단어의 첫 문자부터 마지막 문자까지 반복한다.
'''
