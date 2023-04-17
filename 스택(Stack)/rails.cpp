// 레일 : http://220.89.64.243/30stair/rails/rails.php?pname=rails

#include<stdio.h>
#include<stdlib.h>

int stack[1000], train[1000], size, id, tr;

int main()
{
    int n;
    scanf("%d", &n);
    while (1) {
        for (int i = 0; i < n; i++) {
            scanf("%d", &train[i]);
            if (train[i] == 0) exit(0);  // #1
        }
        tr = 1, size = 0, id = 0;
        while (1) {
            if (size == 0 || stack[size - 1] != train[id]) { // #2
                stack[size++] = tr++;
            }
            else {
                id++;
                size--;
            }
            if (id == n || tr > n + 1) break;  // #3
        }
        if (id == n) {  // #4
            printf("Yes\n");
        }
        else {
            printf("No\n");
        }
    }
    return 0;
}

// #1 매 회마다 기차 번호를 입력받아서 train에 저장했다. 만약 train에 0이 들어오면 프로그램을 종료시켰다.
// #2 만약 스택이 비었거나 이번에 빠져나와야하는 기차번호와 스택의 top이 다르면 스택에 새 기차를 넣었다. 
//    만약 같으면 train의 id를 1 올려서 다음 기차를 가르키고, 스택에서 기차를 빼내었다.
// #3 만약에 기차를 끝까지 탐색했거나 새 기차의 번호가 마지막 기차번호보다 크면, 반복을 중단시켰다.
//    새 기차의 번호가 마지막 기차보다 크다는 것은 불가능한 정렬이라는 뜻이기 때문이다.
// #4 id가 n과 같다면 가능한 조합이니 Yes를, 아니라면 불가능한 정렬이 되어 빠져나왔다는 뜻이므로 No를 출력했다.
