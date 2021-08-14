#https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3
import heapq
def solution(jobs):
    answer = 0
    heapJob = []
    start, now, end = -1, 0, 0
    jobsAll = len(jobs)

    while end < jobsAll:
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heapJob, [job[1], job[0]])
        if heapJob:
            minJob = heapq.heappop(heapJob)
            start = now
            now += minJob[0]
            answer += now - minJob[1]
            end += 1
        else:
            now += 1

    return answer // jobsAll
# heapJob : jobs의 최소힙
# start 변수 : 시작시간으로 처음에는 -1에서 0 범위의 작업을 찾아야되서 -1로 초기화
# now 변수 : 현재시간
# end 변수 : 완료된 작업의 수
# jobsAll : 작업의 수
# 1) while문으로 모든 작업을 완료할 때까지 실행
# 2) for문으로 주어진 작업을 반복
# 3) heapJob에 push(최소힙), 0번 인덱스를 기존으로 정렬되므로 0번 인덱스에 작업처리 시간 입력
# 4) 최소 힙에 작업이 들어와 있으면 최소힙으로 최소 시간(minJob) 작업 꺼냄
# 5) start 변수에 시작 시간에 현재 시간을 입력
# 6) now 변수에 현재시간에 최소시간 작업을 처리한 시간을 입력
# 7) answer에 현재시간 - 최소시간 작업을 입력받은 시점 입력
# 8) 작업을 처리하면 end +1
# 9) 최소힙에 아무것이 없어도 현재시간은 흘러야 되므로 +1

print(solution([[0, 3], [1, 9], [2, 6]]))