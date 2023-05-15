// http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=968&sca=3090

#include <stdio.h>
#include <algorithm>
using namespace std;

int id = 0, res[700], n, arr[30][30], dx[4] = { 1, 0, -1, 0 }, dy[4] = { 0, 1, 0, -1 }, q[700][2], st = -1, ed = -1;

void danji(int r, int c) {  // #1
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
	res[id++] = st + 1;  // #2
	return;
}

int main() {
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			scanf("%1d", &arr[i][j]);  // #3
		}
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (arr[i][j] == 1) {
				int q[700][2];  // #4
				st = -1; ed = -1;
				danji(i, j);
			}
			
		}
	}
	sort(res, res + id);
	printf("%d\n", id);
	for (int i = 0; i < id; i++) {
		printf("%d\n", res[i]);
	}
}

// res에는 각 단지의 크기, arr에는 단지 정보를 저장했다.
// dx와 dy는 각각 같은 인덱스의 값을 한쌍으로 하여, 한 좌표를 기준으로 상, 하, 좌, 우로 이동하는 경우를 쉽게 구현하기 위해 사용했다.
// #1 BFS의 방법을 활용했다.
//    처음 좌표를 q에 넣고 시작하며, q에서 좌표 차례대로 꺼내어 해당 좌표의 상, 하, 좌, 우 중 0이 아닌 곳이라면 그 좌표를 q에 추가했다.
//    만약 좌표를 q에 추가했다면, 해당 좌표는 더 이상 탐색하지 않아도 되기 때문에 0으로 바꾸어 재탐색을 방지했다.
//    모든 탐색이 끝나면, q의 크기가 곧 단지의 크기가 된다.
// #2 단지의 크기를 알아내면 이를 배열에 저장시켜야 했다.
//    문제에서 요구하는 답이 단지의 수와, 오름차순으로 정렬된 단지크기들이기 때문이다.
// #3 입력값이 정수 7자리 숫자로 주어진다. 이를 2차원배열에 하나씩 배정하는 방법으로 포맷을 %1d로 주었다.
// #4 매 탐색마다 큐과 키값을(st, ed) 초기화해서 이미 탐색이 끝난 부분에 대한 정보를 제거했다.
