#https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3
from heapq import heappush
def solution(operations):
    aw = []    
    for oper in operations:
        if oper.startswith("I"): #I로 시작한다면 뒤에 있는 숫자만을 리스트에 남겨놓는다.
            heappush(aw,int(oper[2:]))
        elif aw and oper == "D 1":   #if조건문으로 'D 1'일 경우, 최대값을 삭제한다.
            aw.pop()
        elif aw and oper == "D -1": #if조건문으로 'D -1'일 경우, 최소값을 삭제한다.
            aw.pop(0)
    if not aw:
        return [0,0]
    else :
        return [max(aw), min(aw)] 

print(solution(["I 16","D 1"])) #[0,0]
print(solution(["I 7","I 5","I -5","D -1"]))