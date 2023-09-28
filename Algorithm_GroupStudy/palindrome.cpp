// 백준 10942번 팰린드롬? : https://www.acmicpc.net/problem/10942

#include <stdio.h>
#include <algorithm>
#include <iostream>
using namespace std;

int n, arr[2001], chk[2001][2001], m;

int main() {
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &arr[i]);
	}
	for (int i = 1; i <= n; i++) {
		chk[i][i] = 1;  // 1자리인 경우
		if (i < n && arr[i] == arr[i + 1]) {  // 2자리인 경우
			chk[i][i + 1] = 1;
		}
	}
	for (int k = 3; k <= n; k++) {  // 3자리 이상
		for (int i = 1, j = k; j <= n; i++, j++) {
			if (arr[i] == arr[j]) chk[i][j] = chk[i + 1][j - 1];
			else chk[i][j] = 0;
		}
	}
	scanf("%d", &m);
	for (int i = 0; i < m; i++) {
		int s, e;
		scanf("%d%d", &s, &e);
		printf("%d\n", chk[s][e]);
	}
}

// 알고리즘 : 동적계획법(DP)
/*
풀이 : a~b 구간이 팰린드롬이려면 a == b이고, a+1 ~ b-1구간이 팰린드롬이어야 하는 규칙을 사용한다.

예를 들어 1213121의 경우,
1. 양끝이 같고 : 1과 1이니 같음
2. 21312가 팰린드롬이어야 한다.

이를 DP를 위한 배열에 활용하기위해 초기값으로 1자리와 2자리의 경우에 팰린드롬 여부를 구한다.
1자리 수는 무조건 팰린드롬이니 1로 체크하고, 2자리 수는 두 수가 같으면 1, 아니면 0으로 체크한다.
3자리 수부터는 양 끝에서 한자리씩 줄였을 경우의 칸에 갔을때 체크된 수가 1이고, 양끝의 숫자가 같으면 1로 체크한다.
그 외의 경우는 모두 0으로 체크한다.

팰린드롬 여부를 모두 구했다면 각 질의 칸에 저장된 1/0을 출력한다.
*/
