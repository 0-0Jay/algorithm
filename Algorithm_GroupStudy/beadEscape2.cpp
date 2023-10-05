// 백준 13460번 구슬 탈출 2 : https://www.acmicpc.net/problem/13460

#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;

struct tmp {
	int rx, ry, bx, by, cnt;
};

pair<int, int> hole;
int n, m, chk[10][10][10][10];
char box[10][10];
tmp ball;
queue<tmp> que;

int main(){
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf(" %c", &box[i][j]);
			if (box[i][j] == 'R') ball.rx = i, ball.ry = j;  // 빨간 구슬, 파란 구슬, 구멍의 위치 좌표 저장
			else if (box[i][j] == 'B') ball.bx = i, ball.by = j;
			else if (box[i][j] == 'O') hole.first = i, hole.second = j;
		}
	}
	chk[ball.rx][ball.ry][ball.bx][ball.by] = 1;
	que.push({ ball.rx, ball.ry, ball.bx, ball.by, 0 });
	while (!que.empty()) {  // BFS로 구슬 위치 탐색
		tmp now = que.front();
		que.pop();
		if (now.rx == 0 && now.ry == 0 && now.cnt <= 10) {  // 빨강 구슬이 빠졌고, 횟수가 10회 이하면 출력
			printf("%d", now.cnt);
			return 0;
		}

		// 오른쪽으로 기울이기
		if (now.ry < now.by) {  // 파란 구슬이 더 오른쪽에 있는 경우
			ball.bx = now.bx, ball.rx = now.rx;
			for (int i = now.by; box[now.bx][i] != '#'; i++) {
				ball.by = i;
				if (ball.by == hole.second && ball.bx == hole.first) {  // 공이 빠지면 좌표를 0, 0으로 저장
					ball.by = 0, ball.bx = 0;
					break;
				}
			}
			for (int i = now.ry; box[now.rx][i] != '#' && (i != ball.by || ball.rx != ball.bx); i++) {
				ball.ry = i;
				if (ball.ry == hole.second && ball.rx == hole.first) {
					ball.ry = 0, ball.rx = 0;
					break;
				}
			}
			ball.cnt = now.cnt + 1;
			if (chk[ball.rx][ball.ry][ball.bx][ball.by] == 0 && (ball.by != 0 || ball.bx != 0)) {  // 방문한 적이 없고, 파란 구슬이 빠지지 않았으면 큐에 삽입
				que.push(ball);
				chk[ball.rx][ball.ry][ball.bx][ball.by] = 1;
			}
		}
		else {   // 빨강 구슬이 더 오른쪽에 있는 경우
			ball.bx = now.bx, ball.rx = now.rx;
			for (int i = now.ry; box[now.rx][i] != '#'; i++) {
				ball.ry = i;
				if (ball.ry == hole.second && ball.rx == hole.first) {
					ball.ry = 0, ball.rx = 0;
					break;
				}
			}
			for (int i = now.by; box[now.bx][i] != '#' && (i != ball.ry || ball.bx != ball.rx); i++) {
				ball.by = i;
				if (ball.by == hole.second && ball.bx == hole.first) {
					ball.by = 0, ball.bx = 0;
					break;
				}
			}
			ball.cnt = now.cnt + 1;
			if (chk[ball.rx][ball.ry][ball.bx][ball.by] == 0 && (ball.by != 0 || ball.bx != 0)) {
				que.push(ball);
				chk[ball.rx][ball.ry][ball.bx][ball.by] = 1;
			}
		}

		// 왼쪽으로 기울이기
		if (now.ry > now.by) {  // 파란 구슬이 더 왼쪽에 있는 경우
			ball.bx = now.bx, ball.rx = now.rx;
			for (int i = now.by; box[now.bx][i] != '#'; i--) {
				ball.by = i;
				if (ball.by == hole.second && ball.bx == hole.first) {
					ball.by = 0, ball.bx = 0;
					break;
				}
			}
			for (int i = now.ry; box[now.rx][i] != '#' && (i != ball.by || ball.rx != ball.bx); i--) {
				ball.ry = i;
				if (ball.ry == hole.second && ball.rx == hole.first) {
					ball.ry = 0, ball.rx = 0;
					break;
				}
			}
			ball.cnt = now.cnt + 1;
			if (chk[ball.rx][ball.ry][ball.bx][ball.by] == 0 && (ball.by != 0 || ball.bx != 0)) {
				que.push(ball);
				chk[ball.rx][ball.ry][ball.bx][ball.by] = 1;
			}
		}
		else {   // 빨강 구슬이 더 왼쪽에 있는 경우
			ball.bx = now.bx, ball.rx = now.rx;
			for (int i = now.ry; box[now.rx][i] != '#'; i--) {
				ball.ry = i;
				if (ball.ry == hole.second && ball.rx == hole.first) {
					ball.ry = 0, ball.rx = 0;
					break;
				}
			}
			for (int i = now.by; box[now.bx][i] != '#' && (i != ball.ry || ball.bx != ball.rx); i--) {
				ball.by = i;
				if (ball.by == hole.second && ball.bx == hole.first) {
					ball.by = 0, ball.bx = 0;
					break;
				}
			}
			ball.cnt = now.cnt + 1;
			if (chk[ball.rx][ball.ry][ball.bx][ball.by] == 0 && (ball.by != 0 || ball.bx != 0)) {
				que.push(ball);
				chk[ball.rx][ball.ry][ball.bx][ball.by] = 1;
			}
		}

		// 위쪽으로 기울이기
		if (now.rx > now.bx) {  // 파란 구슬이 더 위쪽에 있는 경우
			ball.by = now.by, ball.ry = now.ry;
			for (int i = now.bx; box[i][now.by] != '#'; i--) {
				ball.bx = i;
				if (ball.bx == hole.first && ball.by == hole.second) {
					ball.bx = 0, ball.by = 0;
					break;
				}
			}
			for (int i = now.rx; box[i][now.ry] != '#' && (i != ball.bx || ball.ry != ball.by); i--) {
				ball.rx = i;
				if (ball.rx == hole.first && ball.ry == hole.second) {
					ball.rx = 0, ball.ry = 0;
					break;
				}
			}
			ball.cnt = now.cnt + 1;
			if (chk[ball.rx][ball.ry][ball.bx][ball.by] == 0 && (ball.by != 0 || ball.bx != 0)) {
				que.push(ball);
				chk[ball.rx][ball.ry][ball.bx][ball.by] = 1;
			}
		}
		else {   // 빨강 구슬이 더 위쪽에 있는 경우
			ball.by = now.by, ball.ry = now.ry;
			for (int i = now.rx; box[i][now.ry] != '#'; i--) {
				ball.rx = i;
				if (ball.rx == hole.first && ball.ry == hole.second) {
					ball.rx = 0, ball.ry = 0;
					break;
				}
			}
			for (int i = now.bx; box[i][now.by] != '#' && (i != ball.rx || ball.by != ball.ry); i--) {
				ball.bx = i;
				if (ball.bx == hole.first && ball.by == hole.second) {
					ball.bx = 0, ball.by = 0;
					break;
				}
			}
			ball.cnt = now.cnt + 1;
			if (chk[ball.rx][ball.ry][ball.bx][ball.by] == 0 && (ball.by != 0 || ball.bx != 0)) {
				que.push(ball);
				chk[ball.rx][ball.ry][ball.bx][ball.by] = 1;
			}
		}

		// 아래로 기울이기
		if (now.rx < now.bx) {  // 파란 구슬이 더 아래쪽에 있는 경우
			ball.by = now.by, ball.ry = now.ry;
			for (int i = now.bx; box[i][now.by] != '#'; i++) {
				ball.bx = i;
				if (ball.bx == hole.first && ball.by == hole.second) {
					ball.bx = 0, ball.by = 0;
					break;
				}
			}
			for (int i = now.rx; box[i][now.ry] != '#' && (i != ball.bx || ball.ry != ball.by); i++) {
				ball.rx = i;
				if (ball.rx == hole.first && ball.ry == hole.second) {
					ball.rx = 0, ball.ry = 0;
					break;
				}
			}
			ball.cnt = now.cnt + 1;
			if (chk[ball.rx][ball.ry][ball.bx][ball.by] == 0 && (ball.by != 0 || ball.bx != 0)) {
				que.push(ball);
				chk[ball.rx][ball.ry][ball.bx][ball.by] = 1;
			}
		}
		else {   // 빨강 구슬이 더 아래쪽에 있는 경우
			ball.by = now.by, ball.ry = now.ry;
			for (int i = now.rx; box[i][now.ry] != '#'; i++) {
				ball.rx = i;
				if (ball.rx == hole.first && ball.ry == hole.second) {
					ball.rx = 0, ball.ry = 0;
					break;
				}
			}
			for (int i = now.bx; box[i][now.by] != '#' && (i != ball.rx || ball.by != ball.ry); i++) {
				ball.bx = i;
				if (ball.bx == hole.first && ball.by == hole.second) {
					ball.bx = 0, ball.by = 0;
					break;
				}
			}
			ball.cnt = now.cnt + 1;
			if (chk[ball.rx][ball.ry][ball.bx][ball.by] == 0 && (ball.by != 0 || ball.bx != 0)) {
				que.push(ball);
				chk[ball.rx][ball.ry][ball.bx][ball.by] = 1;
			}
		}
	}
	printf("-1");
}

// 알고리즘 : BFS (너비 우선 탐색), 구현
/*
풀이 : 빨간 구슬과 파란 구슬의 위치 정보를 하나의 경우로 두고 탐색을 수행한다.
좌우로 기울이는 경우, 상하좌표는 고정하고 좌우만 움직인다.
이 때, 각 구슬의 좌우좌표를 비교하여 기울이는 방향에 더 가까운 구슬부터 움직여야 한다.
이는 상하로 기울이는 경우에도 동일하다
상하로 기울이는 경우, 좌우좌표는 고정하고 상하만 움직이며, 각 구슬의 상하좌표를 비교한다.
위 풀이에서 (ball.by != 0 || ball.bx != 0) 조건일때만 큐에 삽입하기 때문에 파란 구슬이 빠지는 경우는 큐에 삽입되지 않는다.
즉, 큐를 마지막까지 탐색했을 경우, 파란 구슬이 빠지지 않았음에도 빨간 구슬이 빠지지 않았다면 -1을 출력하게 된다.
만약 큐를 모두 탐색하지 않았는데 빨간 구슬이 빠졌다면, 해당 경우의 cnt를 보고 10 이하이면 출력하고, 10보다 크면 아래 조건들에 의해 자연스레 큐에서 빠진다.

상하좌우(4) * 좌표비교(2)의 총 8가지 경우를 모두 BFS로 탐색해야 하는 문제다.
*/
