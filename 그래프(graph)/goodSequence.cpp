// 좋은 수열 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=306&sca=3030

#include <stdio.h>
#include <stdlib.h>
#include <string>
using namespace std;

int n, id = 0;
string num = "1";

void arr(int a, int d) {
    for (int j = 1; j <= num.size() / 2; j++) {  // #2
        if (num.size() > 1 && num.substr(num.size() - j * 2, j) == num.substr(num.size() - j, j)) {
            num = num.substr(0, num.size() - 1);
            return;
        }
    }
    if (d == 0) {  // #3
        for (int i = 0; i < num.size(); i++) {
            printf("%c", num[i]);
        }
        exit(0);
        return;
    }
    for (int i = 1; i <= 3; i++) {  // #4
        if (a != i) {
            num += i + 48;
            arr(i, d - 1);
        }
    }
    num = num.substr(0, num.size() - 1);  // #5
    return;
}

int main() {
    scanf("%d", &n);
    arr(1, n - 1);  // #1
}

// #1 1로 시작하면 시작이 2, 3일때의 경우는 당연히 최소값이 아닐 것이므로 탐색하지 않기 위해 1로 주었다.
//    따라서 남은 수열 길이도 n-1로, num도 '1'을 저장한 상태로 시작했다.
// #2 8글자를 다 채운 것을 검사하는 것보다 먼저 반복되는 숫자가 발생하는 구간이 있는지 검사했다.
//    왜냐하면 #3의 조건과 순서가 바뀌었을 경우 8자를 채우면 무조건 출력이 되기 때문이다.
// #3 #2의 조건을 검사했음에도 return되지 않았다면 d(남은 수열 길이)가 0인지 확인했다.
//    만약 0이면 num을 출력하고, exit(0)로 프로그램을 종료시켜 이후의 탐색을 수행하지 않게 했다.
//    exit(0) 대신 return을 사용하게 되면, 해당 수열을 출력하고 다시 부모 노드로 돌아가 다음 자식 노드를 탐색하게 되어 가능한 모든 수열을 출력하게 된다.
// #4 1, 2, 3을 순서대로 인수로 주기 위해 for문을 활용했다. 숫자를 오름차순으로 탐색하기 때문에 #3에서 exit(0)가 최초로 수행되는 수열이 항상 최소값이 된다.
// #5 만약에 #4의 1, 2, 3을 모두 넣어봤음에도 가능한 수열이 없다면 현재 수열에서 하나를 제거하고 이전 단계에서 다음 노드를 탐색했다.
