// 백준 2565번 : https://www.acmicpc.net/problem/2565

#include<stdio.h>
#include<algorithm>
using namespace std;

struct tmp {
	int l, r, cnt;
};

int chk(tmp i, tmp j) {
	return i.l < j.l;
}

tmp arr[510];
int tMax, res;

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int a, b;
		scanf("%d%d", &a, &b);
		arr[i] = { a, b, 1 };
	}
	sort(arr, arr + n, chk);  // 시작점(l)을 오름차순으로 정렬
	for (int i = 0; i < n; i++) {
		tMax = 0;
		for (int j = 0; j < i; j++) {
			if (arr[i].r > arr[j].r) {  // 0번 인덱스부터 탐색하여 끝점(r)이 현재 탐색중인 줄의 끝점 보다 작은 줄의 cnt 중 가장 큰 값을 저장
				if(tMax < arr[j].cnt) tMax = arr[j].cnt;
			}
			arr[i].cnt = tMax + 1;  // 현재 탐색중인 줄의 cnt에 tMax + 1(자기자신) 누적
			if (arr[i].cnt > res) res = arr[i].cnt;  // cnt들 중 최대값이 곧 가능한 최대의 전깃줄 수
		}
	}
	printf("%d", n - res);  // 전체 전깃줄 수 - 최대 가능 전깃줄 수 - 최소로 제거해야하는 전깃줄 수
	return 0;
}

// 알고리즘 : DP(동적계획법)
/*
풀이 : 현재 전깃줄을 시작점 순으로 나열해두고 끝 점만 비교해서 해당 줄의 카운트를 가져온다.
다음 예제의 경우를 살펴보자(미리 시작점 기준 오름차순으로 정렬했다)
8
1 8
2 2
3 9
4 1
6 4
7 6
9 7
10 10
1번 줄의 경우 -> 자기자신 1 = 1
2번 줄의 경우 -> 1번의 끝점(8), 2번의 끝점(2) 배제. -> 현재 최대값 : 0
                현재 최대값 + 현재 줄(1) = 1
3번 줄의 경우 -> 1번의 끝점(8), 3번의 끝점(9) -> 현재 최대값 : 1
                2번의 끝점(2), 3번의 끝점(9) -> 현재 최대값 : 1
                현재 최대값 + 현재 줄(1) = 2
                :
                :
                :
10번 줄의 경우 -> 최대값(4, 6, 7, 9번 줄) + 현재줄(1) = 5
==> 전체 줄 수(8) - 최대 가능 줄(5) = 3 (최소 제거 줄)
*/
