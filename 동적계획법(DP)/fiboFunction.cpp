// 백준 1003번 피보나치 함수 : https://www.acmicpc.net/problem/1003

#include<stdio.h>
#include<algorithm>
using namespace std;

int n, fibo[50][2] = { {1, 0}, {0, 1}, };  // 각각 0인 경우, 1인 경우의 초기값 저장

int main(){
	scanf("%d", &n);
	for (int i = 2; i <= 40; i++) {  // 미리 40항까지 [0]에 0이 호출되는 횟수, [1]에 1이 호출되는 횟수를 저장
		fibo[i][0] = fibo[i - 2][0] + fibo[i - 1][0];  // 피보나치 수열에서 i항의 0과 1이 호출되는 횟수는 i-2항과 i-1항의 횟수의 합
		fibo[i][1] = fibo[i - 2][1] + fibo[i - 1][1];
	}
	for (int i = 0; i < n; i++) {
		int a;
		scanf("%d", &a);
		printf("%d %d\n", fibo[a][0], fibo[a][1]);
	}
}
