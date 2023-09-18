// 백준 7570번 줄 세우기 : https://www.acmicpc.net/problem/7570

#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;

int n, arr[1000001], m, cnt[1000001];

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
		cnt[arr[i]] = 1;
		if (cnt[arr[i] - 1] > 0) {
			cnt[arr[i]] = max(cnt[arr[i]], cnt[arr[i] - 1] + 1);
		}
		m = max(cnt[arr[i]], m);
	}
	printf("%d", n - m);
}

// 알고리즘 : DP + 그리디
/* 풀이 : 각 숫자 -1의 카운트를 가져오는 방법

*/
