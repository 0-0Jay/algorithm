// 회의실 배정 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=645&sca=3050

#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

struct tmp {
	int num, s, e;
};

vector <tmp> table;
int chk(tmp i, tmp j) {
	return i.e < j.e;
}

int ans[510];

int main() {
	int n, cnt = 0, now = 0, a, b, c;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &a, &b, &c);
		table.push_back({ a, b, c });  // #1
	}
	sort(table.begin(), table.end(), chk);  // #2
	for (int i = 0; i < n; i++) {  // #3
		if (now == 0) {
			now = table[i].e;
			ans[cnt++] = table[i].num;
		}
		else {
			if (now <= table[i].s) {
				now = table[i].e;
				ans[cnt++] = table[i].num;
			}
		}
	}
	printf("%d\n", cnt);
	for (int i = 0; i < cnt; i++) {
		printf("%d ", ans[i]);
	}
}

// 선택된 회의 번호를 순서대로 저장할 배열.
// #1 회의 번호, 시작 시간, 끝 시간을 구조체로 벡터에 저장했다.
// #2 끝 시간을 기준으로 벡터를 오름차순 정렬했다.
// #3 now에 현재 회의의 끝시간을 저장하고, 정렬된 벡터를 순서대로 탐색해서 만약 시작 시간이 now보다 뒤라면 해당 회의의 끝시간을 now에 업데이트했다.
//    now가 업데이트 될때마다 ans에 현재 탐색한 테이블의 회의번호를 저장한다. cnt를 0으로 시작해서 하나씩 증가시켜 인덱스를 옮기는 방식을 사용했다.
