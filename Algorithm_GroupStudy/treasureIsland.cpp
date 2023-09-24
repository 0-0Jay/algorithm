// 백준 2589번 보물섬 : https://www.acmicpc.net/problem/2589

#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;

struct tmp {
	int x, y, d;
};

int n, m, dx[4] = { 1, 0, -1, 0 }, dy[4] = { 0, 1, 0, -1 }, maxlen, chk[51][51];
char map[51][51];

void BFS(int x, int y) {  // 각 지점 별 최장거리 위치 탐색 BFS
	queue<tmp> que;
	que.push({ x, y, 0 });
	while (!que.empty()) {
		tmp now = que.front();
		que.pop();
		if (now.d > maxlen) maxlen = now.d;
		for (int i = 0; i < 4; i++) {
			int nx = now.x + dx[i];
			int ny = now.y + dy[i];
			if (nx >= 0 && nx < n && ny >= 0 && ny < m && map[nx][ny] == 'L' && chk[nx][ny] == 0) {
				que.push({ nx, ny, now.d + 1 });
				chk[nx][ny] = 1;
			}
		}
	}
}

int main() {
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf(" %c", &map[i][j]);
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (map[i][j] == 'L') {
				fill(&chk[0][0], &chk[n][m], 0);
				chk[i][j] = 1;
				BFS(i, j);
				chk[i][j] = 0;
			}
		}
	}
	printf("%d", maxlen);
}

// 알고리즘 : BFS(너비 우선 탐색)
/*
풀이 : 맵전체의 시작점을 이중 for문으로 돌면서 각 시작점 별 최장거리 지점을 탐색하여 최대값 갱신
*/
