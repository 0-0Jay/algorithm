# 프로그래머스 - 과제 진행하기 : https://school.programmers.co.kr/learn/courses/30/lessons/176962

def solution(plans):
    for i in plans:
        i[1] = int(i[1][:2]) * 60 + int(i[1][3:])
        i[2] = int(i[2])
    plans.sort(key=lambda x: x[1])  # 시작 시간을 기준으로 정렬
    no_fin = []   
    answer = []
    time = 0
    size = len(plans)
    plans.append(["", 2000, 0])  # 배열 인덱스 처리에 편의성을 위해 임의로 최고값 삽입
    
    for p in range(size):
        # 현재 과제가 다음 과제 시작시간 전에 안끝나는 경우
        if plans[p][1] + plans[p][2] > plans[p + 1][1]:  
            no_fin.append([plans[p][0], plans[p][1] + plans[p][2] - plans[p + 1][1]])
            time = plans[p + 1][1]
        # 끝나는 경우
        else:
            answer.append(plans[p][0])
            time = plans[p][1] + plans[p][2]
            # 현재 시각이 다음 과제 시작시간인 경우
            if time == plans[p + 1][1]:
                continue
            # 현재 시각이 다음 과제 시작시간 전이며, 중단한 과제가 있는 경우
            while time < plans[p + 1][1] and len(no_fin) > 0:
                tmp = no_fin.pop()
	   # 중단한 과제 1개가 다음 과제 시작전에 못끝내는 경우
                if plans[p + 1][1] < time + tmp[1]:
                    no_fin.append([tmp[0], time + tmp[1] - plans[p + 1][1]])
                    time = plans[p + 1][1]
                # 끝내는 경우
                else:
                    answer.append(tmp[0])
                    time += tmp[1]
        
    while no_fin:
        answer.append(no_fin.pop()[0])  # 중단했던 과제 남은 거 처리
                
    return answer

# 알고리즘 : 시뮬레이션
'''
풀이 : time변수에 시간을 두고 과제 진행 시마다 time을 이동시켜서 해결한다.
문제의 각 조건분기에 적어둔 주석에 따라 과제를 no_fin과 answer에 적절히 분배한다.
answer에 끝난 과제를 다 넣었다면, no_fin에 남아있는 중단했던 과제들을 pop을 사용해 마지막 것부터 answer로 옮겨준다.
'''
