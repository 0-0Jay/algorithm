// 다음 조합 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=762&sca=2080

#include<stdio.h>
#include<algorithm>
int n, m, res[10], a[10], id, chk[50000][10];
void comb(int d) {
	if (d > 1 && res[d - 1] <= res[d - 2]) return;  // #2
	if (d == m) {  // #3
		for (int i = 0; i < m; i++) {
			chk[id][i] = res[i];
		}
		id++;
		return;
	}
	for (int i = 1; i <= n; i++) {
		res[d] = i;
		comb(d + 1);
	}
}
int main() {
	int i, an;
	scanf("%d%d", &n, &m);
	for (int i = 0; i < m; i++) {
		scanf("%d", &a[i]);
	}
	comb(0);  // #1
	for (int i = 0; i < id; i++) {
		an = 0;
		for (int j = 0; j < m; j++) {  // #4
			if (chk[i][j] == a[j]) an++;
		}
		if (an == m) {
			if (i < id - 1) {
				for (int j = 0; j < m; j++) { 
					printf("%d ", chk[i + 1][j]);  // #5
				}
			}
			else {
				printf("NONE");
			}
		}
	}
	return 0;
}

// a는 주어진 조합을 저장하는 배열, res는 선택한 숫자를 임시로 저장하는 배열, chk는 완성된 조합을 저장하는 배열이다.
// #1 comb함수의 초기 인수로 0(선택한 숫자의 수, 함수에서 d)을 주고, 숫자를 선택할 때마다 1씩 증가시켜서 재귀함수를 돌렸다.
// #2 앞서 풀었던 "로또" 문제와 동일하게 오름차순 정렬을 하지 않고 처음부터 큰 값만 선택하게 조건을 걸었다.
//    이 조건을 통해 오름차순으로 정렬되는 것과 동시에 중복 조합도 방지할 수 있다.
//    예를 들어, 1 2 3이 선택되었다면 다음 2부터 선택할때는 1이 선택되지 않으므로 중복을 방지한다.
// #3 DFS 알고리즘으로 d(선택한 숫자의 수, 현재 탐색 중인 깊이)가 전체 숫자의 수(m)와 같으면 조합이 완성된 것이므로 이를 chk에 저장했다.
// #4 an을 0으로 초기화하고 for문을 통해 chk에 저장된 조합들을 탐색하면서 처음에 주어진 조합(a)과 각 자릿수를 비교했다.
//    같은 수면 an에 1을 더해주는 과정을 끝까지 반복했을 때, an이 전체 숫자의 수(m)와 같으면 a와 chk[i]의 조합은 같다는 뜻이다.
// #5 a와 chk[i]가 같으므로 다음에 나올 조합은 chk[i+1]이 된다.
