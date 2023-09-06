// 백준 1477번 휴게소 세우기 : https://www.acmicpc.net/problem/1477

#include<stdio.h>
#include<algorithm>
using namespace std;

int n, m, road, loc[101], minV = 1000, dis[101], l = 1, r = 999, mid;

int main(){
	scanf("%d%d%d", &n, &m, &road);
	for (int i = 1; i <= n; i++) {  // i를 1부터 시작하여 loc[0]은 자동으로 0
		scanf("%d", &loc[i]);
	}
	loc[n + 1] = road;  // 도로의 끝도 loc에 저장
	sort(loc, loc + n + 1);  // 각 휴게소 간 거리를 저장하기 위해 오름차순 정렬
	for (int i = 0; i <= n; i++) {
		dis[i] = loc[i + 1] - loc[i] - 1;  // 휴게소가 없는 구간의 길이를 dis배열에 저장
	}
	while (l <= r) {
		mid = (l + r) / 2;
		int tmp = 0;
		for (int i = 0; i <= n; i++) {
			tmp += dis[i] / mid;  // 각 구간의 길이에 mid가 몇번 들어갈 수 있는지 카운팅
		}
		if (tmp > m) l = mid + 1;  // tmp가 m보다 크면 거리를 길게, 작으면 짧게하여 탐색 
		else r = mid - 1;
	}
	printf("%d", l);
}
