// 백준 2839 설탕 배달 : https://www.acmicpc.net/problem/2839

#include <stdio.h>
#include <algorithm>
using namespace std;

int cnt[5001];

int main() {
	int n;
	scanf("%d", &n);
	cnt[3] = 1;  // 3kg와 5kg에 미리 1을 저장
	cnt[5] = 1;
	for (int i = 6; i <= n; i++) {
		int min = 5000;
		if (cnt[i - 3] != 0 && cnt[i - 3] < min) min = cnt[i - 3] + 1;  // (i - 3)kg에 3kg를 1개 추가하는 방법
		if (cnt[i - 5] != 0 && cnt[i - 5] < min) min = cnt[i - 5] + 1;  // (i - 5)kg에 5kg를 1개 추가하는 방법
		if (cnt[i - 3] == 0 && cnt[i - 5] == 0) continue;  // 만약 (i - 3)kg도, (i - 5)kg도 만들 수 없는 무게라면 continue;
		cnt[i] = min;  // 위에서 계산한 내용중 최소값을 cnt[i]에 저장
	}
	printf("%d", (cnt[n] == 0)? -1 : cnt[n]);  // 만약 cnt[n]이 0이면 만들수 없는 무게이므로 -1, 아니면 cnt[n] 그대로 출력
	return 0;
}

// 알고리즘 : 그리디 + DP
// 풀이 : 각무게에 3kg가 추가된 경우, 5kg가 추가된 경우의 최소값을 계산하여 cnt에 저장한다.
// 예를 들어 16kg일 경우, 13kg의 봉지수에 3kg의 봉지 하나를 더한 값과, 11kg의 봉지수에 5kg 봉지 하나를 더한 값을 비교한다.
