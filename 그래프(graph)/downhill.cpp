// 백준 1520번 내리막 길 : https://www.acmicpc.net/problem/1520

#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define M 501

int n, m, arr[M][M], cnt[M][M], dx[4] = {1, 0, -1, 0}, dy[4] = {0, 1, 0, -1};

int DFS(int x, int y) {
	if (cnt[x][y] >= 0) return cnt[x][y];  // 방문 한 기록이 있으면 카운팅 리턴
	int sum = 0;  // 방문 기록을 위한 카운팅 용도 변수
	for (int i = 0; i < 4; i++) {
		int a = x + dx[i];
		int b = y + dy[i];
		if (a > -1 && a < n && b > -1 && b < m && arr[a][b] > arr[x][y]) {
			sum += DFS(a, b);  // 동서남북 4방향에서 값 추출해서 합산
		}
	}
	cnt[x][y] = sum;  // cnt에 sum을 넣음으로 써 방문 기록 + 카운팅 동시 수행
	return cnt[x][y];
}

int main() {
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &arr[i][j]);
			cnt[i][j] = -1;  // 카운트를 전부 -1로 설정
		}
	}
	cnt[0][0] = 1;
	printf("%d", DFS(n - 1, m - 1));
}

// 알고리즘 : DP + DFS
/*
풀이 : Top-down 방식으로 이전 칸에서 방문카운트를 가져와서 합산하는 방식
불필요한 탐색을 확연히 줄여서 시간초과를 방지하는게 주요 해결 문제였다.
cnt의 초기값을 -1로 설정하는 이유는 이전 칸이 이미 탐색한 칸임에도 카운트가 0인 경우가 있기 때문이다.
만약 초기값을 0으로 했다면, 값을 가져오는 조건을 0보다 큰경우로 설정해야 한다.
그러나 이 경우 탐색을 했음에도 리턴 값이 0일 경우를 최대 4번이나 중복 탐색하게 된다.
따라서 따로 sum 변수에 합을 계산하고 탐색이 끝나면 sum을 cnt에 저장하는 방식을 사용했다.
이러면 탐색이 끝났을 경우 cnt에 0이 저장되기 때문에 DP에 활용 할 수 있다.

그 외에는 전형적인 DFS 탐색방식이다.
*/
