// 요플레 공장 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1454&sca=3050

#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

struct tmp {
	int c, l, k;
};

vector<tmp> milk;

int main() {
	int n, m, cnt = 0, tmp;
	long long sum = 0;
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++) {
		int a, b;
		scanf("%d%d", &a, &b);
		milk.push_back({ a, b, b });  // #1
	}
	for (int i = 0; i < n; i++) {
		sum += cnt * m + milk[i].c * milk[i].l;  // #2
		if (cnt > 0) cnt -= milk[i].k;  // #3
		tmp = m;
		for (int j = i + 1; j < n; j++) {  // #4
			if (milk[i].c + tmp < milk[j].c) {
				cnt += milk[j].l;
				sum += milk[i].c * milk[j].l;
				milk[j].l = 0;
			}
			else {
				break;  // #5
			}
			tmp += m;  // #6
		}
	}
	printf("%lld", sum);
}

// #1 벡터에 1L당 가격, 구매하지 않은 수량, 필요한 수량을 구조체로 만들어 저장했다.
// #2 최종 금액(sum)에 (미리 구매한 우유(cnt)) * (1주 보관에 드는 비용(m)) + (이번 주 1L당 가격 * 구매하지 않은 수량)을 더했다.
// #3 만약에 cnt가 0이 아니면 이번주에 우유를 구매할 필요 없이 미리 구매해둔 우유만 쓰면 되므로 cnt에 (이번주에 필요한 수량)을 빼준다.
// #4 현재 탐색중인 주(i)를 기준으로 이후의 모든 주를 탐색하여 (보관비용(tmp) + 탐색중인 주의 우유 가격)과 비교했다.
//    i 주에 구매하는 것이 j(i 이후의 주) 주에 구매하는 것보다 싸면 cnt에 우유 L수를 추가하고 j주차의 구매하지 않은 수량을 0으로 낮추었다.
//    이를 통해 후에 루프를 돌면서 #2를 돌 때, 중복 구매되는 상황을 제거했다.
// #5 만약에 i주 보다 j주가 싸면 j 이후의 주는 탐색할 필요 없으므로 break로 탈출시켰다.
// #6 탐색하는 주(j)가 증가할수록 보관에 드는 비용도 증가해야 한다.
