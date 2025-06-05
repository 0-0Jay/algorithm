백준 14888번 연산자 끼워넣기 : https://www.acmicpc.net/problem/14888

#include <stdio.h>
#include <algorithm>
using namespace std;

int arr[11], maxRes = -0x7fffffff, minRes = 0x7fffffff, n, cal[4];

void DFS(int d, int res) {
	if (d == n) {  // d가 n과 같아지면 최대값, 최소값 계산
		if (maxRes < res) maxRes = res;
		if (minRes > res) minRes = res;
		return;
	}
	if (cal[0] > 0) {  // 덧셈 (각 연산자당 남은 갯수가 0이 될때까지 탐색)
		cal[0]--;
		DFS(d + 1, res + arr[d]);
		cal[0]++;
	}
	if (cal[1] > 0) {  // 뺄셈
		cal[1]--;
		DFS(d + 1, res - arr[d]);
		cal[1]++;
	}
	if (cal[2] > 0) {  // 곱셈
		cal[2]--;
		DFS(d + 1, res * arr[d]);
		cal[2]++;
	}
	if (cal[3] > 0) {  // 나눗셈
		cal[3]--;
		DFS(d + 1, res / arr[d]);
		cal[3]++;
	}
}

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	for (int i = 0; i < 4; i++) {
		scanf("%d", &cal[i]);
	}
	DFS(1, arr[0]);
	printf("%d\n%d", maxRes, minRes);
	return 0;
}

// 알고리즘 : 브루트포스
/*
풀이 : DFS로 연산자를 브루트포스 탐색하면서 최댓값과 최솟값을 계산한다.
*/
