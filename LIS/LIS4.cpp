// 백준 14002번 가장 긴 증가하는 부분수열 4 : https://www.acmicpc.net/problem/14002
// LIS : Longest Increasing Subsequence

#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int n, arr[1001][3], ml, t = 1;// 0 : 숫자, 1 : 최대 길이, 2: 이전 수 
vector<int> v;

int main() {
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &arr[i][0]);
		arr[i][1] = 1;
		if (ml < arr[i][1]) ml = arr[i][1];
		for (int j = 1; j < i; j++) {
			if (arr[j][0] < arr[i][0] && arr[i][1] < arr[j][1] + 1) {  // 이전 숫자들중 가장 긴 수열을 가진 수의 인덱스 탐색
				arr[i][1] = arr[j][1] + 1;
				arr[i][2] = j;
				if (arr[i][1] > ml) {  // 현재까지 가장 긴 수열과 그 인덱스
					ml = arr[i][1];
					t = i;
				}
			}
		}

	}
	while (t > 0) {  // t를 활용해 역추적하면서 벡터에 삽입
		v.push_back(arr[t][0]);
		t = arr[t][2];
	}
	printf("%d\n", ml);
	while (!v.empty()) {  // 벡터를 back부터 역방향 출력
		printf("%d ", v.back());
		v.pop_back();
	}
}

// 알고리즘 : 동적계획법(DP)
/*
풀이 : 입력을 받으면 이전까지의 수들 중 가장 긴 증가하는 부분수열의 길이와 해당 좌표의 인덱스를 가져온다.
수를 입력받으면 현재 인덱스 - 1 까지의 숫자들 중 현재 입력받은 수보다 작으면서 가장 길이가 긴 수를 찾는다.
그 수의 인덱스와 , 저장된 길이 + 1을 각각 2번, 1번 인덱스에 저장한다.
저장하면서 현재까지 발견 최대 길이(ml)와 최대 길이를 가진 수의 인덱스(t)를 따로 저장해둔다.

모든 탐색이 완료되면 vector(stack을 사용해도 무관하다)와 방금 저장했던 t를 이용해 arr을 역추적하여 가져온다.
vector의 back에는 그 수열에서 가장 작은 수가 들어있으므로 back부터 역순으로 pop_back하여 출력한다.
*/
