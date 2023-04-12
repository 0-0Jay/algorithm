// 공주님의 정원 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1721&sca=3050

#include<stdio.h>
#include<algorithm>
using namespace std;

struct tmp {
	int st, ed;
}flower[100000];

int main() {
	int n, ld, sd = 301, cnt = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int a1, a2, b1, b2;
		scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
		flower[i] = { a1 * 100 + a2, b1 * 100 + b2 };  // #1
	}
	while (1) {
		ld = sd;  // #2
		for (int i = 0; i < n; i++) {
			if (flower[i].ed > ld && flower[i].st <= sd) {
				ld = flower[i].ed;  // #3
			}
		}
		if (ld == sd) {  // #4
			printf("0");
			break;
		}
		sd = ld;  // #5
		cnt++;
		if (sd >= 1201) {  // #6
			printf("%d", cnt);
			break;
		}
	}
	return 0;
}

// flower는 각 꽃의 피는 날과 지는 날을 저장할 배열
// #1 꽃이 피는 날과 지는 날을 연산하기 편하게 하기 위해 하나의 숫자로 만들었다.
//    예를 들어, 1월 1일에 핀다면 a1 = 1, a2 = 1이 되는데, 이를 1 * 100 + 1의 계산을 통해 101로 사용한다.
// #2 우선 피는 날과 지는 날을 현재 탐색중인 날로 두었다. 초기값은 301 (3월 1일) 이다.
// #3 flower를 처음부터 끝까지 탐색하면서 피는 날(st)이 3월 1일보다 이전이면서, 지는 날(ed)이 가장 느린 날을 ld에 저장했다.
//    왜냐하면, 이전에 피는 꽃이 피어있는 기간과 겹치면서 가장 오래 피어있는 꽃을 골라야 꽃의 개수를 최소화 할 수 있기 때문이다.
// #4 만약 탐색을 끝까지 했는데 ld의 변화가 없다면, 꽃이 피어있는 기간이 겹치지 않았다는 뜻이므로 0을 출력하고 반복문을 종료시켰다.
// #5 반복문이 종료되지 않았다는 뜻은 꽃을 선택했다는 뜻이기 때문에 다음 탐색을 위해 sd를 ld 값으로 올려주고, 카운트를 1개 올려주었다.
// #6 sd가 1201 이상이 되었다는 것은 12월 1일까지 꽃이 계속 피어있을 수 있게 꽃을 골랐다는 뜻이므로 카운트를 출력시키고 반복문을 종료시켰다.
