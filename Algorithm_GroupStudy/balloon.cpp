// 백준 11590번 풍선 맞추기 : https://www.acmicpc.net/problem/11509

#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;

struct tmp {
	int index, high;
};

int n, ball, arrow[1000002], cnt;

int main(){
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &ball);
		if (arrow[ball + 1] > 0) arrow[ball + 1]--;
		else cnt++;
		arrow[ball]++;
	}
	printf("%d", cnt);
}

// 알고리즘 : 탐욕법(그리디 알고리즘)
/*
풀이 : 화살의 높이를 인덱스로 활용하여 풍선을 터트릴때마다 인덱스를 이동시켰다.
풍선 높이를 받으면 풍선 높이 + 1 위치에 화살이 있었는지 확인한다.
화살이 있으면 해당 화살이 풍선을 터트리고 높이가 -1 된 상태로 현재 풍선을 터트릴 것이므로 그 화살의 인덱스를 -1해서 옮겨준다.
화살이 없으면 새로운 화살을 쏘아야 하므로 현재 풍선의 높이에 화살을 1개 추가하고, 카운팅한다.
*/
