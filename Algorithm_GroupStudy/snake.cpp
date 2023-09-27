// 백준 3190번 뱀 : https://www.acmicpc.net/problem/3190

#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;

struct loc { int x, y; };

int n, k, l, map[101][101], t = 1, sec;
loc head, tail, vt[4] = { {-1, 0}, { 0, 1 }, {1, 0}, {0, -1} };
char d[10001];

int main() {
	scanf("%d %d", &n, &k);
	for (int i = 0; i < k; i++) {
		int a, b;
		scanf("%d%d", &a, &b);
		map[a][b] = 9;
	}
	head = { 1, 1 }, tail = { 1, 1 };
	map[1][1] = 2;
	scanf("%d", &l);
	for (int i = 0; i < l; i++) {
		int a;
		scanf("%d", &a);
		scanf(" %c", &d[a]);	
	}
	while (1) {
		sec++;  // 초시계
		head.x += vt[t].x;
		head.y += vt[t].y;
		if (map[head.x][head.y] != 0 && map[head.x][head.y] != 9 || head.x == 0 || head.x == n + 1 || head.y == 0 || head.y == n + 1) {
			printf("%d", sec);  // 뱀이 벽에 부딪히거나, 자신의 몸에 닿으면 종료
			return 0;
		}
		else {
			if (map[head.x][head.y] != 9) {
				int t2 = map[tail.x][tail.y] - 1;
				map[tail.x][tail.y] = 0;
				tail.x += vt[t2].x;
				tail.y += vt[t2].y;
			}
			if (d[sec] == 'L') t = (t + 3) % 4;
			else if (d[sec] == 'D') t = (t + 1) % 4;
			map[head.x][head.y] = t + 1;
		}
	}
	printf("%d", sec);
}

// 알고리즘 : 시뮬레이션
/*
풀이 : 맵을 순회하면서 꼬리쪽은 계속 0으로, 머리쪽은 계속 다음 방향 정보로 만드는 방식으로 진행한다.
꼬리는 머리가 움직인 경로 그대로 따라 와야하므로 각 칸에 다음 칸의 방향을 저장한다.
꼬리는 해당 칸으로 좌표를 움직이며 배열을 초기화 시킨다.
만약 머리가 도착한 칸이 다음과 같으면 프로그램을 종료한다.
1. 머리가 도착한 칸이 아직 꼬리가 도착하지않아 초기화되지 않았을 경우
2. 머리가 도착한 칸이 맵 밖인 경우

풀이를 쓰다보니 deque 자료구조를 활용하여 머리가 지나간 방향을 저장하는 방법이 더 간단할 것 같다는 생각이 들었다.
1. deque에 머리가 지나간 좌표를 push_back하고 map에 체크
2. 사과를 못먹었으면 deque에서 map의 front좌표 초기화 후 pop_front();
