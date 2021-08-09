#https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3
from collections import deque
def solution(prices):
    length = len(prices)
    answer = [ i for i in range (length - 1, -1, -1)] # answer을 max값으로 초기화
    
    # 주식 가격이 떨어질 경우 찾기
    stack = [0]
    for i in range (1, length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer


# 1) 모든 prices 값이 떨어지지 않았다는 가정하에 answer값을 초기화시킴
# 2) 주식이 떨어질 경우를 찾음 : stack의 초기값에 index 0번을 넣어줌
# 3) prices를 for문으로 길이만큼 반복
# 4) stack이 존재할 경우, for문 값이 stack의 제일 위 인덱스의 prices의 값보다 작을 경우 아래과정 반복
# 5) stack에서 값을 pop()하고 pop한 index의 answer값을 작아질 경우의 index에서 pop한 index를 뺀 값으로 변경
# 6) stack에 반복하는 index를 append()

print(solution([1, 2, 3, 2, 3]))