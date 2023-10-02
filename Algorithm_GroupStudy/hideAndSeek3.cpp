// 백준 13549번 숨바꼭질 3 : https://www.acmicpc.net/problem/13549

#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <queue>
using namespace std;

#define p pair<int,int>

int n, k, chk[200001];
queue<p> que;

int main() {
	scanf("%d %d", &n, &k);
	que.push({ n, 0 });
	chk[n] = 1;
	while (!que.empty()) {
		p now = que.front();
		que.pop();
		if (now.first == k) {
			printf("%d", now.second);
            return 0;
		}
		if (now.first < 100000 && chk[now.first * 2] != 1) {  // *2로 순간이동 하는 경우
			que.push({ now.first * 2, now.second });
			chk[now.first * 2] = 1;
		}
		if (now.first > 0 && chk[now.first - 1] != 1) {  // -1로 이동하는 경우
			que.push({ now.first - 1, now.second + 1 });
			chk[now.first - 1] = 1;
		}
		if (now.first < 100000 && chk[now.first + 1] != 1) {  // +1로 이동하는 경우
			que.push({ now.first + 1, now.second + 1 });
			chk[now.first - 1] = 1;
		}
	}
}

// 알고리즘 : BFS(너비 우선 탐색)
/*
풀이 : 전형적인 BFS로 해결한다.
각각 *2로 순간이동하는 경우(+0초), +1로 이동하는 경우(+1초), -1로 이동하는 경우(-1초)를 큐에 넣는다.
단, 이동할 공간이 한번도 방문한 적이 없거나, 범위 내에 존재할 경우에만 push한다.

주의할 점은 큐에 넣을때 반드시 *2로 순간이동 하는 경우를 가장 먼저 계산해서 삽입한다.
위의 경우는 걸리는 시간에 변화가 없기 때문에 먼저 삽입하여 중복계산을 방지해주면 최단 시간 계산을 따로 해주지 않아도 된다.
어떠한 경우에도 순간이동을 가장 많이 사용한 카운트가 먼저 chk에 체크되고, 나올때도 가장 먼저 pop될 것이기 때문이다.
*/
