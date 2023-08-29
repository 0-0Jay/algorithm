// 백준 2133번 타일 채우기 : https://www.acmicpc.net/problem/2133

#include<stdio.h>
#include<algorithm>
using namespace std;

int arr[31] = { 0, 0, 3, 0, 11, 0, };  // 점화식 도출 이후, 최소 필요항을 제외한 항 제거(메모리 절약)

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 6; i <= n; i+=2) {
		arr[i] = arr[i - 2] * 4 - arr[i - 4];
	}
	printf("%d", arr[n]);
	return 0;
}

