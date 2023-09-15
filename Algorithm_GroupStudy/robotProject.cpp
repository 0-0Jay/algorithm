// 백준 3649번 로봇 프로젝트 : https://www.acmicpc.net/problem/3649

#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;

int x, n, lego[1000000];

int main(){
	while (cin >> x >> n) {  // 여러 개의 테스트 케이스가 들어오지만, 정확한 갯수를 밝히지 않았기 때문에 조건문에 입력문을 삽입
		for (int j = 0; j < n; j++) {
			scanf("%d", &lego[j]);
		}
		sort(lego, lego + n);
		int l = 0, r = n - 1, flag = 0;
		x *= 10000000;  // 받은 목표값은 10000000를 곱해서 단위 통일
		while (l < r) {
			if (lego[l] + lego[r] > x) r--;
			else if (lego[l] + lego[r] < x) l++;
			else {
				flag = 1;
				break;
			}
		}
		if (flag) printf("yes %d %d\n", lego[l], lego[r]);
		else printf("danger\n");
	}
}

// 알고리즘 : 투 포인터
/*
풀이 : 모든 블럭 크기를 입력받아 오름차순으로 정렬 후, 가장 좌측과 우측부터 시작해서 두 인덱스의 값의 합을 조정한다.
두 수의 합이 작으면 l을 높여서 크기를 키우고, 합이 크면 r을 낮춰서 크기를 줄인다.
*/
