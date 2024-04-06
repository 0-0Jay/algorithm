// 백준 2638번 치즈 : https://www.acmicpc.net/problem/2638

#include<stdio.h>
#include<algorithm>
#include<queue>
#define M 102
using namespace std;

struct tmp {
	int x, y;
};

int n, m, cheeze[M][M], chk[M][M], cnt[M][M], dx[4] = { 1, 0, -1, 0 }, dy[4] = { 0, 1, 0, -1 }, remain, time;

int main() {
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &cheeze[i][j]);
			if (cheeze[i][j] == 1) remain++;  // 잔여 치즈량을 계산하기 위해 미리 치즈 총량을 변수에 저장
		}
	}
	while (remain > 0) {  // 잔여 치즈가 있으면 계속 수행
		time++;  // 매 수행마다 시간 1씩 누적
		queue<tmp> que;  // 매 수행마다 큐와 chk를 초기화하여 이전의 탐색이 현재 탐색에 영향을 주지 않게 설정
		que.push({ 0,0 });
		fill(&chk[0][0], &chk[n][m], 0);
		chk[0][0] = 1;
		while (!que.empty()) {  // 공기를 기준으로 BFS 순회
			tmp now = que.front();
			que.pop();
			for (int i = 0; i < 4; i++) {
				int nx = now.x + dx[i];
				int ny = now.y + dy[i];
				if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
					if (cheeze[nx][ny] == 1) {  // 만약 치즈를 만나면 해당 치즈에 공기접촉 횟수(cnt)를 카운팅
						cnt[nx][ny]++;
					}
					else {  // 빈공간이면 수행
						if (chk[nx][ny] == 0) {  // 중복 방문 체크, 큐에 다음 탐색 공간으로 삽입
							chk[nx][ny] = 1;
							que.push({ nx,ny });
						}
					}
				}
			}
		}
		for (int i = 0; i < n; i++) {  // 한 번의 BFS 순회가 끝날때마다 전체 치즈 탐색
			for (int j = 0; j < m; j++) {
				if (cnt[i][j] > 1) {  // 만약 cnt가 2이상이면 그 좌표에 해당하는 cheeze를 0으로 제거하고 잔여 치즈량 삭감
					cheeze[i][j] = 0;
					remain--;
				}
				cnt[i][j] = 0;  // 동시에 cnt도 0으로 초기화
			}
		}
	}
	printf("%d", time);  // 잔여치즈가 다 사라진 시점의 time 출력
	return 0;
}
