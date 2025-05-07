// DNA 조합 : http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1478&sca=3030

#include<stdio.h>
#include<string>
using namespace std;
 
int n, m = 100, check[7];
char arr[7][8];

void dna(string s, int d, string bef) {  // #1
	if (s.length() > m) return;
	if (d == n) {
		if (m > s.length()) m = s.length();  // #2
		return;
	}
	for (int i = 0; i < n; i++) {
		if (check[i] == 1) continue;  // #3
		string r = arr[i];
		int tmp = 0;  // #4
		for (int j = 1; j <= r.length() && j <= bef.length(); j++) {
			if (bef.substr(bef.length() - j, j) == r.substr(0, j)) tmp = j;  // #5
		}
		check[i] = 1;
		dna(s + r.substr(tmp),d + 1, r);  // #6
		check[i] = 0;
	}
	return;
}

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", &arr[i]);
	}
	dna("", 0, "");  // #7
	printf("%d", m);
}

// arr배열에 입력으로 주어지는 모든 DNA 조각을 저장했다. check배열은 중복된 조각을 탐색하지 않도록 하기 위한 장치로 사용했다.
// #1 함수에 현재 조합된 DNA(s), 탐색한 조각 수(d), 이전에 탐색한 DNA 조각(bef)를 인수로 주었다.
//    이 때, bef가 필요한 이유는 문제의 조건인 '인접한 문자열의 공통부분만 제거할 수 있다.'를 만족하기 위함이다.
//    만약, bef가 아닌 s를 현재 탐색하는 조각과 비교하게 된다면 AT, T, ATGC의 경우 ATGC가 나오게 된다.
//      > 과정) AT <-> T == A(T) / AT <-> ATGC == (AT)GC / ATGC         * () : 중복되어 겹칠 수 있는 부분
//    그러나 문제의 요구사항을 해결하기 위해서는  AT와 T, T와 ATGC만 비교해서 ATATGC로 조합해야 한다.
//      > 과정) AT <-> T == A(T) / [A]T <-> ATGC = [A]TATGC / ATATGC    * [] : 이전 조각이므로 고정되는 부분
// #2 d가 n과 같다는 것은 모든 조각을 탐색했다는 의미이므로 현재 조합된 DNA배열의 길이를 m과 비교해, 최소값만 저장하게 했다.
// #3 check배열은 arr배열의 인덱스를 공유시켰다. 즉 arr[i]를 탐색했다면, check[i]에 1이 저장되고, check[i]가 1인지 확인하는 것으로 중복 탐색을 방지했다.
// #4 tmp는 현재 탐색중인 문자열의 길이를 저장했다.
//    예를 들어, tmp가 2이면 bef의 오른쪽 끝부터 2개, r(현재 탐색중인 조각)의 왼쪽 끝부터 2개를 비교한다.
// #5 #1에서 설명한 바와 같이, bef의 오른쪽 끝부터, r의 왼쪽 끝부터 시작하여 substr을 이용해 같은 길이의 문자열을 잘라서 비교했다.
//    두 문자열이 같다면, tmp에 얼만큼의 길이를 자르면 같은지 저장했다.
//    break 문을 쓰지 않은 이유는 이후의 길이를 탐색했을 때 또 같은 부분이 발생할 수 있기 때문이다.
// #6 s에 r에서 공통된 부분을 잘라낸 문자열을 조합하고, d + 1로 다음조각으로 넘어가게 했다. bef에는 방금 탐색한 조각인 r을 주었다.
