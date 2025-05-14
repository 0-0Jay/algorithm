// 백준 7576번 - 토마토 : https://www.acmicpc.net/problem/7576

#include<stdio.h>
#include<algorithm>
#include<vector>
#define M 1001
using namespace std;

int map[M][M], que[M * M][2], st = -1, ed = -1, cnt, dx[4] = { 1, 0, -1, 0 }, dy[4] = { 0, 1, 0, -1 };

int main() {
	int n, m;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &map[j][i]);
			if (map[j][i] == 1) {
				que[++st][0] = j;
				que[st][1] = i;
			}
		}
	}
	while (st != ed) {
		int nowx = que[++ed][0];
		int nowy = que[ed][1];
		for (int i = 0; i < 4; i++) {
			int nx = nowx + dx[i];
			int ny = nowy + dy[i];
			if (nx >= 0 && nx < n && ny >= 0 && ny < m && map[nx][ny] == 0) {
				map[nx][ny] = map[nowx][nowy] + 1;
				que[++st][0] = nx;
				que[st][1] = ny;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (map[i][j] == 0) {
				printf("-1");
				return 0;
			}
			else if (map[i][j] > 0) {
				if (cnt < map[i][j]) cnt = map[i][j];
			}
		}
	}
	printf("%d", cnt - 1);
	return 0;
}

// 알고리즘 : BFS
/*
풀이 : BFS를 활용해 인접 4칸의 토마토로 뻗어나가며 익은토마토를 늘려간다.
익은 토마토를 전부 큐에 넣어 BFS를 수행한다.
만약 인접한 칸이 -1이라면 건너띈다.
-1이 아니라면 해당 칸에 익어진 날짜를 기록하고 큐에 칸의 좌표를 삽입한다.
익어진 날짜는 현재 큐에서 뽑은 날짜 +1을 기록한다.
이렇게하면 판에서 가장 큰 숫자가 곧 모든 토마토가 익는데 걸린 시간이 된다.

큐가 완전히 빌 때까지 반복 후, 전체 토마토 판을 탐색하여 안익은 토마토가 있는지 여부와 동시에 가장 큰 숫자를 찾아 cnt에 갱신한다.
0이 하나라도 있으면 토마토가 전부 익지 못했으므로 -1을 출력하고, 그렇지 않다면 cnt를 출력한다.
*/
