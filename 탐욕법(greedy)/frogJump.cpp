// 개구리 점프 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2753&sca=3050

#include <vector>
#include <stdio.h>
#include <algorithm>
using namespace std;

struct tmp {
	int x1, x2, r, group = 0;
};

int chk(tmp i, tmp j) {
	return i.x1 < j.x1;
}

int chk2(tmp i, tmp j) {
	return i.r < j.r;
}

vector<tmp> wood;

int main() {
	int n, m, id = 1, now = 0, num = 1;
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++) {
		int a, b, c;
		scanf("%d%d%d", &a, &b, &c);
		wood.push_back({ a,b,id++ }); // #1
	}
	sort(wood.begin(), wood.end(), chk); // #2
	wood[0].group = num;
	now = wood[0].x2; // #3
	for (int i = 1; i < n; i++) {  // #4
		if (now < wood[i].x1) num++;
		wood[i].group = num;
		if (wood[i].x2 > now) now = wood[i].x2;
	}
	sort(wood.begin(), wood.end(), chk2);  // #5
	for (int i = 0; i < m; i++) {  // #6
		int a, b;
		scanf("%d%d", &a, &b);
		if (wood[a - 1].group == wood[b - 1].group) printf("1\n");
		else printf("0\n");
	}
}

// #1 통나무의 왼쪽 좌표(x1), 오른쪽 좌표(x2), 높이 좌표(y)를 받지만, 벡터에 y를 넣지 않았다.
//    왜냐하면 이 문제에서 수직으로 위 아래 점프에는 제한이 없다. 따라서 y좌표는 의미없는 입력값이다.
//    그러나 문제에서 통나무 번호에 따른 가능/불가능을 묻고 있기 때문에 y좌표 대신 통나무 번호(id)를 매겼다.
// #2 통나무의 x1~x2가 겹치는 부분을 알기 위해 통나무들을 x1 좌표를 기준으로 오름차순 정렬했다.
// #3 먼저 wood[0]을 1번(num) 그룹으로 지정하고, now에는 wood[0]의 x2좌표를 초기값으로 주었다.
//    이 후, now에는 아래 반복문을 돌면서 현재까지 탐색한 통나무들 중 가장 오른쪽에 있는 x2좌표를 넣어줄 것이다.
// #4 통나무 벡터에서 이전에 0번 인덱스의 통나무를 미리 탐색 해주었기 때문에 1번 인덱스 부터 탐색했다.
//    i번 통나무의 왼쪽(x1)좌표가 now보다 작거나 같으면 이 통나무는 현재 그룹(num)에 속한다는 뜻이므로 group에 num을 지정하고,
//    now보다 크다면 이 통나무는 새로운 그룹에 소속되어야 하므로 num을 1 올려주었다.
//    같은 그룹에 속한다는 것은 개구리가 1번 이상의 점프로 이동할 수 있는 통나무 집합에 포함될 수 있다는 뜻이다.
// #5 다시 통나무를 입력받을 당시의 순서로 바꿔야 이후에 연산에 편리할 것이라고 판단하여 id 순서대로 재정렬했다.
// #6 이후 질문을 받아 a 통나무와 b 통나무의 group 번호를 비교하여 같으면 1, 아니면 0을 출력했다.
