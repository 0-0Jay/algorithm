// 저울 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1760&sca=3050

#include<stdio.h>
#include<algorithm>
using namespace std;

int arr[1001];

int main() {
	int n, tmp = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	sort(arr, arr + n);  // #1
	for (int i = 0; i <= n; i++) {
		if (arr[0] != 1) {  // #2
			printf("%d", tmp + 1);
			break;
		}
		tmp += arr[i];
		if (arr[i + 1] > tmp + 1 || i == n) {  // #3
			printf("%d", tmp + 1);
			break;
		}
	}
}

// #1 만들 수 없는 최소값을 구해야 하므로 다음 과정을 위해 입력받은 수들을 오름차순으로 정렬했다.
// #2 만약 오름차순으로 정렬했을 때, 가장 작은수가 1이 아니라면 1을 만들 수 없기 때문에 1을 출력했다.
// #3 tmp에 arr[i]를 누적시키고, 다음 수인 arr[i + 1]이 tmp + 1(tmp의 다음 수)보다 크면 tmp + 1은 만들지 못하는 수이므로 이를 출력시켰다.
//    만약 i가 n이라면 모든 탐색이 이루어질동안 불가능한 숫자가 없었다는 뜻이므로 tmp + 1을 출력시킨다.
