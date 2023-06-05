// 치즈 : https://www.jungol.co.kr/problem/1840

#include<stdio.h>

int plate[100][100], chk[100][100], n, m, key = -1, dx[4] = { 1, -1, 0, 0 }, dy[4] = { 0, 0, 1, -1 }, tmp, bef, time = 0;

void dfs(int i, int j) {  // #1
	if (chk[i][j] == key || plate[i][j] == 2) return;
	if (plate[i][j] == 1) {
		plate[i][j] = 2;
		tmp--;
		return;
	}
	chk[i][j] = key;
	for (int t = 0; t < 4; t++) {
		int a = i + dx[t];
		int b = j + dy[t];
		if (a > -1 && a < n && b > -1 && b < m) {
			dfs(i + dx[t], j + dy[t]);
		}
	}
}

void remove() {  // #2
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (plate[i][j] == 2) {
				plate[i][j] = key;
			}
		}
	}
}

int cntCheese() {  // #3
	int cnt = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (plate[i][j] == 1) {
				cnt++;
			}
		}
	}
	return cnt;
}

int main() {
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &plate[i][j]);
		}
	}
	tmp = cntCheese();  
	while (1) { 
		bef = tmp;  // #4
		dfs(0, 0);
		remove();
		key--;  // #5
		time++;
		if (tmp == 0) {
			printf("%d\n%d", time, bef);  //#6
			break;
		}
	}
}

// #1 문제에서 판의 가장자리는 반드시 0으로 주어지기 때문에 0,0을 기준으로 치즈 외부에서 dfs을 수행시켰다.
//    이미 탐색한 구역은 key값을 주어 이미 탐색 했음을 표시했다.    
//    탐색하다 1(치즈)를 만나면 해당 부분을 2로 만들어주고, tmp(현재 남은 치즈 수)를 -1 해주었다.
//    탐색은 dx와 dy 배열을 활용해서 상하좌우 4방향을 미리 지정하여 탐색하는 방식을 사용했다.
// #2 #1이 수행 되고 나면 외부를 기준으로 치즈를 만날때마다 해당 치즈를 2로 올렸기 때문에 가장자리에 있는 모든 치즈는 2가 된다.
//    따라서 전체 plate를 탐색하여 2인 부분을 key로 낮추면 가장자리 치즈가 제거되어 안쪽 치즈만 남길 수 있다.
// #3 맨 처음 주어진 치즈의 양을 카운트 해서 tmp에 저장하기 위한 함수를 만들었다.
// #4 bef에 현재 tmp 값을 저장하고 dfs를 수행하면 bef에는 1시간이 지나기 전의 치즈 양이 기록되어 있게 된다.
//    순서대로 dfs, remove를 수행시켰다.
// #5 #1과 #2에서 이미 탐색했음을 표시하는 장치로 단순히 chk배열에 -1과 같은 정적인 수가 아닌 매 반복마다 1씩 작아지는 key값을 사용했다.
//    왜냐하면 정적인 임의의 수로 체크할 경우 매 탐색마다 chk 배열을 초기화시켜야 한다는 단점이 있고, 이는 소요 시간이 늘어남을 뜻한다고 생각했다.
//    그래서 매 탐색마다 이 구역이 탐색되었음을 뜻하는 수를 바꾸어 배열 초기화 과정 없이 변수만으로 같은 효과를 만들었다.
// #6 만약 dfs를 수행하고 남은 치즈의 양(tmp)이 0이면 소요된 시간과 이전 단계의 남은 치즈 양을 출력시키고 break로 반복을 종료시켰다.
