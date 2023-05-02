// 스도쿠 : 

#include <stdio.h>
#include <stdlib.h>
#include <vector>
using namespace std;

struct tmp {
    int x, y;
};

vector<tmp> point;
int board[9][9], cnt = 0;

bool square(int r, int t, int tmp) {  // #1 
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[r + i][t + j] == tmp) {
                return false;
            }
        }
    }
    return true;
}

bool check(int n, int tmp) {  // #2
    for (int i = 0; i < 9; i++) {
        if (board[point[n].x][i] == tmp) {
            return false;
        }
        if (board[i][point[n].y] == tmp) {
            return false;
        }
    }
    if (!square(point[n].x / 3 * 3, point[n].y / 3 * 3, tmp)) return false;
    return true;
}

void sudoku(int n) {
    if (n == cnt) {  // #3
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                printf("%d ", board[i][j]);
            }
            printf("\n");
        }
        exit(0);
    }
    for (int i = 1; i <= 9; i++) {  // #4
        if (check(n, i)) {
            board[point[n].x][point[n].y] = i;
            sudoku(n + 1);
        }
    }
    board[point[n].x][point[n].y] = 0;  // #5
    return;
}

int main() {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            scanf("%d", &board[i][j]);
            if (board[i][j] == 0) {  // #6
                point.push_back({ i, j });
                cnt++;
            }
        }
    }
    sudoku(0);
}

// #1 3 * 3칸 내에서 겹치는 숫자가 있는지 검사하는 함수를 따로 만들었다.
// #2 #1을 포함하여, 가로 및 세로 줄에 겹치는 숫자가 있는지 검사하여 겹치는 숫자가 있으면 false, 없으면 true를 return 시켰다.
// #3 만약 n(채운 숫자 개수)가 cnt(입력해야 하는 숫자 개수)와 같아지면, 모든 숫자를 문제없이 입력했다는 뜻이므로 스도쿠 판을 출력했다.
//    여러 경우가 존재할 경우, 하나만 출력하는 문제이기 때문에 exit(0)로 프로그램을 종료시켜 추가 탐색을 수행하지 않게 했다.
// #4 for문을 사용하여 1 ~ 9까지 숫자 중, #2의 조건을 통과한 숫자만 대입하였다.
// #5 만약 #4에서 #2의 조건을 통과한 숫자가 존재 하지 않는다면, 이전에 입력한 숫자가 잘못되었다는 뜻이다.
//    따라서 현재 탐색중인 좌표의 숫자를 0으로 초기화 해주고, return하여 이전 단계로 돌아가 추가 탐색을 수행하였다.
// #6 9 * 9칸을 모두 탐색해서 숫자가 있으면 넘기고, 숫자가 없으면 값을 탐색하는 과정을 수행하면 너무 많은 탐색이 수행된다고 생각했다.
//    따라서, 값을 입력할 때 0이 입력되면, 해당 0의 좌표를 point에 저장하고, 0의 갯수를 cnt에 카운팅 해주었다.
//    # cnt는 point.size()로 대체해도 무관하나 코드 작성의 편의를 위해 cnt를 사용했다.
