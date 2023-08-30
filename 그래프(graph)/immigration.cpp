// 백준 16234번 인구 이동 : https://www.acmicpc.net/submit/16234

#include<stdio.h>
#include<algorithm>
#include<queue>
using namespace std;

int n, l, r, arr[50][50], tmp[50][50], chk[50][50], dx[4] = { 1, 0, -1, 0 }, dy[4] = { 0, 1, 0, -1 }, cnt, t, flag;

void BFS(int x, int y) {
	int tmpSum = 0;
	vector<pair <int, int>> loc;
	queue<pair<int, int>> que;
	que.push({ x, y });
	while (!que.empty()) {
		pair<int, int> now = que.front();
		tmpSum += arr[now.first][now.second];  // BFS를 수행하면서 연합 소속 국가의 인구수 누적
		loc.push_back({ now.first, now.second });  // 맵을 다시 순회할 필요없게 연합 소속 국가의 x,y값을 벡터에 저장
		que.pop();
		for (int i = 0; i < 4; i++) {
			int a = now.first + dx[i];
			int b = now.second + dy[i];
			int c = abs(arr[a][b] - arr[now.first][now.second]);
			if (a > -1 && a < n && b > -1 && b < n && chk[a][b] == 0 && c >= l && c <= r) {
				chk[a][b] = t;  // 범위 내의 l이상 r이하에 chk에 t를 적어 연합 소속임을 표시(중복 탐색 방지)
				flag = 1;  // 연합이 발생했으므로 flag를 동작
				que.push({ a, b });
			}
		}
	}
	int div = (int)(tmpSum / loc.size());  // 연합 국가의 평균 인구
	for (int i = 0; i < loc.size(); i++) {
		tmp[loc[i].first][loc[i].second] = div;  // tmp에 각 연합 소속 국가에 div를 저장
	}
}

int main() {
	scanf("%d%d%d", &n, &l, &r);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &arr[i][j]);
		}
	}
	flag = 1;
	while (flag) {  // flag를 while문 진입 즉시 0으로 설정, 탐색 중 인구이동이 발생하면 flag 동작
		flag = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (chk[i][j] == 0) {
					t++;
					chk[i][j] = t; // 방문한 국가는 t를 입력해 중복탐색 방지
					BFS(i, j);
				}
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				arr[i][j] = tmp[i][j];  // 모든 BFS가 동작했으면 arr에 tmp의 이동한 인구수를 업데이트
				chk[i][j] = 0;  // chk는 다음 방문에 영향을 주지않게 0으로 초기화
			}
		}
		cnt++;  // while이 한번 동작할때마다 카운팅
	}
	printf("%d", cnt - 1);  // flag가 동작하지않아 while문을 빠져나오기전에 cnt가 한번 더 카운팅되기 때문에 1회 차감해줌
	return 0;
} 
