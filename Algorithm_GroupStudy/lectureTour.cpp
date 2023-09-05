// 백준 2019번 순회강연 : https://www.acmicpc.net/problem/2109

#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;

struct tmp {
	int cost, to;
};

int chk(tmp i, tmp j) {
	return i.to < j.to || i.to == j.to && i.cost < j.cost;
}

vector<tmp> arr;
int cost[10001], sum, last;

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int a, b;
		scanf("%d%d", &a, &b);
		arr.push_back({ a, b });
		if (last < b) last = b;  // 불필요한 탐색을 방지하기 위해 최대 일수 계산
	}
	sort(arr.begin(), arr.end(), chk);  // arr를 날짜순으로 정렬 및 같은 날짜는 비용순으로 정렬
	for (int i = 0; i < n; i++) {
		if (cost[arr[i].to] <= arr[i].cost) {  // 현재 탐색중인 강연의 비용이 해당 날짜의 기존 비용보다 높으면 교체 시작
			int minV = cost[arr[i].to], midx = 0;
			int t = minV;
			for (int j = 1; j < arr[i].to; j++) {  // 처음부터 현재 탐색중인 날짜까지 중 최소 비용 탐색
				if (minV > cost[j]) {
					minV = cost[j];
					midx = j;
				}
			}
			if(cost[midx] < t) cost[midx] = t;  // 탐색한 최소 비용이 현재 날짜에 있던 비용보다 작을 경우에만 교체
		}
		cost[arr[i].to] = arr[i].cost;  // 교체가 끝나면 현재 날짜에 현재 탐색중인 강연의 비용 저장
	}
	for (int i = 1; i <= last; i++) {
		sum += cost[i];  // 모든 교체가 끝나면 전체 합 출력
	}
	printf("%d", sum);
	return 0;
}

// 알고리즘 : 그리디(탐욕법)
/*
풀이 : 주어진 강연과 마감일자를 정렬해서 각 일자내에 최고가로 배치
최소 일부터 시작해서 강연비를 삽입
만약 탐색중인 강연의 비용이 해당 날짜에 저장되어 있는 비용보다 높으면 교체하고 기존 비용을 따로 추출
추출한 비용을 이전까지의 날짜중 최소 비용을 가진 날짜와 비교해서 더 높은 값으로 교체
*/
