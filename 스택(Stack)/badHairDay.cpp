// 불쾌한 날 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=421&sca=3020

#include <stdio.h>

int stack[80001], st = -1;

int main() {
	int n, now;
	long long cnt = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &now);
		if (st == -1 || stack[st] > now) {
			stack[++st] = now;  // #1
		}
		else {
			for (st; st >= 0 && stack[st] <= now; st--) {
				cnt += st;  // #2
			}
			stack[++st] = now; // #3
		}
	}
	cnt += st * (st + 1) / 2; // #4
	printf("%lld", cnt);
}

// #1 스택에 값이 없거나 입력받은 값(now)이 스택의 top(st)보다 작으면 값을 스택에 넣었다.
// #2 스택에 값이 있고, now가 스택의 top보다 크거나 같으면 스택의 키(st)를 이용해서 볼 수 있는 소의 카운트를 올려주면서
//    키 값을 낮춰주었다.(스택에서 자료를 굳이 뺄 필요 없다. 키값만 낮춰주면 해당 자리에 새로 데이터를 수정해줄 수 있다.)
// #3 이전 소의 키가 현재 소보다 커지면 키 값을 낮추는 과정을 멈추고 now를 스택에 넣었다.
// #4 for문이 끝났을때 스택에 값이 남아있다면, 반드시 내림차순으로 값이 존재하게 된다.
//    따라서 1부터 st까지를 더한 값을 cnt에 누적시켜주어 남아있는 소들에 대한 계산도 반영해주었다.
