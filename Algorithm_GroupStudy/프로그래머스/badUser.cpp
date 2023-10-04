// 2019 카카오 개발자 겨울 인턴십 - 불량 사용자 : https://school.programmers.co.kr/learn/courses/30/lessons/64064

#include <string>
#include <vector>
#include <math.h>
using namespace std;

int chk[8], cnt, comb[256];
vector<string> user, ban;

bool check(string u, string b) {
    if (u.length() != b.length()) return false;
    int i;
    for (i = 0; i < u.length(); i++) {
        if (u[i] != b[i] && b[i] != '*') return false;
    }
    return true;
}

void back(int d) {
    if (d == ban.size()) {
        int tmp = 0;
        for (int i = 0; i < 8; i++) {  // 십진수로 치환
            tmp += chk[i] * pow(2, i);
        }
        if (comb[tmp] == 0) {  // 같은 조합이 중복 탐색되었는지 체크. 처음 만든 조합이면 cnt++
            comb[tmp]++;
            cnt++;
        }
        return;
    }
    for (int i = 0; i < user.size(); i++) {  // 백트래킹으로 제재아이디 경우의 수 탐색
         if (chk[i] == 0 && check(user[i], ban[d])) {
            chk[i] = 1;
            back(d + 1);
            chk[i] = 0;
         }
    }
}

int solution(vector<string> user_id, vector<string> banned_id) {
    int answer = 0;
    user = user_id;
    ban = banned_id;
    back(0);
    return cnt;
}

// 알고리즘 : 백트래킹 + 비트마스킹 응용
/*
풀이 : 백트래킹으로 가능한 조합을 모두 찾고, 비트마스킹을 활용해 동일한 경우를 배제했다.
1. 백트래킹으로 ban의 0번 인덱스부터 가능한 아이디를 하나씩 채워넣는다.(d를 1씩 증가시키며 ban 아이디를 하나씩 확인한다.)
  1-1. 현재 탐색중인 user가 ban[d]에 매칭될 수 있으면 chk배열의 해당 user 인덱스에 1로 체크한다.
2. ban에 제재 아이디가 모두 채워졌으면, chk배열의 각 인덱스를 이진수 자릿수로 보고 10진수로 치환한다.
  2-1. 예를 들어, 0번, 1번, 3번 인덱스에 1로 체크되어 있다면 다음과 같다.
       11010 -> (1 * 2^0) + (1 * 2^1) + (1 * 2^3) = 11
3. 2에서 만들어진 십진수를 활용해 comb에 체크하여 같은 조합은 카운트 되지 않도록 한다.
*/
