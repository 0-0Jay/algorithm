// 백준 12904번 A와 B : https://www.acmicpc.net/problem/12904

#include <stdio.h>
#include <algorithm>
#include <iostream>
using namespace std;

string s, t;

void back(string n) {
	if (n.length() == s.length()) {
		if (n.compare(s) == 0) printf("1");
		else printf("0");
		exit(0);
	}
	if (n[n.length() - 1] == 'A') back(n.erase(n.length() - 1, 1));
	if (n[n.length() - 1] == 'B') {
		n.erase(n.length() - 1, 1);
		reverse(n.begin(), n.end());
		back(n);
	}
}

int main() {
	cin >> s >> t;
	back(t);
}

// 알고리즘 : 그리디(탐욕법)
/*
풀이 : s로 부터 시작해서 t로 가는 것이 아닌, t에서 s로 역방향으로 수행한다.

각각 두가지 조건을 반대로 수행한다.
1. 끝에 A를 추가한다. -> 끝에 A가 있으면 A를 제거한다.
2. 문자열을 뒤집고 B를 추가한다. -> 끝에 B가 있으면 B를 제거하고 문자열을 뒤집는다.

s로 부터 시작하면  매 탐색에서 (A를 추가하는 경우)와 (뒤집고 B를 추가하는 경우)를 시간복잡도 O(2^n)으로 완전탐색해야 한다.
그러나 t에서 시작하여 맨 우측의 알파벳이 A인가 B인가만 판단하면 시간복잡도 O(n)만에 탐색할 수 있다.
*/
