// 인덱스 찾기 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2857&sca=3010

#include <stdio.h>
int arr[500000];

int main() {
    int n, m, t, l, r, mid;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    scanf("%d", &m);
    for (int i = 0; i < m; i++) {
        scanf("%d", &t);
        l = 0, r = n;  // #1
        while (1) {
            if (l > r) {  // #3
                printf("-1 ");
                break;
            }
            mid = (l + r) / 2;
            if (arr[mid] == t) {
                printf("%d ", mid);
                break;
            }
            else if (arr[mid] < t) l = mid + 1;  // #2
            else r = mid - 1;
        }
    }
}

// arr은 입력된 숫자들을 저장하는 배열
// #1 인덱스를 구하는게 문제의 조건이기 때문에 배열의 값이 아닌 인덱스를 기준으로 left를 0, right를 n으로 두었다.
//    배열에 들어오는 값은 문제에서 오름차순으로 주어지기 때문에 이 방식을 사용했다.
// #2 이진 탐색을 수행하면서 arr[mid]가 주어진 수보다 크면 left를 올리고, 작으면 right를 내려서 탐색했다.
// #3 만약 left가 right 보다 커지면, 끝까지 탐색했음에도 값을 찾지 못했다는 의미이므로 -1을 출력한다.
