// 정올 - DNA 조합 : https://jungol.co.kr/problem/2217

#include<stdio.h>
#include<string>
using namespace std;

int n, m = 100, check[7];
char arr[7][8];

void dna(string s, int d, string bef) {  // #1
	if (s.length() > m) return;
	if (d == n) {
		if (m > s.length()) m = s.length();
		return;
	}
	for (int i = 0; i < n; i++) {
		if (check[i] == 1) continue;
		string r = arr[i];
		int tmp = 0;
		for (int j = 1; j <= r.length() && j <= bef.length(); j++) {
			if (bef.substr(bef.length() - j, j) == r.substr(0, j)) tmp = j;
		}
		check[i] = 1;
		dna(s + r.substr(tmp),d + 1, r);
		check[i] = 0;
	}
	return;
}

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", &arr[i]);
	}
	dna("", 0, "");
	printf("%d", m);
}

// 알고리즘 : DFS
/*
풀이 : substr함수를 활용해 두 문자열의 겹치는 길이를 검사한다.
빈 문자열로 시작해서 주어진 문자열들을 하나씩 겹친다.
이 때, 이미 사용한 문자열은 사용하지 않기 위해 check배열을 활용하여 방문체크를 해준다.
반복문을 사용하여 왼쪽 문자열의 오른쪽 j개와 오른쪽 문자열의 왼쪽 j개를 비요하여 겹칠 수 있는 길이를 찾는다.(tmp)
겹칠 수 있는 길이를 찾았다면, 그만큼 겹친 후 다음 노드로 넘긴다.

모든 문자열을 하나로 연결했다면, 그 문자열의 길이와 m에 저장된 최대 문자열의 길이를 비교해 갱신한다.
*/
