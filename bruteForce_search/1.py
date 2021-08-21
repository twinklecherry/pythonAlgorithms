#https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3
def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    aCnt, bCnt, cCnt = 0,0,0

    for i in range(0,len(answers)):
        if a[i%5] == answers[i] :   #시험은 최대 10,000문제로 구성되어있으므로 리스트의 길이 맞춤
            aCnt += 1
        if b[i%8] == answers[i]:
            bCnt += 1
        if c[i%10] == answers[i]:
            cCnt += 1
    cntDict = {1:aCnt, 2:bCnt, 3:cCnt} #딕셔너리로 key와 value를 담음
    topScore = max(cntDict.values())
    result = [student for student, score in cntDict.items() if score == topScore]
    return result

print(solution([1,2,3,4,5]))#[1]
print(solution([1,3,2,4,2]))#[1,2,3]