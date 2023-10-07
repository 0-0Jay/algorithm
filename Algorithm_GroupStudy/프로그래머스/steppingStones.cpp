// 2019 카카오 개발자 겨울 인턴십 - 징검다리 건너기 : https://school.programmers.co.kr/learn/courses/30/lessons/64062#

#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> stones, int k) {
	vector<int> s(stones.size());
	copy(stones.begin(), stones.end(), s.begin());  // s에 stones 복사
	sort(s.begin(), s.end());  // s 정렬
	s.erase(unique(s.begin(), s.end()), s.end());  // s에 중복 제거
	
  int l = 0, r = s.size() -1 , mid;
  
	while (l <= r) {
		mid = (l + r) / 2;
		int maxCnt = 0;
		int cnt = 0;

		for (int i : stones) {
			if (i <= s[mid]) {
				cnt++;
				if (maxCnt < cnt) maxCnt = cnt;
			}
			else cnt = 0;
		}

		if (maxCnt >= k) r = mid - 1;
		else l = mid + 1;
	}
  
	return s[l];
}

// 알고리즘 : 이분탐색(binary search)
/*
풀이 : 디딤돌의 숫자를 중복없이 오름차순으로 가지고 있는 서브 배열을 하나 생성하여 이분 탐색
1. stones의 디딤돌 숫자를 오름차순으로 가지고 있는 배열 s를 만든다.
2. 인덱스를 기준으로 l을 0번, r를 (s.size() - 1)번으로 둔다.
3. stones를 순회하면서 s[mid]보다 작으면 s[mid]번째 인원이 지나갈 때 점프해야 하므로 카운트 한다.
  3-1. 만약 크거나 같으면, 카운트를 초기화 한다.
  3-2. maxCnt에 이번 탐색의 최대 카운트를 저장한다.
4. 만약 maxCnt가 k보다 크거나 같으면 r을 내리고, 작으면 l을 올린다.
  4-1. 만약 maxCnt가 같은 경우 r을 한번 더 내려도 가능한지 추가 탐색을 수행해야 한다.
5. r을 계속 낮추다가 l이 r보다 커지면, s[l]을 출력한다.
*/
