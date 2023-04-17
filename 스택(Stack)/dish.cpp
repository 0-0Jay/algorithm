// 접시 꺼내기 : http://220.89.64.243/30stair/dish/dish.php?pname=dish

#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char stk[31], arr[31], ans[61], id = 'a';
int size = 0, k = 0, t = 0;

int main()
{
    scanf("%s", &arr);
    while (1) {
        if (size == 0 || stk[size - 1] != arr[k]) {  // #1
            stk[size++] = id++;
            ans[t++] = '1';  // #2
        }
        else {
            size--;
            k++;
            ans[t++] = '0';
        }
        if (k == strlen(arr) || id > 'a' + strlen(arr)) {
            break;  // #3
        }
    }
    if (k == strlen(arr)) {  // #4
        for (int i = 0; ans[i] != 0; i++) {
            if (ans[i] == '1') {
                printf("push\n");
            }
            else {
                printf("pop\n");
            }
        }
    }
    else {
        printf("impossible");
    }
    return 0;
}

// #1 스택에 값이 없거나 스택의 top(t)이 현재 꺼내야할 접시와 다르면 스택에 접시를 넣었다.
//    id에 초기값으로 'a'를 주고 char형으로 활용해서 1씩 더해주는 방식으로 스택에 넣는다.
// #2 스택에 값이 들어가면 ans에 들어갔다는 의미로 1을, 값이 빠지면 빠졌다는 의미로 0을 저장하고 k를 1 올렸다.
// #3 만약 k가 arr의 길이와 같아지거나 id가 arr에 있는 알파벳을 벗어나면 break로 탈출시켰다.
//    k가 arr의 길이와 같아졌다는 것은 해당 단어를 만들 수 있다는 뜻이기 때문에 탈출시키고,
//    id가 arr에 있는 알파벳을 벗어났다는 것은 만들 수 없다는 뜻이기 때문에 탈출시킨다.
// #4 만약 k가 arr의 길이와 같다면 ans을 탐색해서 1이면 push, 0이면 pop을 출력시켰다.
//    만약 k가 arr의 길이와 같지 않다면 impossible을 출력시켰다.
