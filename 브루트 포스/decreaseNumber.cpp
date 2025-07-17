// 백준 1038번 감소하는 수 : https://www.acmicpc.net/problem/1038

#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;

long long int now, decr[1022] = { 0, };
int n, st = 0, ed = 0;

int main() {
	scanf("%d", &n);
	for (int i = 1; i < 10; i++) {
		decr[++st] = i;
	}
	while (st != ed && st < 1022) {
		now = decr[++ed];
		for (int i = 0; i < now % 10; i++) {
			if (st < 1022) decr[++st] = now * 10 + i;
		}
	}
	if (n > 1022) printf("-1");
	else if (n < 1022) printf("%lld", decr[n]);
	else printf("9876543210");
}

// 알고리즘 : 브루트 포스(완전 탐색)
/* 풀이 : 중복되는 연산을 최소화하여 시간을 줄인다.
매 탐색마다 현재 숫자의 1의 자리수보다 작은 수를 뒤에 붙인다.
모든 감소하는 수는 오름차순으로 번호가 매겨지기 때문에
0부터 1개씩 넣다가 1의 자릿수가 되면 빠져나오는 방법으로 해결했다.

long long int가 int64로 9876543210을 수용할 수 있을 거라 생각했는데 OS 별로 long long 타입의 크기가 다를 수 도 있다는 조언을 얻었다.
여러 환경에서 테스트 해보니 987654321 이후의 숫자는 망가지는 것을 확인했고, 9876543210만 따로 처리해주었다.
*/
