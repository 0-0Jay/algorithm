// 택배 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1903&sca=3050

#include <stdio.h>
#include <algorithm>
using namespace std;

struct tmp {
    int fr, to, am;
} vil[2001];

int chk(tmp i, tmp j)
{ 
    return i.to < j.to;                                      
}

int n, c, m, box[2001], load, sum, t;

int main()
{
    scanf("%d%d%d", &n, &c, &m);
    for (int i = 1; i <= m; i++) {                            
        scanf("%d%d%d", &vil[i].fr, &vil[i].to, &vil[i].am);  
    }
    sort(vil + 1, vil + 1 + m, chk);  // #1
    for (int i = 1; i <= m; i++) {
        t = 0; load = 0;  // #2
        for (int j = vil[i].fr; j < vil[i].to; j++) {        
            if (box[j] > t) t = box[j];  // #3
        }
        if (vil[i].am > c - t) load = c - t;              
        else load = vil[i].am;  // #4    
        for (int j = vil[i].fr; j < vil[i].to; j++) {         
            box[j] += load;  // #5                            
        }                                                  
        sum += load;  // #6                               
    }
    printf("%d", sum);                              
    return 0;
}

// box는 현재 마을에서 실을 박스 양을 저장할 배열
// #1 목적지를 기준으로 오름차순 정렬했다. 택배를 최대한 많이 싫으려면 가까운 목적지부터 가야 트럭을 비우고 택배를 더 실을 수 있기 때문이다.
// #2 t에는 현재 트럭에 실린 박스를, load에는 운반한 박스 양을 저장했다.
// #3 box 배열을 확인해서 최대로 실을 수 있는 양을 t에 저장했다.
// #4 만약에 트럭의 남은 용량(c - t)이 현재 마을에서 배송해야 하는 박스 양보다 작으면 트럭의 남은 용량만 채우고, 아니면 모든 박스를 트럭에 적재했다.
// #5 각 마을을 지나면서 해당 마을에 도착했을 때 적재한 박스양을 누적했다.
// #6 마지막으로 적재한 박스양을 최종적으로 운반한 박스 양에 누적했다.
