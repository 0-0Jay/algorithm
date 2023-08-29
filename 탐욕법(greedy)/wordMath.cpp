// 백준 1339번 단어 수학 : https://www.acmicpc.net/problem/1339

#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;

int alp[26], len[10], res;
char word[10][9];

int chk(int i, int j) {  // 높은 자리일 수록 높은 숫자를 받는 것이 유리하므로 내림차순 정렬해서 활용
	return i > j;
}

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", word[i]);
		len[i] = strlen(word[i]);  // 각 단어의 길이를 저장
	}
	for (int i = 0; i < n; i++) {
		int tmp = 1;
		for (int j = len[i] - 1; j >= 0; j--) {  // 위에서 저장한 길이를 활용해 word의 각 알파벳에 자릿수 기록
			alp[word[i][j] - 'A'] += tmp;
			tmp *= 10;
		}
	}
	sort(alp, alp + 26, chk);  // 정렬
	for (int i = 0; i < 10; i++) {
		res += alp[i] * (9 - i);  // alp에 저장된 자릿수에 차례대로 9 ~ 0을 곱하여 바로바로 res에 누적
	}
	printf("%d", res);
	return 0;
}
