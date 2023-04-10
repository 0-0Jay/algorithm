// 추 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2861&sca=3050

#include <stdio.h>

int main() {
	int a, b, c, d, e, n, cnt = 0;
	scanf("%d%d%d%d%d%d", &a, &b, &c, &d, &e, &n);
	while (e > 0 && n >= 16) {  // #1
		cnt++; n -= 16; e--;
	}
	while (d > 0 && n >= 8) {
		cnt++; n -= 8; d--;
	}
	while (c > 0 && n >= 4) {
		cnt++; n -= 4; c--;
	}
	while (b > 0 && n >= 2) {
		cnt++; n -= 2; b--;
	}
	while (a > 0 && n >= 1) {
		cnt++; n--; a--;
	}
	if (n == 0) printf("%d", cnt);
	else printf("impossible");
}

// #1 가장 무거운 추부터 최대한 사용하는 방식으로 풀었다.
//    어떤 추가 남은 무게보다 작거나 남은 개수가 부족할 경우는 다음 무게로 넘겼다.
