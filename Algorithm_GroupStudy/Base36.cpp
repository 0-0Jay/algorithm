// 백준 1036번 36진수 : https://www.acmicpc.net/problem/1036

/*
스터디 인원들과 회의한 결과 : 
0~Z까지 각 숫자별 총합을 계산 -> 이 합은 따로 누적
Z로 각 숫자별 총합을 계산한 값과 기존 값의 차를 저장
그 차를 크기순으로 내림차순 정렬
K인덱스만큼 그 값을 더함

위 계산을 계산하려고 하니 최대 50자리라는 조건에 의해 데이터가 터지는 문제 발생
*/
