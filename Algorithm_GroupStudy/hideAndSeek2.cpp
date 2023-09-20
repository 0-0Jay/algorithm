// 백준 12851번 숨바꼭질 2 : https://www.acmicpc.net/problem/12851

#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;

struct tmp {
	int x, cnt;
};

int n, k, sh = 200001, cnt, chk[200001];
queue<tmp> que;

int main() {
	scanf("%d%d", &n, &k);
	if (n == k) {
		sh = 1;
	}
	que.push({ n, 1 });
	chk[n] = 1;
	while (!que.empty()) {
		tmp now = que.front();
		que.pop();

		if (now.x == k && now.cnt == sh) cnt++;

		if (now.x + 1 <= 200000 && now.cnt + 1 <= sh && (chk[now.x + 1] == 0 || now.cnt <= chk[now.x + 1])) {
			if (now.x + 1 == k) sh = now.cnt + 1;
			que.push({ now.x + 1, now.cnt + 1 });
			chk[now.x + 1] = now.cnt;
		}
		if (now.x - 1 >= 0 && now.cnt + 1 <= sh && (chk[now.x - 1] == 0 || now.cnt <= chk[now.x - 1])) {
			if (now.x - 1 == k) sh = now.cnt + 1;
			que.push({ now.x - 1, now.cnt + 1 });
			chk[now.x - 1] = now.cnt;
		}
		if (now.x * 2 <= 200000 && now.cnt + 1 <= sh && (chk[now.x * 2] == 0 || now.cnt <= chk[now.x * 2])) {
			if (now.x * 2 == k) sh = now.cnt + 1;
			que.push({ now.x * 2, now.cnt + 1 });
			chk[now.x * 2] = now.cnt;
		}
	}
	printf("%d\n%d", sh - 1, cnt);
}

// 알고리즘 : BFS(너비 우선 탐색)
/*
풀이 : 이동횟수를 활용한 방문체크를 해서 메모리 사용을 최소화 한다.

큐에 값을 넣을 때, 다음 3가지를 확인했다.
1. x + 1이 허용범위 내에 존재한다.
2. 현재 이동 횟수가 도착지점에 저장된 최소 이동 횟수보다 작다
3. 현재 이동 횟수가 현재 지점의 최소 이동 횟수 보다 작다.

2번의 경우 이미 도착한 경우가 존재하고, 해당 지점까지 이동횟수가 3일경우 3회 이상 이동하는 모든 경우는 무시하기 위함이다.
3번의 경우 4회만에 5에 도착을 했지만, 5에 이동횟수에 3이 있는 경우 이후 어떤 경우라도 3회만에 도착한 경우가 더 짧을 것이기 때문이다.

방문체크를 이렇게 섬세하게 하는 이유는 다음과 같다.
1. 단순히 0과 1로 방문체크를 할경우,  5에 3회만에 도착하는 경우가 여러번 있어도 1회밖에 카운팅 되지 않는다.
2. 1번의 이유로 방문체크를 하지 않을 경우 +1와 -1의 반복으로 인해 허용 메모리가 초과된다.
*/
