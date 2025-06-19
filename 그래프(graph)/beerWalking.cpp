// 백준 9205번 맥주 마시면서 걸어가기 : https://www.acmicpc.net/problem/9205

#include<stdio.h>
#include<algorithm>
#include<queue>
using namespace std;

struct tmp {
	int x, y, chk;
};

int t, n;
tmp conv[101];

int main() {
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		int homeX, homeY, finX, finY;
		scanf("%d%d%d", &n, &homeX, &homeY);
		for (int j = 0; j < n; j++) {
			scanf("%d%d", &conv[j].x, &conv[j].y);
			conv[j].chk = 0;  // 만약 t가 2이상일 경우 이전 탐색의 chk가 남아있으면 안되므로 초기화
		}
		scanf("%d%d", &finX, &finY);
		conv[n] = { finX, finY, 0 };  // 편의점 배열에 목적지도 삽입해서 한번에 BFS 탐색
		queue<tmp> que;
		que.push({ homeX, homeY });  // 큐에 시작점 초기값으로 저장
		int flag = 0;
		while (!que.empty()) {
			tmp now = que.front();
			que.pop();
			if (now.x == finX && now.y == finY) {  // 만약 목적지에 도달하면 flag를 1로 변경하고 불필요한 추가탐색 break로 방지
				flag = 1;
				break;
			}
			for (int i = 0; i <= n; i++) {  // 편의점 배열을 탐색하면서 거리가 1000이하면 큐에 삽입 후, 중복 탐색 방지 체크
				if (conv[i].chk == 0 && abs(conv[i].x - now.x) + abs(conv[i].y - now.y) <= 1000) {
					que.push({conv[i].x, conv[i].y});
					conv[i].chk = 1;
				}
			}
		}
		if (flag == 1) printf("happy\n");  // flag에 따라 출력
		else printf("sad\n");
	}
}

// 알고리즘 : BFS(너비 우선 탐색)
/*
풀이 : 매 경우마다 큐, 배열, 체크를 초기화하고, BFS로 도착 여부 탐색
좌표의 범위가 -32768 ≤ x, y ≤ 32767 인데, 이를 직접 2차원 배열로 탐색하려하면 배열크기 한계에 막힌다.
따라서 이 문제는 큐에 한칸씩 이동하는 것이 아니라, 각각의 편의점을 노드로 보고 BFS를 탐색해야한다.
각 편의점의 위치 및 목적지를 하나의 배열에 넣고 매 탐색마다 배열전체를 확인하여 조건에 맞으면 다음 목적지로 큐에 저장한다.
큐에서 좌표를 뽑았을때 최종 목적지면 happy, 큐가 빌 때까지 탐색해도 찾지 못했다면 sad를 출력한다.
*/
