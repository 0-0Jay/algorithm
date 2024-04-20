// 백준 2294번 동전 2 : https://www.acmicpc.net/problem/2294

#include<stdio.h>
#include<algorithm>
using namespace std;

int coin[10000], cost[100001];

int main() {
	int n, k;
	scanf("%d %d", &n, &k);
	for (int i = 0; i < n; i++) {
		scanf("%d", &coin[i]);
		cost[coin[i]] = 1;  // 해당 동전의 가격에 동전 1개만 사용하는 경우를 미리 입력
	}
	for (int i = 1; i <= k; i++) {
		int cnt = i + 1;  // cnt에 현재 가격보다 높은 임의의 숫자 부여
		for (int j = 0; j < n; j++) {
			if (i >= coin[j] && i % coin[j] == 0 && cnt > i / coin[j]) cnt = i / coin[j];  // 만약 i가 j번째 동전으로 나누어 떨어지고, 몫이 cnt보다 작으면 cnt 교체
			if (i > coin[j] && cost[i - coin[j]] != 0 && cnt > cost[i - coin[j]] + 1) cnt = cost[i - coin[j]] + 1;  // i - j동전 가격을 만들 수 있는 경우의 수가 존재하고 해당 경우에 j동전을 하나 추가하는 경우가 cnt보다 작으면 cnt 교체
		}
		cost[i] = (cnt <= i) ? cnt:0;  // 만약 cnt가 한번도 교체되지 않았으면 해당 가격에 가능한 경우 0 저장
	}
	printf("%d", (cost[k] > 0)? cost[k] : -1);  // 원하는 가격의 경우의 수가 0이면 -1, 아니면 그 갯수 출력
}
