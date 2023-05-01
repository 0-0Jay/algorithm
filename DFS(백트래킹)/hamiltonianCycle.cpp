// 해밀턴 순환회로 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=954&sca=3030

#include<stdio.h>

int chk[14] = { 0,1 }, map[14][14], n, min = 10000, cost[14];

void route(int c, int d) {
	if (d == n) {
		if (map[c][1] == 0 || cost[d - 1] + map[c][1] >= min) return;  // #1
		min = cost[d - 1] + map[c][1];
		return;
	}
	for (int i = 2; i <= n; i++) {  // #2
		if (map[c][i] == 0 || chk[i] != 0 || cost[d - 1] + map[c][i] > min) continue;  // #3
		cost[d] = cost[d - 1] + map[c][i];
		chk[i] = map[c][i];
		route(i, d + 1);
		chk[i] = 0;  // #4
	}
}

int main() {
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			scanf("%d", &map[i][j]);
		}
	}
	route(1, 1);
	printf("%d", min);
}

// chk는 해당 장소를 방문했다는 것을 체크, map은 각 이동별 소모비용, cost는 누적합을 저장하는 배열
// #1 만약 이동할 방법이 없거나(map에서 해당 값이 0), 마지막에 회사로 돌아오는 비용을 더했을 때 기존의 최소값보다 작지 않으면 return 시켰다.
//    그 외의 경우는 더 낮은 값이 존재한다는 뜻이므로 min의 값을 더 낮은 값으로 교체해주었다.
// #2 다음에 도착할 장소를 2 ~ n까지 탐색했다. 
//    i가 1인 경우는 회사로 다시 돌아오는 경우로 마지막에 연산할 것이기 때문에 여기서는 포함시키지 않았다.
// #3 #1번에서의 최종 점검 외에도 중간 과정에서 더이상 진행해도 의미없는 경우가 발생할 경우 해당 장소를 넘겼다.
//    그 외의 경우는 다음 장소를 c로 주고, cost[d]에 해당 장소까지의 누적 비용을 저장했다.
//    chk[i]에는 해당 장소로 이동하는데 소모되는 비용을 기록하여 이미 거쳐간 장소임을 표시했다.
// #4 만약 해당 서브 트리로의 탐색이 끝났다면, chk에 저장했던 내용을 다음 서브트리에서 사용할 수 있게 0으로 초기화 시켰다.
