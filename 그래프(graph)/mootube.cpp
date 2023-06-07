// MooTube(Silver) : https://www.acmicpc.net/problem/15591

#include<stdio.h>
#include<vector>
using namespace std;

struct tmp {
	int mov, usa;
};

vector<tmp> usado[5001];
int n, m, chk[5001], que[30000000], st, ed;

int main() {
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n - 1; i++) {
		int p, q, r;
		scanf("%d%d%d", &p, &q, &r);
		usado[p].push_back({ q,r });  // #1
		usado[q].push_back({ p,r });
	}
	for (int i = 0; i < m; i++) {
		int usa, a, cnt = 0;  // #2
		scanf("%d%d", &usa, &a);
		st = -1, ed = -1;
		que[++st] = a;
		while (st != ed) {
			int now = que[++ed];
			chk[now] = 1;  // #3
			for (int j = 0; j < usado[now].size(); j++) {  // #4
				if (chk[usado[now][j].mov] == 1) continue;
				if (usado[now][j].usa >= usa) {
					cnt++;
					que[++st] = usado[now][j].mov;
				}
			}
		}
		for (int i = 0; i < 5001; i++) {  // #5
			chk[i] = 0;
		}
		printf("%d\n", cnt);
	}
}

// #1 p, q, r(유사도)을 입력받아서 usado벡터에 p인덱스에 q, q인덱스에 p를 r과 함께 저장해서 p와 q가 서로 탐색할 수 있게 했다.
// #2 각 질문들 마다 질문에서 주어지는 유사도(usa)를 기준으로 , a(시작 동영상)과 연결된 모든 동영상을 BFS로 탐색했다.
//    매 질문당 추천동영상의 갯수를 묻는 문제이므로 cnt를 0으로 초기화시켰다.
// #3 chk배열에 현재 동영상이 탐색되었음을 체크해서 중복탐색을 방지했다.
// #4 각 동영상과 연결되어 있는 모든 동영상중에서 유사도 조건에 만족하는 동영상은 q에 넣고 cnt를 +1 했다.
// #5 매 탐색마다 chk 배열을 초기화해서 현재 질문에 대한 탐색이 다음 질문에 영향을 주지 않도록 했다.
