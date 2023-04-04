// 하노이1 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=441&sca=2080

#include <stdio.h>
void hanoi(int t, int s, int e) {
    if (t == 0) return;
    hanoi(t - 1, s, 6 - s - e);  // #1
    printf("%d : %d -> %d\n", t, s, e);
    hanoi(t - 1, 6 - s - e, e);  // #2
}
int main() {
    int n;
    scanf("%d", &n);
    hanoi(n, 1, 3);
}

// #1 : 가장 아래 원판을 A라고 한다면, A가 3번 기둥에 이동하기 위해서 나머지 원판들이 2번 기둥으로 이동해야 한다.
// #2 : 예를들어 A가 3번 기둥에 이동했다면 다시 2번 기둥의 가장 아래 원판이 3번 기둥으로 가기위해 나머지 원판들이 1번 기둥으로 이동해야 한다.
