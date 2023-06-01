// 바이러스 : https://www.acmicpc.net/problem/2606

#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> arr[110];
int chk[110], que[110], st = -1, ed = -1, cnt;

int main() {
	int n, m;
	scanf("%d%d", &n, &m);
	for (int i = 0; i < m; i++) {
		int a, b;
		scanf("%d%d", &a, &b);
		arr[a].push_back(b); arr[b].push_back(a);  // #1
	}
	que[++st] = 1, chk[1] = 1;  // #2
	while (st != ed) {
		int now = que[++ed];
		for (int i : arr[now]) {
			if (chk[i] == 0) {  // #3
				que[++st] = i;
				chk[i] = 1;
				cnt++;
			}
		}
	}
	printf("%d", cnt);
}

// #1 백터의 a행에 b를, b행에 a를 push하여 두 컴퓨터의 네트워크가 연결되어 있음을 저장했다.
// #2 bfs를 활용했다. 큐에 1번 컴퓨터를 넣고, 컴퓨터를 중복 탐색하지 않게 chk배열에 체크했다.
// #3 큐에서 컴퓨터 하나를 꺼내서 해당 컴퓨터와 연결된 컴퓨터들 중 탐색하지 않은 곳을 큐에 추가, chk로 체크, cnt로 카운팅 해주었다.
