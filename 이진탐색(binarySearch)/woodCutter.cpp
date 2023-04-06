// 나무꾼 미르코 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=4794&sca=3010

#include <stdio.h>
# define M 1000100

long long tree[M];

int main() {
	int n;
	long long m, l , r, mid, sum, max = 0, ans;
	scanf("%d%lld", &n, &m);
	for (int i = 0; i < n; i++) {
		scanf("%d", &tree[i]);
		if (tree[i] > max) max = tree[i];  // #1
	}
	l = 0, r = max;
	while (1) {
		if (l > r) break;
		mid = (l + r) / 2;
		sum = 0;
		for (int i = 0; i < n; i++) {
			if (tree[i] > mid) {
				sum += tree[i] - mid;  // #2
			}
		}
		if (sum >= m) {  // #3
			ans = mid;
			l = mid + 1;
		}
		else if (sum < m) r = mid - 1;
	}
	printf("%d", ans);
}

// #1 입력받은 나무의 길이의 최대 값을 구해 right로 사용해서 이진탐색할 범위를 축소시켰다.
// #2 절단기의 높이(mid)로 모든 나무를 잘랐을 때 나오는 나무의 길이를 모두 sum에 저장해서 가져가야하는 최소 나무 길이(m)와 비교하는 방식을 사용했다.
// #3 절단기의 높이의 최대값을 구해야 하므로 만약 m이 sum과 같다면 ans에 m을 저장해두고, left를 올려서 한번 더 수행해본다.




