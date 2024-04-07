백준 1932번 정수 삼각형 : https://www.acmicpc.net/problem/1932

#include <stdio.h>
#include <algorithm>
#define M 501
using namespace std;

int tri[M][M], maxSum;

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			scanf("%d", &tri[i][j]);  // 현재 위치의 데이터 저장
			tri[i][j] += max(tri[i - 1][j], tri[i - 1][j - 1]);  // 윗줄에서 왼쪽과 오른쪽 중 더 큰 수를 현재 칸에 합산
			if (maxSum < tri[i][j]) maxSum = tri[i][j];  // 최대합 계산
		}
	}
	printf("%d", maxSum);
	return 0;
}

// 알고리즘 : DP
