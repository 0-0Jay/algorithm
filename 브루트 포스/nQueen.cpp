// 백준 9663번 N-Queen : https://www.acmicpc.net/problem/9663

#include<stdio.h>
#include<algorithm>
using namespace std;

int board[14], cnt = 0, n, check;

void queen(int c, int d) {
	if (c == d) {  // 마지막 가로줄 까지 탐색했으면 카운팅
		cnt++;
		return;
	}
	for (int i = 1; i <= d; i++) {
		check = 0;
		board[c] = i;
		if (c > 0) {
			for (int j = 0; j < c; j++) {
				if (abs(board[c] - board[j]) == c - j || board[c] == board[j]) {  // 이전 가로줄에 놓인 퀸들 중 같은 대각/세로줄에 놓인 퀸이 있으면 체크
					check = 1;
					break;
				}
			}
		}
		if (check == 1) continue;  // 대각선 상에 퀸이 있으면 스킵
		queen(c + 1, d);  // 퀸은 같은 가로줄에 존재할 수 없으므로 세로줄만 1칸씩 높여가며 체크
		if (i == d) return;  // 끝까지 탐색했으면 리턴
	}
}

int main() {
	scanf("%d", &n);
	queen(0, n);
	printf("%d", cnt);
}
