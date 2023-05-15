// 트리 순회 : https://www.acmicpc.net/problem/1991

#include <stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

struct tmp {
	char m, l, r;
};

vector<tmp> tree;

int chk(tmp i, tmp j) {
	return i.m < j.m;
}

void preorder(tmp node) {  // #1
	printf("%c", node.m);
	if (node.l != '.') preorder(tree[node.l - 65]);  // #2
	if (node.r != '.') preorder(tree[node.r - 65]);
	return;
}

void inorder(tmp node) {
	if (node.l != '.') inorder(tree[node.l - 65]);
	printf("%c", node.m);
	if (node.r != '.') inorder(tree[node.r - 65]);
	return;
}

void postorder(tmp node) {
	if (node.l != '.') postorder(tree[node.l - 65]);
	if (node.r != '.') postorder(tree[node.r - 65]);
	printf("%c", node.m);
	return;
}

int main(void) {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		char m, l, r;
		cin >> m;
		cin >> l;
		cin >> r;
		tree.push_back({ m, l, r });
	}
	sort(tree.begin(), tree.end(), chk);  // #3
	preorder(tree[0]);
	printf("\n");
	inorder(tree[0]);
	printf("\n");
	postorder(tree[0]);
}

// #1 이진 트리에서 preorder(전위 탐색), inorder(중위 탐색), postorder(후위 탐색)은 동작할 탐색 내용이 포인터(left, right)를 기준으로 어디에 위치하는지에 따라 달라진다.
//    전위 탐색은 left 포인터로 이동하기 전, 중위 탐색은 right 포인터로 이동하기 전, 후위 탐색은 모든 포인터를 탐색한 후에 출력문을 삽입했다.
// #2 해당 노드에 도착하면 포인터(l, r)의 값에 - 65(char 'A')를 한 값을 인덱스로 하여 tree에서 해당 알파벳으로 이동할 수 있게 했다.
// #3 값은 대문자로 주어지기 때문에 각 노드(m)에서 포인터가 어느 노드(l, r)를 다음 노드로 지목하고 있는지를 tree 벡터에 저장했다.
//    이 후, char와 정수를 연산할 수 있다는 점을 활용하기 위해 각 노드를 알파벳 순서로 정렬했다.
