// 짝이 맞는 괄호 찾기 : http://220.89.64.243/30stair/match/match.php?pname=match

#include<stdio.h>

char arr[51];
int st[51], size, ck;

int main() {
    scanf("%s", &arr);
    for (int i = 0; arr[i] != 0; i++) {  // #1
        if (arr[i] == '(') {
            size++;
        }
        else if (arr[i] == ')') {
            size--;
        }
        if (size < 0) {
            break;
        }
    }
    if (size != 0) {
        printf("not match");
    }
    else {
        for (int i = 0; arr[i] != 0; i++) {  // #2
            if (arr[i] == '(') st[size++] = i;
            else if (arr[i] == ')') {
                printf("%d %d\n", st[--size], i);
            }
        }
    }
    return 0;
}

// #1 먼저 괄호의 짝이 맞는지를 검사하기 위해 arr에 입력값을 모두 받아서 처음부터 탐색했다.
//    '('가 나오면 size를 1 증가시키고, ')'가 나오면 size를 줄여서 만약 size가 음수가 되는 곳이 존재하거나 0보다 크다면
//    not match를 출력시키게 했다.
// #2 '('가 나오면 스택에 '('의 인덱스를 쌓고, ')'가 나오면 스택에서 하나를 빼서 ')'의 인덱스와 함께 출력했다.
