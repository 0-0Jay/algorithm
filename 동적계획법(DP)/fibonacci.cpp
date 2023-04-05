// 피보나치 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2862&sca=3060

#include <stdio.h>
#define d 1000000007

int a[100000] = { 0,1,1 };

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 3; i <= n; i++) {
		a[i] = ((a[i - 1] % d) + (a[i - 2] % d)) % d;
	}
	printf("%d", a[n]);
}

// bottom-up 방식으로 코딩했다.
