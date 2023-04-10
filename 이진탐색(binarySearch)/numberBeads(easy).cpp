// 숫자구슬(easy) : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=4300&sca=30

#include <stdio.h>

int arr[301];

int main() {
	int n, m, l = 0, r = 0, mid, tmp = 0, cnt = 0;
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
		r += arr[i];
		if (arr[i] > l) l = arr[i];  // #1
	}
	while (1) {
		if (l > r) break;
		mid = (l + r) / 2;
		cnt = 0; tmp = 0;
		for (int i = 0; i < n; i++) {
			tmp += arr[i];  // #2
			if (tmp + arr[i + 1] > mid || tmp > 0 && i == n - 1) {  // #3
				cnt++;
				tmp = 0;
			}
		}
		if (cnt > m) l = mid + 1;  // #4
		else r = mid - 1;
	}
	printf("%d", l);
}

// #1 값을 입력받으면서 right(최대 합)에 계속 누적시키고, left(최소 합)에는 입력된 값들 중 최대값을 저장했다.
//    문제에서 요구한 답은 그룹별 합의 최대값이기 때문에 left를 모든 숫자 중 최대 값으로 두었다.
//    최대 합이라면 반드시 모든 숫자중 최대값 이상일 것이기 때문이다.
// #2 배열을 돌면서 tmp(임시로 저장할 부분 합)에 숫자들을 누적시켰다.
// #3 tmp에 다음 수를 더했을 때, mid보다 크다면 cnt를 1 증가시키고 tmp를 0으로 초기화 시켰다.
// #4 만약 cnt가 주어진 m(그룹 수)보다 크다면 left를 올려서 부분 합의 최대값을 높게 잡고, 작으면 right를 낮춘다.
