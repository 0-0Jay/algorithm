// 빌딩 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=607&sca=3020

#include <stdio.h>
#include <stack>
using namespace std;

int stk[100100][2], ans[100000], top = 0;

int main() {
    int n, t, top = 0;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &t);
        if (top == 0 || stk[top][0] >= t) {  // #1
            stk[++top][0] = t;
            stk[top][1] = i;
        }
        else {
            for (top; top > 0 && stk[top][0] < t; top--) {
                ans[stk[top][1]] = i;  // #2
            }
            stk[++top][0] = t;
            stk[top][1] = i;  // #3
        }
    }
    for (int i = 1; i <= n; i++) {
        printf("%d\n", ans[i]);  // #4
    }
}

// #1 스택에 값이 없거나 스택의 top에 있는 빌딩의 높이가 현재 입력받은 값(t)보다 크거나 같으면 스택에 t를 넣었다.
// #2 만약 스택에 값이 있고, 스택의 top이 t보다 작으면 ans에 현재 빌딩(t)의 순번(i)을 ans의 top 인덱스에 넣었다.
//    스택에 값이 쌓인다는 뜻은 이전 빌딩에서 현재 빌딩이 보이지 않는다는 뜻이며,
//    만약 top에 있는 빌딩에서 t가 보이면 ans의 top 인덱스에 현재 빌딩의 순번을 적어주는 방식이다.
// #3 t가 보이지 않는 빌딩이 top이 될때까지 반복한 후, t를 스택에 넣는다.
// #4 이전에 풀었던 불쾌한 날 문제와는 달리 이 문제에서는 스택에 값이 남아있다는 것은 보이는 빌딩이 없다는 뜻이다.
//    따라서 추가적인 과정 없이 ans를 출력시켰다.

