// 비숍 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=935&sca=3030

#include <stdio.h>

int chess[11][11], ld[30], rd[30], wm = 0, bm = 0, n;

void black(int r, int c, int cnt) {  // #1
    if (cnt > bm) bm = cnt;
    if (c > n) {  // #2
        r++;
        if (r % 2 == 0) c = 2;
        else c = 1;
    }
    if (r > n) return;
    if (ld[r + c] == 0 && rd[r - c + 10] == 0 && chess[r][c] == 1) {
        ld[r + c] = 1;  // #3
        rd[r - c + 10] = 1;
        black(r, c + 2, cnt + 1);  // #2
        ld[r + c] = 0;
        rd[r - c + 10] = 0;
    }
    black(r, c + 2, cnt);
}

void White(int r, int c, int cnt) {
    if (cnt > wm) wm = cnt;
    if (c > n) {
        r++;
        if (r % 2 == 0) c = 1;
        else c = 2;
    }
    if (r > n) return;
    if (ld[r + c] == 0 && rd[r - c + 10] == 0 && chess[r][c] == 1) {
        ld[r + c] = 1;
        rd[r - c + 10] = 1;
        White(r, c + 2, cnt + 1);
        ld[r + c] = 0;
        rd[r - c + 10] = 0;
    }
    White(r, c + 2, cnt);
}

int main(void) {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            scanf("%d", &chess[i][j]);
        }
    }
    black(1, 1, 0);
    White(1, 2, 0);
    printf("%d", wm + bm);  // #4
    return 0;
}

// chess에 입력으로 주어지는 체스판 정보를 저장했고, ld와 rd에 각각 ↘방향 대각선과 ↙방향 대각선에 다른 비숍이 존재하는 지를 체크했다.
// #1 주어진 체스판 전체를 한 번에 탐색하려 했더니, 스택 오버플로우 또는 시간 제한을 초과하는 문제가 발생했다.
//    따라서 비숍은 체스판에서 같은 색의 칸에 존재하는 비숍에게만 영향을 끼칠 수 있다는 점을 활용하여 검정칸 위의 비숍과 흰칸 위의 비숍을 나누어서 탐색했다.
// #2 체스판에서 같은 색의 칸은 가로로 2칸, 세로로 2칸마다 존재한다.
//    이를 위해 매 탐색마다 가장 윗줄의 칸읜 맨왼쪽의 검정/흰 칸부터 시작하여 c(가로)를 2씩 증가시켰다.
//    만약 c가 체스판의 범위를 벗어나면 다음 줄(r)로 옮기는 방식을 사용했다.
// #3 해당 칸을 탐색해서 비숍을 놓았다면, ld와 rd에 해당 방향 대각선은 놓을 수 없음 표시했다.
//    ld(↘방향 대각선)는 같은 대각선위에 존재하는 모든 r,c 짝은 r-c가 같다는 규칙이 있다. 따라서 ld[r-c]를 1로 체크해주는 방법을 활용했다.
//    그러나 그냥 r-c로 사용하면, 음수가 나오는 경우를 배열을 통해 체크할 수 없다. 따라서 체스판의 최대 크기가 10이므로 10을 더해주어 양수값으로 활용했다.
//    rd(↙방향 대각선)는 같은 대각선위에 존재하는 모든 r,c 짝이 r+c가 같다는 규칙이 있다.
// #4 각각 black의 최대값은 bm에, white의 최대값은 wm에 저장했기 때문에 이를 더한 값이 곧 전체 체스판에 놓을 수 있는 비숍의 최대값이 된다.
