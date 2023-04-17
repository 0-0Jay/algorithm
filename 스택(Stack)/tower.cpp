// 탑 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=607&sca=3020

#include <stdio.h>
# define M 500001

int stack[M][2], arr[M], res[M];

int main() {
	int n, top = -1, id = -1;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &arr[i]);
	}
	for (int i = n; i > 0; i--) {  // #1
		if (top == -1 or arr[i] < stack[top][0]) {
			stack[++top][0] = arr[i];
			stack[top][1] = i;  // #2
		}
		else {
			while (arr[i] >= stack[top][0] && top > -1) {
				res[stack[top--][1]] = i;

			}
			stack[++top][0] = arr[i];
			stack[top][1] = i;
		}
	}
	for (int i = 1; i <= n; i++) {
		printf("%d ", res[i]);
	}
}

// #1 탑의 왼쪽방향으로 신호를 전달하기 때문에 값 전체를 배열에 선 입력받고 이를 역순으로 탐색했다.
// #2 여기서 부터는 이전에 풀었던 빌딩 문제와 동일하다.
//    스택이 비어있거나 현재 탑의 크기가 이전 탑의 크기보다 작으면 스택에 값을 넣고, 아니면 작아질 때까지 스택에서 값을 뺐다.
//    값을 빼면서 res에 수신한 탑의 인덱스를 저장했다.
