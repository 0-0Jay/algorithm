// 백준 1010번 다리 놓기 : https://www.acmicpc.net/problem/1010

#include<stdio.h>
#include<algorithm>
using namespace std;

long long int bridge[30][30];

int main(){
	for (int i = 0; i < 30; i++) {
		bridge[0][i] = 1;  // dp 계산을 위해 0번 인덱스에 기본값 1 저장
	}
	for (int i = 1; i < 30; i++) {
		for (int j = i; j < 30; j++) {
			bridge[i][j] = bridge[i - 1][j - 1] + bridge[i][j - 1];  // 파스칼의 삼각형으로 조합 계산 단순화

		}
	}
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int l, r;
		scanf("%d%d", &l, &r);
		printf("%lld\n", bridge[l][r]);
	}
}
