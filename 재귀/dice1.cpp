// 주사위 던지기 1 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=449&sca=2080

#include <stdio.h>
int dice[5], n, m, flag;
void roll(int t, int d) {
    if (d == n) {  // #3
        for (int i = 0; i < d; i++) {
            printf("%d ", dice[i]);
        }
        printf("\n");
        return;
    }
    if (m == 1) {  // m이 1인 경우 : 주사위를 n번 던져서 나올 수 있는 모든 경우
        for (int i = 1; i <= 6; i++) {
            dice[d] = i;
            roll(i, d + 1);  // #2
        }
    }
    else if (m == 2) {  // m이 2인 경우 : 주사위를 n번 던져서 중복이 되는 경우를 제외하고 나올 수 있는 모든 경우
        for (int i = 1; i <= 6; i++) {
            if (d >= 1 && t > i) continue;
            dice[d] = i;
            roll(i, d + 1);  // #2
        }
    }
    else {  // m이 3인 경우 : 주사위를 n번 던져서 모두 다른 수가 나오는 모든 경우
        for (int i = 1; i <= 6; i++) {
            flag = 0;
            for (int j = 0; j < d; j++) {
                if (dice[j] == i) flag = 1;
            }
            if (flag == 1) continue;
            dice[d] = i;
            roll(i, d + 1);  // #2
        }
    }
}
int main() {
    scanf("%d%d", &n, &m);
    roll(0, 0); // #1
}

// 주사위를 던진 횟수(n)과 출력 형태(m)을 전역변수로 지정하고 함수 내에서 n, m에 따라 출력을 다르게 하게끔 조건문으로 구분지었다.
// #1 : n, m은 변하지 않는 수 이므로 재귀함수를 활용할 때, 인수 변화를 위해 함수에 입력되는 값은 n, m을 활용하지 않고 0, 0으로 설정했다.
// #2 : i는 주사위의 눈금이고, d는 주사위를 던진 횟수로 매 호출마다 1씩 증가한다.
//      각 호출마다 주사위의 눈금은 그대로 dice 배열에 차례대로 저장된다.
// #3 : 함수 내에서 주사위를 던진 횟수(d)가 처음 주어진 횟수(n)과 같아지면 dice 배열에 저장된 눈금들을 순서대로 출력하고 return한다.
//      각 조건문마다 주사위의 눈금을 1부터 시작하기 때문에 문제에서 제시했던 오름차순 출력을 위해 정렬하는 과정을 생략할 수 있다.
