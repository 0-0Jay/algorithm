// 백준 14503번 로봇 청소기 : https://www.acmicpc.net/problem/14503

#include<stdio.h>
#include<algorithm>
using namespace std;

int room[51][51], n, m, r, c, d, dl[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}}, cnt; // 북 동 남 서

void DFS(int x, int y, int d) {
	if (room[x][y] == 1) {
		printf("%d", cnt);
		exit(0);
	}
	room[x][y] = 2;
	for (int i = (d + 3) % 4, j = 0; j < 4; i = (i + 3) % 4, j++) {
		int a = x + dl[i][0];
		int b = y + dl[i][1];
		if (a > -1 && a < n && b > -1 && b < m && room[a][b] == 0) {  // 바로 90도 반시계 회전, 전진 가능한지 탐색
			cnt++;
			DFS(a, b, i);
		}
	}
	DFS(x - dl[d][0], y - dl[d][1], d);  // 360도 회전 후에도 진행을 못했으면 방향 그대로 후진
}

int main(){
	scanf("%d%d%d%d%d", &n, &m, &r, &c, &d);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &room[i][j]);
		}
	}
	cnt++;
	DFS(r, c, d);
}

// 알고리즘 : 구현(재귀함수 활용)
/*
풀이 : 재귀함수를 활용해서 조건에 맞추어 로봇청소기 이동
북, 동, 남, 서 방향으로 0~3이므로 변수(d)를 하나 선언해서 나머지계산으로 90도 회전 구현(시계방향은 +1, 반시계는 +3 하여 % 4)
문제에서 로봇 위치의 전후좌우 4방향중 어느 곳이든 청소하지 않은 공간이 존재하면 90도 회전부터 실행
예를들어 현재 로봇이 보고 있는 방향에 청소하지 않은 공간이 있어도, 전진이 아닌 90도 좌회전부터 수행한다는 의미
*/

