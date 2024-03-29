// 백준 1260번 DFS와 BFS : https://www.acmicpc.net/problem/1260

#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;

queue<int> que;
vector<int> arr[1001];
int chk[1001];
int n, m, v;

void BFS(int k) {
	que.push(k);
	chk[k] = 1;
	while (!que.empty()) {
		int now = que.front();
		printf("%d ", now);
		que.pop();
		for (int i = 0; i < arr[now].size(); i++) {
			if (chk[arr[now][i]] == 0) {  // 중복 방문으로 인한 무한 루프 방지
				chk[arr[now][i]] = 1;
				que.push(arr[now][i]);
			}
		}
	}
}

void DFS(int k) {
	for (int i = 0; i < arr[k].size(); i++) {
		if (chk[arr[k][i]] == 0) {  // 중복 방문으로 인한 무한 루프 방지
			chk[arr[k][i]] = 1;
			printf("%d ", arr[k][i]);
			DFS(arr[k][i]);
		}
	}
	return;
}

int main() {
	scanf("%d %d %d", &n, &m, &v);
	for (int i = 0; i < m; i++) {
		int a, b;
		scanf("%d%d", &a, &b);
		arr[a].push_back(b);
		arr[b].push_back(a);
	}
	for (int i = 1; i <= n; i++) {
		sort(arr[i].begin(), arr[i].end());  // 각 벡터 오름차순으로 정렬
	}
	printf("%d ", v);
	chk[v] = 1;
	DFS(v);
	printf("\n");
	fill(chk, chk + 1001, 0);  // 하나의 체크배열을 사용하므로 BFS 전에 체크 배열 0으로 초기화
	BFS(v);
	return 0;
}

// 알고리즘 : DFS, BFS
//풀이 : DFS와 BFS를 구현해본다.
