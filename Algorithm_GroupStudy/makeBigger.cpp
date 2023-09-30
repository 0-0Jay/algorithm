#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;

int stk[500001], t = 0, n, k, now;

int main() {
	scanf("%d %d", &n, &k);
	int total = n - k;  // 넣을 수 있는 숫자 자릿 수
	for (int i = 1; i <= n; i++) {
		scanf("%1d", &now);
		if (t == 0 || stk[t] >= now && t < total) {
			stk[++t] = now;
		}
		else {
			while(stk[t] < now && k > 0 && t > 0) {
				t--;
				k--;
			}
			stk[++t] = now;
		}
	}
	while (k > 0) {
		k--;
		t--;
	}
	
	for (int i = 1; i <= t; i++) {
		printf("%d", stk[i]);
	}
}

// 알고리즘 : 탐욕법(greedy)
/*
풀이 : 숫자를 1자리씩 받아서 이전 숫자와 크기를 비교하며 스택에 쌓는다.
스택에 쌓는 조건은 다음 중 하나다.
1. 스택이 비어있다.
2. 스택의 top에 있는 수가 현재 수(now)보다 작고, 채워넣을 수 있는 자릿수(total)가 남아있다.

만약 위 두 조건에 맞지 않는다면,
지울 수 있는 수(k)가 남아있고, 스택의 크기가 0이 아니면서 스택의 top이 now보다 커질 때까지 숫자를 pop한다.
이 후, now를 스택에 쌓는다.

모든 계산이 끝난 후, 만약 완성된 숫자의 자릿수가 total보다 크다면, 그만큼 1의 자리부터 제거한다.
*/
