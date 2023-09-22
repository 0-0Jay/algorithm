// 백준 19238번 스타트 택시 : https://www.acmicpc.net/problem/19238

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

int n, m, f, map[21][21], pchk[21][21], echk[21][21], sx, sy, flag, hit, endhit,
dx[4] = { 1, 0, -1, 0 }, dy[4] = { 0, 1, 0, -1 };
queue<qtmp> que;
priority_queue<pqtmp> pq;

int main() {
	scanf("%d%d%d", &n, &m, &f);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			scanf("%d", &map[i][j]);
		}
	}
	scanf("%d%d", &sx, &sy);
	// 출발점, 도착점 저장
	for (int i = 0; i < m; i++) {
		int a1, b1, a2, b2;
		scanf("%d %d %d %d", &a1, &b1, &a2, &b2);
		map[a1][b1] = a2 * 100 + b2;
	}
	// 탐색 시작
	while (m > 0) {
		// 체크, 큐, 힙, hit 초기화
		flag++;
		hit = 500000; endhit = 500000;
		que = queue<qtmp>();
		pq = priority_queue<pqtmp>();
		
		que.push({ sx, sy, 0 });
		pchk[sx][sy] = flag;
		while (!que.empty()) {
			qtmp now = que.front();
			que.pop();
			if (now.d > hit) break;  // hit보다 크면 break;
			if (map[now.x][now.y] != 0) {  // 사람을 발견하면 hit, 사람좌표는 pq에 삽입
				hit = now.d;
				pq.push({ now.x, now.y });
			}
			for (int i = 0; i < 4; i++) {
				int nx = now.x + dx[i];
				int ny = now.y + dy[i];
				// 범위 안이고, 벽이 아니며, 방문한 적이 없으면
				if (nx > 0 && nx <= n && ny > 0 && ny <= n && map[nx][ny] != 1 && pchk[nx][ny] != flag) {
					if (now.d + 1 > hit) continue;
					que.push({ nx, ny, now.d + 1 });
					pchk[nx][ny] = flag;
				}
			}
		}

		if (hit > f) {  // hit가 남은 연료보다 크면 -1 출력
			printf("-1");
			return 0;
		}

		// 힙에서 사람 pop
		sx = pq.top().x;
		sy = pq.top().y;
		int finx = map[sx][sy] / 100;
		int finy = map[sx][sy] % 100;
		map[sx][sy] = 0;  // 탐색되지 않게 0으로 초기화
		f -= hit; // 연료 감소

		que = queue<qtmp>();  // 큐 초기화
		que.push({ sx, sy, 0 });
		while (!que.empty()) {
			qtmp now = que.front();
			que.pop();
			if (now.x == finx && now.y == finy) {  // 도착 지점에 도착하면 연료 기록하고 break;
				endhit = now.d;
				sx = now.x;  // 택시 위치 도착지점으로 변경
				sy = now.y;
				break;
			}
			// 도착지점 탐색
			for (int i = 0; i < 4; i++) {
				int nx = now.x + dx[i];
				int ny = now.y + dy[i];
				// 범위 안이고, 벽이 아니며, 방문한 적 없으면
				if (nx > 0 && nx <= n && ny > 0 && ny <= n && map[nx][ny] != 1 && echk[nx][ny] != flag) {
					que.push({ nx, ny, now.d + 1 });
					echk[nx][ny] = flag;
				}
			}
		}

		if (endhit > f) {  // endhit이 남은 연료보다 크면 -1 출력
			printf("-1");
			return 0;
		}

		f += endhit;  // 사용한 연료만큼 충전
		m--;
	}
	printf("%d", f);
}

// 알고리즘 : BFS (너비 우선 탐색) + 구현
/*
풀이 : 한번의 운행당 BFS를 두번(손님을 찾으러 가는 탐색, 손님의 목적지로 가는 탐색) 수행한다.
각 손님의 좌표에 목적지 좌표를 활용하기 쉽게 x * 100 + y 꼴로 변환하여 삽입
1. 택시 위치에서 손님 탐색 BFS를 수행한다.
2. 가장 먼저 탐색되는 손님의 거리를 hit에 두고, hit보다 먼 거리는 탐색하지 않는다.
  2-1 : 손님이 탐색되지 않거나 hit이 남은 연료보다 크면 -1 출력 후 프로그램 종료
3. hit 범위 내의 손님들은 priority_queue(이하 pq)에 넣어서 손님 좌표 비교
  3-1 : x가 작은 순, x가 같다면 y가 작은 순
4. pq에서 pop한 손님의 좌표로 택시 위치 변경, 남은 연료 - hit
  4-1: 해당 손님의 좌표는 0으로 초기화하여 중복 탐색 방지
5. 택시 위치에서 해당 손님의 목적지 탐색 BFS 수행
6. 손님의 목적지를 찾으면 그 좌표로 택시 위치 변경, 남은 연료 + 이동한 거리
  6-1: 만약 남은 연료보다 목적지까지의 거리가 멀면 -1 출력 후 프로그램 종료
7. 손님카운트 1 감소
8. 손님을 모두 운반할 때까지 1~7까지 반복
9. 손님을 모두 운반하면 잔여 연료량 출력
*/
