// 벽장문의 이동 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=685&sca=3030

#include<stdio.h>
#include<math.h>

int use[20], min = 100000, n, st1, st2, m;

void mov(int a, int b, int r, int d) {  // #1
	if (d > min) return;  // #2
	if (r == m) {
		if (d < min) min = d;
		return;
	}
	mov(use[r], b, r + 1, d + abs(use[r] - a));  // #3
	mov(a, use[r], r + 1, d + abs(use[r] - b));
	return;
}

int main() {
	scanf("%d%d%d%d", &n, &st1, &st2, &m);
	for (int i = 0; i < m; i++) {
		scanf("%d", &use[i]);
	}
	mov(st1, st2, 0, 0);
	printf("%d", min);
	return 0;
}

// use 배열에는 열어야할 문의 좌표를 순서대로 저장해놓는 배열이다.
// #1 a, b에 각각 열린 문의 좌표를 두고, r로 use의 인덱스를, d로 움직인 문의 개수를 세었다.
// #2 만약에 움직인 문의 개수(d)가 이전에 저장된 최소값보다 크다면, 이 루트는 이미 최소 이동 수가 불가능하다는 뜻이므로 return으로 벗어났다.
// #3 문을 움직이는 방법은 a의 위치를 움직이는 방법과 b의 위치를 움직이는 방법으로 두가지다.
//    따라서 각각 a를 use[r]로 옮기고 a와 use[r]의 차를(움직인 문의 개수는 음수일 수 없으므로 절대값을 취했다.) 움직인 문의 개수(d)에 저장했다.
