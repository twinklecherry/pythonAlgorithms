#https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3
from collections import deque
def solution(priorities, location):
    answer = 0
    arr = deque([(v,i) for i, v in enumerate(priorities)])

    while len(arr):
        docu = arr.popleft()
        if any(docu[0] <a[0] for a in arr ):
            arr.append(docu)
        else:
            answer += 1
            if docu[1] == location:
                break
    return answer

# 1) deque 자료형으로 popleft() 사용해 시간복잡도를 O(1)로 효율적으로 사용
# 2) enumerate를 사용해 index와 value를 함께 사용가능
# 3) docu보다 max값이 크면 배열에 담고 그렇지 않은 경우는 answer에 +1
# 4) docu의 index가 location과 동일하면 반복문 종료하고 answer 반환
# 5) 파이썬 내장함수인 any(x) 사용   <-----> all(x)
# : 반복 가능한(iterable) 자료형 x를 입력 인수로 받음.
# : 이 x의 요소 중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때에만 False


print(solution([1, 1, 9, 1, 1, 1],0))