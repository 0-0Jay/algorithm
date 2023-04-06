// 모자이크 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=502&sca=3010

#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

struct tmp {
	int i, j;
};

int chk(tmp i, tmp j) {
	return i.j < j.j;  // #
}

vector<tmp> paper;

int main() {
	int a, b, p, n, l = 0, r = 0, mid = 0, s = 1000001, st, cnt, res;
	scanf("%d%d%d%d", &a, &b, &p, &n);
	for (int i = 0; i < n; i++) {
		int x, y;
		scanf("%d%d", &x, &y);
		if (l < x) l = x;
		if (s > y) s = y;
		paper.push_back({ x,y });
	}
	sort(paper.begin(), paper.end(), chk);
	r = b;
	while (1) {
		if (l > r) break;
		mid = (l + r) / 2;
		st = s + mid;
		cnt = 1;
		for (int i = 0; i < n; i++) {
			if (paper[i].j >= st) {
				cnt++;
				st = paper[i].j + mid;
			}
		}
		if (cnt > p) l = mid + 1;
		else {
			r = mid - 1;
		}
	}
	printf("%d", l);
	return 0;
}

// #1
//
//
//
//
//
