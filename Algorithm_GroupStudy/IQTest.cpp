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

// 알고리즘 : 브루트포스(완전탐색)
/*
풀이 : 수열이 주어질때마다 다음에 올 수 있는 수가 많은 경우, 하나인 경우, 없는 경우를 모두 고려
복잡한 완전탐색 문제처럼 보이지만 수열의 규칙을 알고 있으면 간단하다.

항이 1개일 경우, 다음에는 어떤 수가 오든 수열을 만들 수 있으니 A
항이 2개일 경우, 두 수가 다르면 수많은 경우의 수열을 만들 수 있으니 A지만 두 수가 같으면 무조건 똑같은 수만 올 수 있으니 해당 수를 출력
항이 3개 이상일 경우, 만약 수열의 규칙을 만족한다면 다음에 올 수 있는 수는 1개로 고정되기 때문에 해당 수 출력.
항이 3개 이상이지만, 규칙성이 없는 수열이라면 다음에 올 수 있는 수는 알 수 없으므로 B 출력
*/
