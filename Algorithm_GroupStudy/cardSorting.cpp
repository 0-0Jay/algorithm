// 백준 1715번 카드 정렬하기 : https://www.acmicpc.net/problem/1715

#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <queue>
using namespace std;

int n, t, sum;
priority_queue<int, vector<int>, greater<int>> q;

int main() {
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &t);
		q.push(t);
	}
	while (q.size() > 1) {
		int a = q.top();
		q.pop();
		int b = q.top();
		q.pop();
		q.push(a + b);
		sum += a + b;
	}
	printf("%d", sum);
}

// 알고리즘 : 그리디
/*
풀이 : 매 탐색에서 가장 작은 카드뭉치 두개를 합쳐야 한다.
우선순위 큐를 오름차순 조건으로 생성해서, 각 카드 뭉치의 크기를 삽입했다.
q의 size가 2이상 일때만 탐색을 수행한다.
왜냐하면 q에 들어간 카드뭉치가 1개라면, 합치는 과정이 필요없기 때문에 0이 반환되어야 하기 때문이다.
q에서 가장 작은 카드뭉치 2개를 꺼내서 합친 후, 다시 q에 삽입한다.
이 때, 합친 카드뭉치의 크기를 sum에 누적한다.
합치는 것을 반복하다가 카드 뭉치의 갯수가 1개가 되면 자연스레 반복문이 종료되고, sum이 출력된다.
*/
