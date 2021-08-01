#https://programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations): 
    citations = sorted(citations)  #인용 횟수를 오름차순으로 정렬
    n = len(citations) #H-Index 초기값: 0  #논문이 제출되면 0 번 인용 횟수를 가진 논문은 0개 이상
    h_index = 0 
    for idx, citation in enumerate(citations): #i번째 인용 횟수가 남은 논문의 수보다 많은 지점에 최대 H-Index 가 결정 
        if citation >= (n - idx): 
            h_index = (n - idx) 
            break 
    return h_index

#i 번째 인용 횟수 citations[i] 보다 많은 인용 횟수를 가진 논문의 수 = (전체 논문의 수 - i)
#H Index의 최댓값 = citations[i]가 (전체 논문의 수 - i) 보다 크거나 같은 시점에서 결정

print(solution([3, 0, 6, 1, 5]))