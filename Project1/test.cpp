#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
char s[1010];
int stk[1010], top = -1;
queue<int> q;
int main() {
    int answer = -1;
    scanf("%s", &s);
    for (int i = 0; s[i] != 0; i++) {
        q.push(s[i]);
    }
    printf("%d", answer);
}