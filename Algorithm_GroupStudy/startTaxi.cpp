// 백준 19238번 스타트 택시 : https://www.acmicpc.net/problem/19238
// !!! 아직 통과하지 못한 코드. 재작성 필수 !!!

#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;

struct tmp {
	int x, y, d;

};

struct p_tmp {
	int x, y;

	bool operator<(const p_tmp t) const {
		if (x < t.x) return true;
		else if (y < t.y) return true;
		return false;
	}
};

int map[21][21], n, m, f, sx, sy, chk[21][21], hit = 500, flag = 1, drive[21][21], use, arrive,
dx[4] = { 1, 0, -1, 0 }, dy[4] = { 0, 1, 0, -1 };
queue<tmp> que;
priority_queue<p_tmp> pq;

int main() {
	scanf("%d%d%d", &n, &m, &f);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			scanf("%d", &map[i][j]);
		}
	}
	scanf("%d%d", &sx, &sy);
	while (m > 0) {
		chk[sx][sy] = flag;
		que = queue<tmp>();
		pq = priority_queue<p_tmp>();
		que.push({ sx, sy, 0 });
		for (int i = 0; i < 3; i++) {
			int a, b, a2, b2, line = 10;
			scanf("%d%d%d%d", &a, &b, &a2, &b2);
			map[a][b] = line;  // 사람은 line
			map[a2][b2] = -line;  // 목적지는 -line
			line++;
		}
		while (!que.empty()) {  // 가장 가깝고 같은 거리에 위치한 사람
			tmp now = que.front();
			que.pop();
			if (now.d >= f) break;
			if (now.d == hit) break;  // now가 hit 거리면 탐색 중단
			for (int i = 0; i < 4; i++) {
				int a = now.x + dx[i];
				int b = now.y + dy[i];
				if (a > 0 && a <= n && b > 0 && b <= n && chk[a][b] != flag && map[a][b] == 0) {
					if (map[a][b] > 10) {
						pq.push({a, b});
						hit = now.d + 1;
					}
					que.push({a, b, now.d + 1});
					chk[a][b] = flag;
				}
			}
		}
		f -= hit;
		if (pq.empty()) {  // 사람이 없으면 -1
			printf("-1");
			return 0;
		}

		p_tmp cl = pq.top();
		int fin = -map[cl.x][cl.y];
		map[cl.x][cl.y] = 0;
		sx = cl.x, sy = cl.y;
		que.push({sx, sy, 0});
		drive[sx][sy] = flag;
		while (!que.empty()) {
			tmp now = que.front();
			que.pop();
			if (now.d >= f) break;
			if (map[now.x][now.y] == fin) {
				arrive = 1;
				f += now.d;
				sx = now.x;
				sy = now.y;
				break;
			}
			for (int i = 0; i < 4; i++) {
				int a = now.x + dx[i];
				int b = now.y + dy[i];
				if (a > 0 && a <= n && b > 0 && b <= n && drive[a][b] != flag && map[a][b] == 0) {
					if (map[a][b] > 10) {
						pq.push({ a, b });
						hit = now.d + 1;
					}
					que.push({ a, b, now.d + 1 });
					drive[a][b] = flag;
				}
			}
		}
		if (arrive == 0) {
			printf("-1");
			return 0;
		}
		flag++;
		m--;
		arrive = 0;
	}
	printf("%d", f);
}
