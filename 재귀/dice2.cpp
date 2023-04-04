// 주사위 던지기 2 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=458&sca=2080

#include <stdio.h>
int dice[8], n, m;
void roll(int d, int s) {
    if (s < 0 || (d == n && s > 0)) return; // #2
    if (d == n) {  // #3
        for (int i = 0; i < n; i++) {
            printf("%d ", dice[i]);
        }
        printf("\n");
    }
    for (int i = 1; i <= 6; i++) {
        dice[d] = i;
        roll(d + 1, s - i);
    }
}
int main() {
    scanf("%d%d", &n, &m);
    roll(0, m);  // #1
}

// #1 : 함수의 인수에 초기값으로 0과 눈의 합(m)을 주고, 함수 내에서 나온 주사위의 눈금을 m(함수에서 s)에서 빼주는 방식으로 재귀함수를 돌렸다.
//      이 때, 주사위를 던진 횟수 n은 변하지 않는 수이므로 인수로 주지않고 전역변수로 두어 활용했다.
// #2 : "횟수를 모두 소진했을때 남은 눈금(s)이 1 이상" 이거나 "횟수와 관계없이 남은 눈금이 0보다 작아지면" 현재 경우의 수를 탈출한다.
// #3 : 앞서 풀어봤던 '주사위 던지기 1' 문제와 마찬가지로 dice 배열에 주사위 눈금을 저장해두고, 모든 횟수를 던졌다면 차례대로 출력한다. 
