#https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) > 1:
            answer += 1
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a + b *2)
        else:
            return -1
    return answer

# 파이썬은 'heapq' 함수 제공 : 기본적으로 오름차순이며 내림차순은 별도의 솔루션 필요
# 1) 기존의 scoville 리스트를 오름차순 heapQ로 변환(heapq.heapify(list))
# 2) while 함수로 가장작은 수가 기준보다 낮다면 계속
# 3) heapq.heappop(list)로 가장 작은 값을 return하며 삭제
# 4) heapq.heappush(list, value)로 scoville에 a+b*2를 삽입, 자동으로 정렬
# heapQ를 사용하지 않을경우는 sort사용 가능하지만 효율성을 따질 때는 heapQ를 사용
print(solution([1, 2, 3, 9, 10, 12],7))