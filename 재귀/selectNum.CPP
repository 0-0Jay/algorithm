// 숫자 고르기 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=731&sca=2080

#include<stdio.h>

int cnt, a[101], num[101], chk[101], n;

void sel(int st, int now) {
	if (chk[now] == 1 || num[now] == 1) {
		for (int i = 1; i <= n; i++) {
			chk[i] = 0;
		}
		return;
	}
	chk[now] = 1;  // #4
	if (st == now) {  // #5
		for (int i = 1; i <= n; i++) {
			if (chk[i] == 1) {
				cnt++;
				num[i] = 1;
				chk[i] = 0;
			}
		}
		return;
	}
	sel(st, a[now]);
}

int main() {
	int ans = 0;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &a[i]); // #1
	}
	for (int i = 1; i <= n; i++) {
		cnt = 0;
		sel(i, a[i]);  // #2
		ans += cnt;  // #3
	}
	printf("%d\n", ans);
	for (int i = 0; i <= n; i++) {
		if (num[i] == 1) {  // #6
			printf("%d\n", i);
		}
	}
}

// a배열 : 주어진 값을 저장하는 배열 / num배열 : 사이클이 발생했던 위치임을 체크하는 배열 / chk배열 : 현 회차에서 이미 탐색한 공간임을 체크하는 배열
// #1 주어지는 값을 a배열에 1번 인덱스부터 입력했다. ( 인덱스 번호를 활용하여 편리하게 해결하기 위함. )
// #2 sel함수에 시작 인덱스 번호(i)와 시작 인덱스의 값(a[i])를 초기값으로 주고 재귀함수를 돌렸다.
// #3 매 반복마다 cnt(사이클이 발생하는 그룹의 크기를 저장할 변수)를 0으로 초기화하고 sel함수를 통해 cnt에 값이 발생하면 ans에 누적하는 방식을 사용했다.
// #4 만약 사이클이 발생했을 경우, 재귀함수에서 무한 루프가 발생 할 수 있으므로 chk배열을 통해 현재 탐색한 인덱스를 체크하여 중복 탐색되지 않도록 했다.
// #5 now(현재 탐생 중인 위치)가 st(시작 위치)와 동일하다면 사이클이 발생했으므로 전체 인덱스를 돌면서 사이클에 해당하는 인덱스는 num배열에서 1로 체크하고,
//    다음 회차 반복을 위해 chk배열은 다시 0으로 초기화했다. 이후 cnt를 return하여 #3에서 ans에 누적되도록 했다.
// #6 모든 탐색이 끝나면 num배열을 탐색하여 1로 체크되어 있는 인덱스를 출력한다.
