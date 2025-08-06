// 백준 17143번 낚시왕 : https://www.acmicpc.net/problem/17143

#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<queue>
#include<memory.h>  // 백준 제출시 memset함수 호출을 위해 작성해줘야함
using namespace std;

int r, c, m, total, human;

struct tmp {
	int r, c, speed, vt, size;  // vt : 1이면 위, 2면 아래, 3은 오른쪽, 4는 왼쪽

};

queue<tmp> shark;
struct arrchk { int sp, vt, sz; }mov[101][101];

int main() {
	scanf("%d%d%d", &r, &c, &m);
	for (int i = 0; i < m; i++) {
		int x, y, s, d, z;
		scanf("%d%d%d%d%d", &x, &y, &s, &d, &z);
		mov[x][y] = { s, d, z };
	}
	if (m == 0) {  // 상어가 없으면 0 출력 후, 프로그램 종료
		printf("0");
		return 0;
	}
	for (human = 1; human <= c; human++) {
		// 사람이 있는 줄에 상어가 있는지 확인 해서 있으면 젤 위의 것의 크기 추가
		for (int i = 1; i <= r; i++) {
			if (mov[i][human].sz != 0) {
				total += mov[i][human].sz;
				mov[i][human] = { 0, 0, 0 };
				break;
			}
		}
		// 잡은 상어를 제외하고 다시 큐에 삽입
		for (int a = 1; a <= r; a++) {
			for (int b = 1; b <= c; b++) {
				if (mov[a][b].sz != 0) {
					shark.push({ a, b, mov[a][b].sp, mov[a][b].vt, mov[a][b].sz });
				}
			}
		}
		memset(mov, 0, sizeof(mov));  // 다음 탐색을 위해 mov 초기화

		while(!shark.empty()){
			tmp now = shark.front();
			shark.pop();
			if (now.vt == 1) {  // 위를 보고있는 상어일 경우 (r만 컨트롤)
				int remain = now.speed;
				if (remain > now.r - 1) {
					remain -= (now.r - 1);
					int mok = remain / (r - 1);
					int nam = remain % (r - 1);
					if (mok % 2 == 0) {
						now.r = 1;
						now.vt = 2;
					}
					else {
						now.r = r;
						now.vt = 1;
					}
					if (now.r == 1) now.r += nam;
					else now.r -= nam;
				}
				else {
					now.r -= remain;
				}
			}
			else if (now.vt == 2) {  // 아래를 보고있는 상어일 경우 (r만 컨트롤)
				int remain = now.speed;
				if (remain > r - now.r) {
					remain -= (r - now.r);
					int mok = remain / (r - 1);
					int nam = remain % (r - 1);
					if (mok % 2 == 0) {
						now.r = r;
						now.vt = 1;
					}
					else {
						now.r = 1;
						now.vt = 2;
					}
					if (now.r == 1) now.r += nam;
					else now.r -= nam;
				}
				else {
					now.r += remain;
				}
			}
			else if (now.vt == 3) {  // 오른쪽 보고있는 상어일 경우 (c만 컨트롤)
				int remain = now.speed;
				if (remain > c - now.c) {
					remain -= (c - now.c);
					int mok = remain / (c - 1);
					int nam = remain % (c - 1);
					if (mok % 2 == 0) {
						now.c = c;
						now.vt = 4;
					}
					else {
						now.c = 1;
						now.vt = 3;
					}
					if (now.c == 1) now.c += nam;
					else now.c -= nam;
				}
				else {
					now.c += remain;
				}
			}
			else if (now.vt == 4) {  // 왼쪽 보고있는 상어일 경우 (c만 컨트롤)
				int remain = now.speed;
				if (remain > now.c - 1) {
					remain -= (now.c - 1);
					int mok = remain / (c - 1);
					int nam = remain % (c - 1);
					if (mok % 2 == 0) {
						now.c = 1;
						now.vt = 3;
					}
					else {
						now.c = c;
						now.vt = 4;
					}
					if (now.c == 1) now.c += nam;
					else now.c -= nam;
				}
				else {
					now.c -= remain;
				}
			}
			if (mov[now.r][now.c].sz < now.size) mov[now.r][now.c] = { now.speed, now.vt, now.size };  // 겹치면 크기가 큰 상어를 저장
		}

	}
	printf("%d", total);
}

// 알고리즘 : 구현, 시뮬레이션
/*
풀이 : 매 회차 문제에서 제시된 순서에 맞게 상어 이동과 삭제 수행
1. for문을 응용해서 사람이 있는 줄의 1번 인덱스 부터 탐색해 가장 먼저 만나는 상어의 크기를 합산하고 낚시를 중단한다.
  1-1. 만약 상어를 발견하면 해당 상어의 정보를 0으로 초기화 한다. 
  1-2. 상어를 발견하지 못했다면 map 그대로 다음 절차로 넘긴다
2. map을 전부 탐색해서 상어의 정보를 전부 큐에 넣는다.
3. 큐에서 상어를 하나씩 꺼내서 상어의 정보에 맞게 이동을 수행한다.
  3-1. 만약 이동한 곳에 상어가 이미 있다면 두 상어의 크기를 비교해서 크기가 큰 상어의 정보로 교체한다.
4. 이동이 끝난 상어를 다시 map으로 변환한다.
5. 1 ~ 4를 human이 c과 같아질 때까지 반복한 후, 합산된 total을 출력한다.
*/
