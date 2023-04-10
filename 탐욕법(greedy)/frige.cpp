// 냉장고 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1101&sca=3050

#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

struct tmp {
	int bot, top;
};

vector<tmp> rfg;

int chk(tmp i, tmp j) {
	return i.top < j.top;
}

int main() {
	int n, k = -300, cnt = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int a, b;
		scanf("%d%d", &a, &b);
		rfg.push_back({ a,b });  // #1
	}
	sort(rfg.begin(), rfg.end(), chk);  // #2
	for (int i = 0; i < rfg.size(); i++) {  // #3
		if (k == -300) {
			k = rfg[i].top;
			cnt++;
		}
		else {
			if (k < rfg[i].bot) {
				k = rfg[i].top;
				cnt++;
			}
		}
	}
	printf("%d", cnt);
}

// #1 화학물질의 최소 온도와 최고 온도를 구조체로 만들어 벡터에 저장했다.
// #2 벡터를 최고 온도를 기준으로 오름차순 정렬했다.
// #3 만약 k가 -300이라면(화학물질이 선택되지 않았다면) 냉장고 수(cnt)를 1 증가시키고 k에 선택한 화학물질의 최고 온도를 저장했다.
//    이 후, k가 다음에 선택한 화학물질의 최저 온도보다 작으면 해당 화확물질의 최고 온도를 k에 저장하고 cnt를 1 증가시켰다.
