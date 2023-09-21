// 백준 2138번 전구와 스위치 : https://www.acmicpc.net/problem/2138

#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;

int n, s[100001], e[100001], s2[100001], cnt1, cnt2;

int main() {
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		scanf("%1d", &s[i]);
		s2[i] = s[i];
	}
	s2[0] = (s[0]) ? 0 : 1;
	for (int i = 1; i <= n; i++) {
		scanf("%1d", &e[i]);
	}
	for (int i = 1; i <= n; i++) {
		if (s[i - 1] != e[i - 1]) {  // 첫번째 스위치를 안누르는 경우
			s[i - 1] = (s[i - 1]) ? 0 : 1;
			s[i] = (s[i]) ? 0 : 1;
			if(i + 1 <= n) s[i + 1] = (s[i + 1]) ? 0 : 1;
			cnt1++;
		}
		if (s2[i - 1] != e[i - 1]) {  // 첫번째 스위치를 누르는 경우
			s2[i - 1] = (s2[i - 1]) ? 0 : 1; 
			s2[i] = (s2[i]) ? 0 : 1;
			if (i + 1 <= n) s2[i + 1] = (s2[i + 1]) ? 0 : 1;
			cnt2++;
		}
	}
	int i;
	for (i = 1; i <= n; i++) {
		if (s[i] != e[i]) {
			break;
		}
	}
	int j;
	for (j = 1; j <= n; j++) {
		if (s2[i] != e[i]) {
			break;
		}
	}
	if (i > n) printf("%d", cnt1);
	else if (j > n) printf("%d", cnt2);
	else printf("-1");
}

// 알고리즘 : 그리디(탐욕법)
/*
풀이 : 맨 왼쪽 스위치부터 시작해서 바로 직전의 전구를 비교해서 다르면 누르고 같으면 넘긴다.
시작 점을 1번 인덱스로 시작하여 0번인덱스가 0인 경우, 1인 경우 두가지로 나누어 계산한다.
이는 첫번째 스위치를 누르는 경우와 안누르는 경우를 계산하기 위함이다.

가능하면 가능한 경우의 누르는 횟수를, 두가지 모두 불가능하면 -1을 출력한다.
*/
