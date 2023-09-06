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

// 알고리즘 : 바이너리 서치(이분탐색)
/*
풀이 : 최대거리를 증감하면서 가장 짧은 최대거리를 탐색

l을 1(가능한 최단거리) r을 999(도로의 최대 길이)로 하여 mid를 구한다.
각 구간에 mid 길이마다 휴게소를 설치하면서 그 수를 카운팅(tmp)한다.
tmp가 설치해야하는 수(m)보다 크면 mid 길이를 늘려서 수를 줄이기 위해 l을 mid+1로 올린다.
tmp가 m보다 작으면 mid 길이를 줄여서 수를 늘려야 하므로 r을 mid-1로 내린다.
만약 tmp가 m과 같은경우, 가능한 가장 짧은 최대거리를 구해야하므로 r을 한 번 더 내려서 가능한지 확인한다.
위 코드에서는 while문 마지막 if문의 조건을 tmp > m으로 주고 그외에는 else로 내리는 것으로 처리했다.
*/
