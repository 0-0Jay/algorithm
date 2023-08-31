백준 11048번 이동하기 : https://www.acmicpc.net/problem/11048

#include<stdio.h>
#include<algorithm>
using namespace std;

int maze[1001][1001], n, m;

int main() {
	scanf("%d%d", &n, &m);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			int c;
			scanf("%d", &c);  // 현재 위치 사탕 변수에 임시 저장
			maze[i][j] = max(c + maze[i - 1][j], (max(c + maze[i][j - 1], c + maze[i - 1][j - 1])));  // 이전 방중 가장 높은 숫자 누적
		}
	}
	printf("%d", maze[n][m]);  // 마지막 방 반환
	return 0;
}
