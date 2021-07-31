#https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3
def solution(clothes): #key:옷종류 value:옷종류 수
    answer = 1
    kind = dict() #dictionary(해시 테이블로 구현): 빠른 속도로 자료를 탐색가능

    for cloth in clothes: #for문으로 종류마다 옷개수 저장
        if(cloth[1] not in kind.keys()):
            kind[cloth[1]] = 1
        else:
            kind[cloth[1]] += 1

    kindCnt = list(kind.values())

    for kCnt in kindCnt: #dictionary의 key값가져옴
        answer = answer * (kCnt+1) #안입는 경우도 존재하니 모두 곱함

    return answer-1 #아무것도 입지않는 경우 제외 (a+1)(b+1)(c+1)-1

print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))