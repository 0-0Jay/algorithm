// 백준 14501번 퇴사 : https://www.acmicpc.net/problem/14501

#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;

int n, cost[16];

int main(){
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int t, p;
		scanf("%d%d", &t, &p);
		p += cost[i];
		for (int j = t + i; j <= n; j++) {
			if (cost[j] < p) cost[j] = p;
		}
	}
	printf("%d", cost[n]);
}

// 알고리즘 : 동적계획법(DP)
/*
풀이 : 각 일자별 기간과 가격을 입력받아 해당 기간 이후의 값과 비교하면서 채워넣는다
1일차에 들어온 상담이 3일동안 이루어지고 20을 준다면 4일차부터 20을 모두 채워넣는다
2일차에 들어온 상담이 2일동안 이루어지고 30을 준다면 4일차부터 마지막 날까지 가격을 보고 더 높은 가격으로 교체한다
4일차에 들어온 상담이 2일동안 이루어지고 20을 준다면 4일차에는 위 과정에 의해 이미 30이 저장되어 있다.
그럼 30 + 20인 50을 6일차부터 채워넣는 방식으로 해결했다.
*/
