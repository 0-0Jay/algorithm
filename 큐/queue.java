// 자바 10845번 큐 : https://www.acmicpc.net/problem/10845

#include<stdio.h>
#include<string.h>
int arr[10001], qf = 0, qr = 0;
char cmd[6];
int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s", &cmd);
        if (strcmp(cmd, "push") == 0) {
            scanf("%d", &arr[qr++]);
        }
        else if (strcmp(cmd, "front") == 0) {
            if (qr - qf > 0) printf("%d\n", arr[qf]);
            else printf("-1\n");
        }
        else if (strcmp(cmd, "back") == 0) {
            if (qr - qf > 0) printf("%d\n", arr[qr - 1]);
            else printf("-1\n");
        }
        else if (strcmp(cmd, "pop") == 0) {
            if (qf < qr) printf("%d\n", arr[qf++]);
            else printf("-1\n");
        }
        else if (strcmp(cmd, "size") == 0) {
            printf("%d\n", qr - qf);
        }
        else if (strcmp(cmd, "empty") == 0) {
            if (qr - qf == 0) printf("1\n");
            else printf("0\n");
        }
    }
    return 0;
}
