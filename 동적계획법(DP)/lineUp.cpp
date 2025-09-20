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
	printf("%d", n - m);  // 가장 긴 부분수열의 길이를 전체 길이에서 뺀 값
}

// 알고리즘 : DP + 그리디
/* 
풀이 : 각 숫자 -1의 카운트를 가져오는 방법
등차가 1인 부분 수열을 뽑아서 그중에 가장 긴 부분수열을 제외한 나머지 숫자를 순서대로 옮긴다.
5 2 4 1 3 을 예로 들면,
가장 긴 부분 수열은 2 3이 된다.
따라서 2, 3을 제외한 나머지 숫자 3개를 옮기는 것이 가장 최소로 옮기는 방법이 된다.
옮겨야 하는 수의 개수만 알면 그 갯수만큼 순서대로 옮기면 해결되기 때문에 옮기는 순서는 고려하지 않아도 해결할 수 있다.
*/
