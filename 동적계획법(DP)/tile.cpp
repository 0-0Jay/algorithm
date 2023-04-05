// 두 줄로 타일 깔기 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=687&sca=3060

#include <stdio.h>
#define d 20100529

int a[100000] = { 0,1,3 };

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 3; i <= n; i++) {
		a[i] = ((a[i - 1] % d) + (a[i - 2] * 2) % d) % d;
	}
	printf("%d", a[n]);
}

// 타일의 세로가 1칸인 경우부터 n칸인 경우까지의 갯수를 세어보고 일반항을 구하는 방식으로 해결했다.
// 4번째 항까지 구했을 때 찾은 일반항은 a(n) = a(n-1) + (a(n-2) * 2) 였다.
