// 로또 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2082&sca=2080

#include<stdio.h>

int number[13], res[6], n;

void lotto(int d) {
	if (d > 1 && res[d - 1] <= res[d - 2]) return;  // #2
	if (d == 6) {  // #3
		for (int i = 0; i < 6; i++) {
			printf("%d ", res[i]);
		}
		printf("\n");
		return;
	}
	for (int i = 0; i < n; i++) {  // #4
		res[d] = number[i];
		lotto(d + 1);
	}
}

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &number[i]);
	}
	lotto(0);  // #1
	return 0;
}

// number는 주어지는 숫자들을 저장할 배열. res는 선택된 번호 6 개를 저장할 배열
// #1 lotto함수에 초기값으로 0(선택된 숫자의 개수)을 인수로 주고 재귀함수를 돌렸다.
// #2 만약 선택된 수가 1개 이상일 때, 선택된 숫자가 이전에 선택한 숫자보다 작거나 같으면 더 이상 이 경우의 수는 탐색하지 않았다.
//    이를 통해 오름차순 정렬을 하지 않아도 오름차순으로 수가 선택되어 저장된다.
// #3 만약 선택한 숫자의 개수(d)가 6이면 지금까지 선택한 수를 순서대로 출력한다.
// #4 number배열의 숫자들이 다음에 올 경우를 각각 재귀함수를 활용해 탐색했다.
//    #2의 조건으로 인해 return되지 않으면 최종 깊이까지 탐색하는 DFS 문제다.
