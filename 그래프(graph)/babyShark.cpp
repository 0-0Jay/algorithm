// 백준 16236번 아기상어 : https://www.acmicpc.net/problem/16236

#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;

struct qtmp { int x, y, d; };
struct pqtmp { 
	int x, y;
	bool operator<(const pqtmp& t) const {
		if (x != t.x) {
			return x > t.x;
		}
		return y > t.y;
	}
};

queue<qtmp> que;
priority_queue<pqtmp> pq;
int n, map[21][21], eat, shark = 2, fish, cnt, sx, sy, flag, chk[21][21], hit,
dx[4] = { 0, 1, 0, -1 }, dy[4] = { 1, 0, -1, 0 };

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &map[i][j]);
			if (map[i][j] > 0 && map[i][j] < 7) fish++;
			if (map[i][j] == 9) {
				sx = i; sy = j;
				map[i][j] = 0;
			}
		}
	}
	while (fish > 0) {
		// 큐, 체크, 힙 초기화
		flag++;
		hit = 500;
		que = queue<qtmp>();
		pq = priority_queue<pqtmp>();
		// 현재 위치로 부터 탐색 시작
		que.push({ sx, sy, 0 });
		chk[sx][sy] = flag;
		while (!que.empty()) {
			qtmp now = que.front();
			que.pop();
			if (now.d > hit) break;  // 이전 hit보다 거리가 멀면 break
			if (map[now.x][now.y] > 0 && map[now.x][now.y] < shark) {  // 먹을 수 있으면 hit
				hit = now.d;
				pq.push({now.x, now.y});
				continue;
			}
			for (int i = 0; i < 4; i++) {
				int nx = now.x + dx[i];
				int ny = now.y + dy[i];
        // 범위 안이고, 방문하지 않았고, 상어의 크기 이하면
				if (nx >= 0 && nx < n && ny >= 0 && ny < n && chk[nx][ny] != flag && map[nx][ny] <= shark) {
					chk[nx][ny] = flag;
					que.push({ nx, ny, now.d + 1 });
				}
			}
		}
		if (hit < 500) {  // 한번이라도 hit가 발생했으면
			sx = pq.top().x;
			sy = pq.top().y;  // 상어 위치 최신화
			fish--;  // 남은 물고기 감소
			cnt += hit;  // 이동시간 최신화
			map[sx][sy] = 0;  // 먹은 물고기 0으로 초기화
			eat++;  // 먹은 횟수 1 추가
			if (eat == shark) {  // 상어 크기만큼 먹었으면
				eat = 0; // eat 초기화
				shark++;  // 상어크기 1 추가
			}
		}
		else {  // hit가 발생하지 않았으면 while문 break
			break;
		}
	}
	printf("%d", cnt);  // 이동횟수 출력
}

// 알고리즘 : BFS + 구현
/*
풀이 : 현재 상어의 위치에서 BFS를 탐색하여 가장 가까운 먹이를 먹고, 상어의 위치를 최신화 한다.
매 탐색마다 이동시간, 먹은 먹이, 크기를 계산한다.

1. 상어의 위치에서 BFS를 수행하여 현재 상어의 크기보다 작은 곳을 탐색한다.
2. 작은 곳이 발견되면 hit을 해당 좌표까지의 거리로 변경한다.
3. 거리가 hit인 먹이들을 priority_queue(이하 pq)에 넣는다.
  3-1. 정렬 조건은 문제에서 제시한 높은 것 우선, 높이가 같다면 왼쪽 우선이다.
4. hit가 발생했다면, pq에서 pop한 좌표로 상어를 이동하고, 먹은 횟수 +1, 이동시간 + hit, 물고기수 -1한다.
5. 만약 먹은횟수가 상어크기와 같으면 상어 크기를 올리고 먹은 횟수를 0으로 초기화 한다.
6. 1 ~ 5를 hit가 발생하지 않을 때까지 반복한다.
7. while문 탐색이 끝났으면 누적된 이동시간을 출력한다.
*/
