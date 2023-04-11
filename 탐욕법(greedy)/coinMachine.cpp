// 동전 자판기 : http://www.jungol.co.kr/theme/jungol/status4.php?fid=youngjin2712

#include<stdio.h>

int arr[6], cost[6] = { 500, 100, 50, 10, 5, 1 };  // #1

int main() {
	int n, sum = 0, cnt = 0;
	scanf("%d", &n);
	for (int i = 0; i < 6; i++) {
		scanf("%d", &arr[i]);
		cnt += arr[i];
		sum += cost[i] * arr[i];  // #2
	}
	sum -= n;
	for (int i = 0; i < 6; i++) {
		while (sum - cost[i] >= 0 && arr[i] > 0) {  // #3
			sum -= cost[i]; arr[i]--; cnt--;
		}
	}
	printf("%d\n", cnt);
	for (int i = 0; i < 6; i++) {
		printf("%d ", arr[i]);
	}
}

// #1 cost에 각각 500~1원까지의 정보를 순서대로 저장해서 if문을 사용하지 않고 이중 반복문으로 풀 수 있게 만들었다.
// #2 n원을 만들기 위해 가장 많은 동전을 사용한다는 뜻은 (모든 동전의 총 금액 - n)을 만들기 위해 가장 적은 동전을 사용한다는 뜻과 같다.
//    따라서 sum에 모든 동전의 금액을, cnt에 모든 동전의 개수를 저장했다.
// #3 어떤 금액을 구하기 위해 최소의 동전을 사용하는 방법은 가장 비싼 동전부터 사용하는 방법이다.
