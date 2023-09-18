// 백준 1107번 리모컨 : https://www.acmicpc.net/problem/1107

#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;

struct tmp {
	int ch, f, cnt;
};

int x = 100, n, m, button[10], chk[1000001][2];  // 0번 인덱스에는 숫자만, 1번 인덱스에는 +, -버튼으로 이동한 경우 체크
queue<tmp> que;

int main() {
	scanf("%d%d", &n, &m);
	for (int i = 0; i < m; i++) {
		int b;
		scanf("%d", &b);
		button[b] = 1;
	}
	que.push({ 100, 0 });
	chk[100][1] = 1;
	while (!que.empty()) {
		tmp now = que.front();
		que.pop();
		if (now.ch == n) {
			printf("%d", now.cnt);
			return 0;
		}
		if (now.f == 0) {  // 아무 버튼도 안누른 경우
			for (int i = 0; i < 10; i++) {
				if (button[i] == 0) {  // 숫자 버튼
					que.push({ i, 1, now.cnt + 1 });
					chk[i][0] = 1;
				}
			}
			if (now.ch < 500000 && chk[now.ch + 1][1] == 0) {  // + 버튼
				que.push({ now.ch + 1, 2, now.cnt + 1 });
				chk[now.ch + 1][1] = 1;
			}
			if (now.ch > 0 && chk[now.ch - 1][1] == 0) {  // - 버튼
				que.push({ now.ch - 1, 2, now.cnt + 1 });
				chk[now.ch - 1][1] = 1;
			}
		}
		else if (now.f == 1) {  // 이전에 숫자 버튼을 누른 경우
			for (int i = 0; i < 10; i++) {  // 숫자 버튼
				int t = now.ch * 10 + i;
				if (t <= 1000000 && button[i] == 0 && chk[t][0] == 0) {
					que.push({ t, 1, now.cnt + 1 });
					chk[t][0] = 1;
				}
			}
			if (now.ch < 500000 && chk[now.ch + 1][1] == 0) {  // + 버튼
				que.push({ now.ch + 1, 2, now.cnt + 1 });
				chk[now.ch + 1][1] = 1;
			}
			if (now.ch > 0 && chk[now.ch - 1][1] == 0) {  // - 버튼
				que.push({ now.ch - 1, 2, now.cnt + 1 });
				chk[now.ch - 1][1] = 1;
			}
		}
		else if (now.f == 2) {  // 이전에 +, -를 누른 경우
			if (now.ch < 500000 && chk[now.ch + 1][1] == 0) {  // + 버튼
				que.push({ now.ch + 1, 2, now.cnt + 1 });
				chk[now.ch + 1][1] = 1;
			}
			if (now.ch > 0 && chk[now.ch - 1][1] == 0) {  // - 버튼
				que.push({ now.ch - 1, 2, now.cnt + 1 });
				chk[now.ch - 1][1] = 1;
			}
		}
	}
}

// 알고리즘 : BFS(너비 우선 탐색)
/*
풀이 : 0~9, +, - 버튼을 누르는 경우를 모두 너비로 두고 탐색한다.
리모컨의 특성상 한번이라도 +나 - 버튼을 눌렀다면, 이후에 숫자버튼을 누를시 채널이 한자리 숫자로 다시 입력된다.
따라서 맨처음 경우, 숫자버튼을 누르는 경우, +나-를 누르는 경우에 조건식을 섬세하게 작성해야한다.

또한, 요구하는 숫자의 한계는 500000이지만, 문제에서 채널은 무한히 있다고 제시했다.
이는 500000이 목표 채널이고,  5를 제외한 모든 숫자 버튼이 고장났을 때,
5555에서 50000까지 +버튼을 누르는 방법만 있는게 아니라 55555에서 50000까지 -버튼을 누르는 방법도 가능하다는 의미다.
따라서 계산과정에서 나타날 수 있는 숫자의 한계를 1000000으로 설정하여 999999채널까지는 계산과정에서 이동할 수 있어야 한다.
(위 코드에서는 계산과정에서 한계를 주지 않고, chk에대한 조건을 0~1000000으로 주었다.)

리모컨의 특성상 반드시 +나 -버튼을 누르면 이후에 숫자버튼을 누르지 않는다.
이를 이용해서 +나 -버튼을 누르면 반드시 목적지까지 +나 - 버튼만 누르게 하여 계산을 하는 방법도 고려했다.
(+1 혹은 -1씩 매번 반복하는 것이 아닌, 현재 채널값 - 목표 채널값만큼 한번에 카운팅 하는 방법)
그러나 이렇게 작성할 경우 +나 -버튼을 눌렀을 때의 최소 횟수를 구해야 하므로 결국 큐를 전부 탐색해야하여 시간초과 혹은 메모리초과가 발생했다.
*/
