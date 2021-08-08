#https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3
from collections import deque #스택과 큐를 일반화 O(1)
def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        if progresses[0] >= 100:
            while progresses:
                if progresses[0] >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    cnt += 1
                else:
                    break
            answer.append(cnt)
    return answer

#1) progresses 리스트와 speeds 리스트의 값을 하나씩 넣습니다.
#2) speeds와 progresses의 요소들을 각각 인덱스 순서로 더합니다.
#3) 더한 값이 100이 될때 return 1을 합니다.
#4) if문으로 앞의 더한 값이 100이 되지 않았지만, 뒤의 값w이 100일때 앞의 남은 개수만큼 return합니다.
 
print(solution([93, 30, 55],[1, 30, 5]))