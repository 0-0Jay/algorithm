// 블랙잭 : https://www.acmicpc.net/problem/2798

#include <stdio.h>

int n, m, ans = 0, arr[101];

void bjack(int d, int sum) {  // #1
	if (sum > m) return;  // #2
	if (d == 3) { // #3
		if (ans < sum) ans = sum;
		return;
	}
	for (int i = 0; i < n; i++) {
		if (arr[i] == -1) continue;  // #4
		int a = arr[i];
		arr[i] = -1;
		bjack(d + 1, sum + a);
		arr[i] = a;
	}
	return;
}

int main(void) {
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	bjack(0, 0);
	printf("%d", ans);
}

// #1 d에는 고른 숫자 개수, sum에는 고른 숫자들의 합을 저장하여 재귀함수를 통해 완전 탐색을 수행했다.
// #2 합이 m을 넘어가면 안되기 때문에 m을 넘어가는 순간 return하여 해당 루트를 탐색하지 않는다.
// #3 가장 가까운 값을 찾는 것이 목적이다. 따라서 #2에서 넘어가는 값은 걸러주고 있으므로, 나머지 합들 중에 최대값을 구했다.
// #4 이미 고른 카드는 -1로 낮추고, 뽑았을 때 -1이면 continue 시키는 방법으로 중복 선택을 방지했다.
//    만약 골랐던 수가 조건을 벗어난다면 다시 해당 숫자를 원래 숫자로 돌려놓고 다음 수를 탐색시켰다.
