// 장난감조립(easy) : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=300&sca=2080

#include<stdio.h>
#include<vector>
using namespace std;

struct tmp {
	int base, count;
};

vector<tmp> part[101];  // #1
int cnt[101];

void sol(int n) {
	if (part[n].size() == 0) {  // #3
		cnt[n]++;
		return;
	}
	for (int i = 0; i < part[n].size(); i++) {
		for (int j = 0; j < part[n][i].count; j++) {
			sol(part[n][i].base);  // #4
		}
	}
	return;
}

int main() {
	int n, m, a, b, c;
	scanf("%d%d", &n, &m);
	for (int i = 0; i < m; i++) {
		scanf("%d%d%d", &a, &b, &c);
		part[a].push_back({ b, c });
	}
	sol(n); // #2
	for (int i = 1; i <= 100; i++) {
		if (cnt[i] >= 1) {
			printf("%d %d\n", i, cnt[i]);
		}
	}
	return 0;
}

// cnt는 기본 부품의 개수를 카운팅 하는 배열
// #1 part 벡터를 생성하여 각 인덱스를 부품의 번호로 활용하고, 구성 부품은 구조체(tmp)를 활용하여 해당 인덱스에 삽입했다.
//    예를 들어, 입력값으로 5 1 2 가 들어오면 5번 부품은 1번 부품이 2개 사용되었다는 뜻이므로 part의 5번 인덱스에 {1, 2}를 저장한다.
// #2 Top-down 방식으로 해결하는 문제다. sol함수의 인수로 완제품 숫자를 주고, 재귀함수를 돌리면서 완제품을 작은 부품으로 분해했다. 
// #3 만약 해당 부품을 구성하는 하위 부품이 없다면 해당 부품은 '기본 부품'이므로 더 이상 분해하지 못한다는 뜻이다.
//    cnt배열에서 해당 부품 인덱스의 값을 1 올리고 return 한다.
// #4 반면, 해당 부품을 구성하는 하위 부품이 있다면, 해당 부품의 종류와 그 개수만큼 재귀 호출을 반복하여 더 이상 분해되지 않을 때까지 분해한다.
