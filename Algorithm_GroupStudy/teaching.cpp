// 백준 1062번 가르침 : https://www.acmicpc.net/problem/1062

#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<vector>
using namespace std;

int alp[26], n, k, mCnt, chk[26];  // alp는 탐색에서 고른 알파벳, chk는 중복탐색을 방지하기위해 단어에 존재하는 모든 알파벳
char word[50][16];
vector<char> tmp;

void back(string sel, int id ,int cnt) {
	if (cnt == k || cnt == tmp.size()) {
		int sc = 0;
		for (int i = 0; i < n; i++) {
			int len = strlen(word[i]) - 4;
			int j = 4;
			for (j = 4; j < len; j++) {  // 인덱스 4부터 단어 길이 -4까지만 탐색하여 탐색 시간 최소화
				if (alp[word[i][j] - 97] == 0) break;
			}
			if (j == len) sc++;
		}
		if (sc > mCnt) mCnt = sc;
		return;
	}
	for (int i = id + 1; i < tmp.size(); i++) {
		alp[tmp[i] - 97] = 1;
		back(sel + tmp[i], i, cnt + 1);
		alp[tmp[i] - 97] = 0;
	}
}

int main() {
	scanf("%d %d", &n, &k);
	k -= 5;  // a, n, t, i, c는 반드시 선택할 수 밖에 없음
	chk['a' - 97] = alp['a' - 97] = 1;
	chk['n' - 97] = alp['n' - 97] = 1;
	chk['t' - 97] = alp['t' - 97] = 1;
	chk['i' - 97] = alp['i' - 97] = 1;
	chk['c' - 97] = alp['c' - 97] = 1;

	for (int i = 0; i < n; i++) {
		scanf(" %s", word[i]);
		// anta (0 ~3)  tica(n-4 ~ n-1)
		for (int j = 4; j < strlen(word[i]) - 4; j++) {
			if (chk[word[i][j] - 97] == 0) {
				tmp.push_back(word[i][j]);
				chk[word[i][j] - 97] = 1;
			}
		}
	}

	if (k < 0) {  // k가 5보다 작으면 가능한 경우의 수 없음
		printf("0");
		return 0;
	}

	back("", -1, 0);
	printf("%d", mCnt);
}

// 알고리즘 : 백트래킹
/*
풀이 : 미리 a, n, t, i, c를 선택해두고 4 ~ (단어길이 - 4)까지에 존재하는 알파벳을 모두 모아서 백트래킹으로 탐색한다.
1. 4 ~ (단어길이 - 4)까지에 존재하는 알파벳을 벡터에 중복없이 담는다.
2. 백트래킹 기법을 사용해 k - 5개의 알파벳을 고른다.
  2-1. 단, k-5개가 존재하는 알파벳 갯수보다 많을 수 있다. 이 경우, 존재하는 알파벳 갯수만큼만 고른다.
      반례 )  2 25
              antatica
              antaztica
3. 고른 알파벳으로 모든 단어를 순회하며 익힐 수 있는 단어의 갯수를 카운팅한다.
4. 카운팅한 갯수들 중 최대 값을 산출한다.
*/
