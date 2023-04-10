// 외양간 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1089&sca=3050

#include <stdio.h>
#include <algorithm>
using namespace std;

int arr[200], dist[200];

int main() {
	int m, s, c;
	scanf("%d%d%d", &m, &s, &c);
	for (int i = 0; i < c; i++) {
		scanf("%d", &arr[i]);
	}
	sort(arr, arr + c);  // #1
	s = arr[c - 1] - arr[0] + 1;  // #2
	for (int i = 0; i < c - 1; i++) {
		dist[i] = arr[i + 1] - arr[i] - 1;
	}
	sort(dist, dist + c);
	for (int i = 1; i < m; i++) {  // #3
		s -= dist[c - i];
		if (i >= c) break;
	}
	printf("%d", s);
}

// arr은 소가 있는 우리를 저장할 배열, dist는 우리 사이의 거리를 저장할 배열
// 판자의 총 길이를 최소화하려면 각 우리의 거리를 재서 긴 거리 m-1(판자 개수 - 1)개를 빼는 방법을 사용했다. 판자가 4개라면 판자 간 빈 공간은 3개이다.
// #1 가장 긴 거리부터 빼기 위해 각 우리 사이의 거리를 오름차순으로 정렬했다.
// #2 가장 왼쪽에 있는 우리와 가장 오른쪽에 있는 우리 사이에만 판자가 필요하기 때문에 s에 이를 저장했다.
//    예를 들어, 전체 우리가 20이고 소가 있는 우리 중 가장 왼쪽에 있는 우리 번호가 3, 가장 오른쪽에 있는 우리 번호가 17이라면 다음과 같다
//    s = 17 - 3 - 1 = 13.
//    이를 통해 0 ~ 3까지와 17 ~ 20까지 판자가 불필요한 공간을 배제할 수 있다.
// #3 #1에서 정렬해놓은 dist배열의 가장 오른쪽에서 부터 m-1개 만큼 s에서 빼주었다.
