// 괄호의 값 : http://220.89.64.243/30stair/paren/paren.php?pname=paren

#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char arr[31];
int stack[31], int sum, top = -1, cnt, flag;

int main()
{
    scanf("%s", &arr);
    for (int i = 0; i <= strlen(arr); i++) {
        cnt = 0;
        if (top == -1 || stack[top] != ')' && stack[top] != ']') {  // #1
            stack[++top] = arr[i];
        }
        else if (stack[top] == ')') {  // #2
            if (stack[top - 1] == '(') {
                stack[--top] = 2;
            }
            else {
                for (int j = top - 1; stack[j] != '('; j--) {
                    cnt += stack[j];
                    top--;
                    if (top < 0) {
                        printf("0"); exit(0);
                    }
                }
                stack[--top] = cnt * 2;
            }
            stack[++top] = arr[i];
        }
        else if (stack[top] == ']') {  // #3
            if (stack[top - 1] == '[') {
                stack[--top] = 3;
            }
            else {
                for (int j = top - 1; stack[j] != '['; j--) {
                    cnt += stack[j];
                    top--;
                    if (top < 0) {
                        printf("0"); exit(0);
                    }
                }
                stack[--top] = cnt * 3;
            }
            stack[++top] = arr[i];
        }
    }
    for (int i = 0; i <= top; i++) {
        sum += stack[i];
        if (stack[i] == '(' || stack[i] == '[') {  // #4
            printf("0");
            exit(0);
        }
    }
    printf("%d", sum);
    return 0;
}

// #1 만약 스택이 비었거나 스택의 top이 ')'와 ']'가 아니면 스택에 값을 넣었다.
// #2 스택의 top이 ')'라면 '('가 나올때까지 스택에서 값을 빼서 cnt에 누적시켰다.
//    '('와 ')'가 붙어있는 경우라면 '('를 2로 바꿔주고 top을 낮춰주고,
//    붙어있는 경우가 아니라면 cnt에 누적된 값에 2를 곱해주었다.
//    만약에 스택을 다 비울때까지 '('가 나오지 않는다면 올바르지 못한 괄호열이므로 0을 출력시키고 프로그램을 종료시켰다.
// #3 '['와 ']'의 경우도 #2번과 동일하게 진행했다. 단, '['와 ']'가 붙어있는 경우엔 3, 그외의 경우엔 누적된 값이 3을 곱했다.
// #4 최종적으로 스택을 처음부터 끝까지 돌면서 sum에 스택에 존재하는 값들을 더해주고 마지막에 을 출력시켰다.
//    단, '('와 '['가 남아있는 경우는 올바르지 못한 괄호열이므로 0을 출력시키고 프로그램을 종료시켰다.
