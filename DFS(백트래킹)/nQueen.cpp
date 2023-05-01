// #1 N Queen : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1162&sca=3030

#include<stdio.h>
#include<math.h>

int board[14], cnt = 0, n, check;

void queen(int c, int d) {
	if (c == d) {  // #1
		cnt++;
		return;
	}
	for (int i = 1; i <= d; i++) {
		check = 0;
		board[c] = i;
		if (c > 0) {
			for (int j = 0; j < c; j++) {
				if (abs(board[c] - board[j]) == c - j || board[c] == board[j]) {  // #2
					check = 1;
					break;
				}
			}
		}
		if (check == 1) continue;  // #3
		queen(c + 1, d);  // #4
		if (i == d) return;
	}
}

int main() {
	scanf("%d", &n);
	queen(0, n);
	printf("%d", cnt);
}

// board는 각 행에서 몇 번 열에 퀸을 배치할지를 저장하는 배열
// #1 c(현재 행 번호)가 d(총 행수) 만큼 진행되었으면 가능한 수를 찾았다는 의미이므로 cnt를 1 증가시켰다.
// #2 board 배열을 처음부터 c 이전까지 탐색하여 board[j]가 board[c]와 같은 열이거나, 대각선 상에 존재하면 check를 1로 바꿔주었다.
//    대각선 조건 : board 배열에서 (c번 인덱스의 값 - j번 인덱스의 값)과 (c - j)의 값이 같으면 대각선 상에 존재한다.
//    ex) (1, 2)와  (3, 4)의 경우
// #3 check가 1이면 불가능한 배치이므로 다음 배치로 넘어갔다.
// #4 c는 계속 +1될 것이고, 행은 처음부터 순차적으로 진행되기 때문에 #2의 조건을 위쪽 행까지 탐색할 필요가 없다.

