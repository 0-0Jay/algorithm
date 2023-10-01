// 백준 1781번 컵라면 : https://www.acmicpc.net/problem/1781

#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct tmp {
	int dead, ramen;
};

int chk(tmp i, tmp j) {
	return i.dead < j.dead;
}

int n, a, b, cnt;
vector<tmp> arr;
priority_queue<int, vector<int>, greater<int>> pq;

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &a, &b);
		arr.push_back({ a, b });
	}
	sort(arr.begin(), arr.end(), chk);  // 데드라인을 오름차순으로 정렬
	for (int i = 0; i < n; i++) {
		if (pq.size() < arr[i].dead) {  // pq의 사이즈를 일수로 생각
			pq.push(arr[i].ramen);
		}
		else {
			if (pq.top() < arr[i].ramen) {
				pq.pop();
				pq.push(arr[i].ramen);
			}
		}
	}
	while (!pq.empty()) {
		cnt += pq.top();
		pq.pop();
	}
	printf("%d", cnt);
}

// 알고리즘 : 그리디(탐욕법)
/*
풀이 : 우선순위 큐를 사용하여 라면갯수와 데드라인을 비교하여 최대 갯수 계산
우선순위 큐(pq)의 비교연산자를 greater로 주어서 top에 가장 적은 라면의 갯수가 올라오게 한다.
pq의 size를 일수로 생각하기 때문에 pq에 값이 변경되는 과정은 두가지다.
1. pq의 size(일수)보다 dead가 크면 그냥 pq에 ramen 값을 넣는다(size가 1 증가하므로 일수도 1 증가한다고 생각한다.)
2. pq의 size보다 dead가 작거나 같으며 pq의 top에 있는 ramen보다 현재 ramen이 크다면 둘을 교체한다.
  2-1. pq의 연산자인 greater로 인해 항상 가장 작은 수의 라면이 top에 존재하기 때문에 이를 pop하고 현재 라면 갯수를 push 한다.

모든 탐색이 끝나면 pq에 들어있는 모든 라면 갯수를 cnt에 누적한다.
*/
