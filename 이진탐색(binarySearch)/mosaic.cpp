// 모자이크 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=502&sca=3010

#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

struct tmp {
	int i, j;
};

int chk(tmp i, tmp j) {
	return i.j < j.j; 
}

vector<tmp> paper;

int main() {
	int a, b, p, n, l = 0, r = 0, mid = 0, s = 1000001, st, cnt, res;
	scanf("%d%d%d%d", &a, &b, &p, &n);
	for (int i = 0; i < n; i++) {
		int x, y;
		scanf("%d%d", &x, &y);
		if (l < x) l = x;  // #1
		if (s > y) s = y;  // #2
		paper.push_back({ x,y });  // #3
	}
	sort(paper.begin(), paper.end(), chk);  // #4
	r = b;  // #5
	while (1) {
		if (l > r) break;
		mid = (l + r) / 2;
		st = s + mid;
		cnt = 1;  // #6
		for (int i = 0; i < n; i++) {
			if (paper[i].j >= st) {  // #7
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

// #1 색종이는 반드시 바닥에 붙어있어야 하므로 색종이의 최소값은 입력된 좌표에서 행번호의 최대값 이상이어야 색종이로 해당 부분을 덮을 수 있다. 
//    따라서 left에 가장높이 있는 좌표의 행번호를 넣었다.
// #2 만약에 s가 입력된 열번호보다 작으면 s를 해당 번호로 내렸다. 이 과정은 색종이를 붙이기 시작할 지점을 정하기 위해서 수행했다.
// #3 주어지는 좌표(행,열)를 구조체로 만들어 paper 벡터에 넣었다.
// #4 벡터의 좌표들을 열번호를 오름차순으로 정렬했다.
// #5 right는 전체 벽의 가로길이(b)로 두었다. b 이상의 색종이는 불 필요하다.
// #6 #2에서 구한 벽에서 가장 왼쪽에 위치한 부분부터 mid 크기만큼의 색종이를 붙였다는 것을 st에 s + mid로 저장하고, 색종이 수(cnt)를 1로 두었다.
// #7 만약에 st보다 열번호가 작은 칸들은 해당 색종이에 칸이 전부 가려졌다는 뜻이다.
//    따라서 열번호가 st보다 커지면 해당 열번호부터 mid 크기만큼의 색종이를 붙이고 cnt를 1 증가시킨다.
