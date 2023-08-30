// 백준 12933번 오리 : https://www.acmicpc.net/problem/12933

#include<stdio.h>
#include<iostream>
#include<algorithm>
#include <string>
using namespace std;

int quack[120], cnt, maxCnt = 0;

int main() {
	string s;
	cin >> s;
	for (char i : s) {
		quack[i]++;
		if (quack['q'] < quack['u'] || quack['u'] < quack['a'] || quack['a'] < quack['c'] || quack['c'] < quack['k']) {
			printf("-1");  // 한번이라도 q >= u >= a >= c >= k 를 만족하지 않으면 불가능한 경우
			return 0;
		}
		if (i == 'q') {  // q가 나올때마다 오리를 추가
			cnt++;
			if (maxCnt < cnt) maxCnt = cnt;  // 만약 추가한 오리가 현재 최대 수보다 크다면 갱신
		}
		if (i == 'k') cnt--;  // k가 나올때마다 다음 울음소리는 방금 오리가 또 낼 수 있으므로 오리를 차감해서 카운트 유지
	}
	if (quack['q'] > quack['u'] || quack['u'] > quack['a'] || quack['a'] > quack['c'] || quack['c'] > quack['k']) {
		printf("-1");  // 모든 울음소리가 종료되었을 때 q, u, a, c, k의 수가 다르면 불가능한 경우
		return 0;
	}
	printf("%d", maxCnt);  // 최종 maxCnt를 출력
	return 0;
}
