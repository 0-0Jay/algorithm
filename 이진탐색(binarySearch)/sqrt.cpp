// 제곱근 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=523&sca=3010

#include <stdio.h>
#include <math.h>

int main() {
	long long n, m;  // #1
	scanf("%lld", &n);
	long long l = 0, r = n;  // #2
	while (1) {
		if (l > r) {
			printf("%lld", r);
			break;
		}
		m = (l + r) / 2;
		if (pow(m, 2) <= n) l = m + 1;
		else if (pow(m, 2) > n) r = m - 1;  // #3
	}
}

// #1 입력값의 범위가 2의 63제곱 이기 때문에 자료형으로 long long을 사용했다.
// #2 제곱근의 정수부분을 탐색해야 하므로 left를 0, right를 입력한 수(n)로 두고 이진탐색을 수행했다.
// #3 만약 m의 제곱이 n보다 작으면 right를 내리고, 크면 left를 올려서 탐색했다.
//    이 때, 주어진 n의 제곱근이 반드시 정수인 것이 아니며 제곱근의 정수부분을 구해야 하므로 n의 제곱근의 소숫점 자리를 내린 값을 구해야 한다.
//    예를 들어, 2의 제곱근의 정수값을 구한다면, 2의 제곱근 값인 1.414에서 0.414를 내림한 1을 도출해야 한다. 그 과정을 이진탐색하는 과정은 다음과 같다.
/*    l   0     1+1     2 
      m   1      2      1    
      r   2      2      1    -> l이 r보다 커졌으므로 r을 도출
*/
//    m을 출력하지 않는 이유는 m은 소숫점 부분을 올림한 값을 탐색하기 때문이다.   예시 ) 1.414 -> 2 
