// 테트로미노 : https://www.acmicpc.net/problem/14500

#include<stdio.h>

int arr[510][510], chk[510][510], n, m, maxSum = 0, dx[4] = { 1, -1, 0, 0 }, dy[4] = { 0, 0, 1, -1 };

void dfs(int a, int b, int d, int sum) {  // #1
	if (chk[a][b] == 1) return;
	if (d == 4) {
		if (sum > maxSum) maxSum = sum;
		return;
	}
	chk[a][b] = 1;
	for (int i = 0; i < 4; i++) {
		if (a + dx[i] > 0 && a + dx[i] <= n && b + dy[i] > 0 && b + dy[i] <= m) {
			dfs(a + dx[i], b + dy[i], d + 1, sum + arr[a + dx[i]][b + dy[i]]);
		}
	}
	chk[a][b] = 0;
	return;
}

void Tform(int a, int b) {  // #2
	int full = arr[a][b];
	for (int i = 0; i < 4; i++) {
		full += arr[a + dx[i]][b + dy[i]];
	}
	for (int i = 0; i < 4; i++) {
		int T = full - arr[a + dx[i]][b + dy[i]];
		if (T > maxSum) maxSum = T;
	}
}

int main() {
	scanf("%d%d", &n, &m);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			scanf("%d", &arr[i][j]);
		}
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			dfs(i, j, 1, arr[i][j]);
			Tform(i, j);
		}
	}
	printf("%d", maxSum);
}

// #1 먼저 DFS를 활용해서 'ㅗ' 모양을 제외한 다른 4가지 모양을 탐색했다.
//    인자에 sum과 행/열 좌표를 주어 각 좌표에 도착하면 해당 좌표의 값을 sum에 누적시켰다.
//    d는 탐색 깊이로, 4가되면 총 4개의 연결된 칸을 탐색했다는 의미이기 때문에 sum을 maxSum값과 비교해 더 큰 값이면 갱신해주고 return 했다.
// #2 #1에서 제외했던 'ㅗ' 모양을 탐색하기 위해 따로 함수를 작성했다.
//    full에 해당 좌표를 기준으로 상하좌우의 좌표를 모두 더한 값('+' 모양의 도형)을 저장했다.
//    이후 '+' 모양의 도형에서 상, 하, 좌, 우의 값을 하나씩 빼는 방법으로 'ㅗ','ㅓ','ㅏ','ㅜ' 모양을 탐색했다.
