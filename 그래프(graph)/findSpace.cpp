// 영역 구하기 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=729&sca=3090

#include <stdio.h>
#include <algorithm>
using namespace std;
#define M 10100

int id = 0, res[M], n, m, d, arr[110][110], dx[4] = { 1, 0, -1, 0 }, dy[4] = { 0, 1, 0, -1 }, q[M][2], st = -1, ed = -1;

void space(int r, int c) {
	q[++st][0] = r; q[st][1] = c;
	arr[r][c] = 0;
	while (st != ed) {
		int a = q[++ed][0];
		int b = q[ed][1];
		for (int i = 0; i < 4; i++) {
			if (arr[a + dx[i]][b + dy[i]] == 1) {
				q[++st][0] = a + dx[i];
				q[st][1] = b + dy[i];
				arr[a + dx[i]][b + dy[i]] = 0;
			}
		}
	}
	res[id++] = st + 1;
	return;
}

int main() {
	scanf("%d%d%d", &n, &m, &d);
	for (int i = 1; i <= n; i++) {  // #1
		for (int j = 1; j <= m; j++) {
			arr[i][j] = 1;
		}
	}
	for (int i = 0; i < d; i++) {  // #2
		int r1, c1, r2, c2;
		scanf("%d%d%d%d", &r1, &c1, &r2, &c2);
		for (int j = c1 + 1; j <= c2; j++) {
			for (int k = r1 + 1; k <= r2; k++) {
				arr[j][k] = 0;
			}
		}
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (arr[i][j] == 1) {
				int q[10100][2];
				st = -1; ed = -1;
				space(i, j);
			}
			
		}
	}
	sort(res, res + id);
	printf("%d\n", id);
	for (int i = 0; i < id; i++) {
		printf("%d ", res[i]);
	}
}

// 앞서 해결했던 단지번호구하기와 완전히 똑같은 문제였다. 배열 크기와 입출력 부분만 수정했다.
// #1 1은 가능, 0은 불가능으로 두기 위해 먼저 범위 내 모든 구역을 1로 채웠다.
// #2 r1,c1 부터 r2,c2 까지는 불가능 영역으로 두기위해 해당 영역을 0으로 다시 내렸다.
// 나머지는 동일하게 BFS를 통한 영역 크기 구하는 알고리즘으로 해결했다.
