// 장기 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=386&sca=3030

// !caution : 이 문제는 백트래킹 문제로 나와있지만 나는 BFS로 푸는게 더 효율적이라고 생각하여 BFS로 해결했다.

#include<stdio.h>

int board[101][101], point[100001][2];
int mx[8] = { 2, 1, -1, -2, -2, -1, 1, 2 }, my[8] = { 1, 2, 2, 1, -1 , -2, -2, -1 };  // #1
int n, m, r, c, s, k, st = -1, ed = -1, a, b, x, y;

void bfs() {
	while (st != ed) {
		x = point[++ed][0];
		y = point[ed][1];
		if (x == s && y == k) {
			printf("%d", board[s][k] - 1);
			return;
		}
		for (int i = 0; i < 8; i++) {  // #2
			a = x + mx[i];
			b = y + my[i];
			if (0 < a && a <= n && 0 < b && b <= m && board[a][b] == 0) {
				point[++st][0] = a;
				point[st][1] = b;
				board[a][b] = board[x][y] + 1;
			}
		}
	}
}

int main() {
	scanf("%d%d%d%d%d%d", &n, &m, &r, &c, &s, &k);
	point[++st][0] = r;  // #3
	point[st][1] = c;
	board[r][c] = 1;
	bfs();
	return 0;
}

// board는 처음위치를 포함하여 여기까지 몇번 움직였는지를 체크해주는 장기판 배열, point는 말이 이동할 좌표를 기록할 queue 배열이다.
// #1 mx와 my는 장기말이 움직일수 있는 8방향을 for문에서 i를 0 ~ 8로 돌리는 것과 연계하여 활용하기 위해 각각 x로 이동하는 칸, y로 이동하는 칸을 저장해두었다.
//    예를들어 for 문에서 i가 3이라면 mx[3]인 -2와 my[3]인 1이 만나 행으로 -2, 열로 1만큼 움직였다는 뜻이다.
// #2 BFS 알고리즘을 활용해서 for문으로 (mx[i], my[i])만큼 이동한 좌표를 다음 좌표로 지정(a, b)했다.
//    만약 (a, b)가 장기판 범위를 벗어나지 않고, board[a][b]가 0이라면 장기판 내 범위 중 한 번도 거치지 않은 장소라는 뜻이므로 해당 장소에 board[x][y] + 1을 저장했다.
//    이를 통해 매 회마다 이동한 좌표에 현재 까지 몇 번 이동 했는지 기록된다.
// #3 point에 r, c로 입력받은 말의 첫 좌표를 넣어주고, 이 좌표를 다시 거치지 않도록 board에서 1로 체크해준다.
