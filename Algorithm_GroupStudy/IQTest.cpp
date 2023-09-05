// 백준 1111번 IQ Test : https://www.acmicpc.net/problem/1111

#include<stdio.h>
#include<algorithm>
using namespace std;

int arr[101];

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	if (n == 1 || n == 2 && arr[1] != arr[0]) {  // 만약 항이 1개 또는 항이 2개인데 다른 수로 이루어져 있을 경우 가능한 숫자는 2개 이상 
		printf("A");
		return 0;
	}
	int a = (arr[1] != arr[0]) ? (arr[2] - arr[1]) / (arr[1] - arr[0]) : 0;  // (3번 - 2번) / (2번 - 1번)을 곱할 수에 저장
	int b = arr[1] - arr[0] * a;  // 2번 - 1번 * a를 b에 저장
	int i;
	for (i = 0; i < n - 1; i++) {  // 반복문을 돌면서 한 번이라도 위에서 구한 a*n + b 조건에 맞지 않을 경우 가능한 숫자는 없음 
		if (arr[i] * a + b != arr[i + 1]) {
			printf("B");
			return 0;
		}
	}
	if (i == n - 1) printf("%d", arr[i] * a + b);  // 반복문을 끝까지 순회했다면, 다음 숫자 출력
	return 0;
}

// 알고리즘 : 완전탐색
/*
풀이
