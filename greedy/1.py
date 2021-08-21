#https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    #reverse 리스트 내 학생들 중에서 lost 리스트 내의 일치하는 학생들이 있을 경우 빌려줄 수 없음.
    reserve_st = [r for r in reserve if r not in lost]
    lost_st = [l for l in lost if l not in reserve]

    for i in reserve_st:    #도난당한 학생 앞뒤로 여벌이 있는 학생이 있는지 검사
        left = i-1  
        right = i+1
        if left in lost_st:
            lost_st.remove(left) #도난당한 학생이면 체육복 제공후 리스트에서 제외
        elif right in lost_st:
            lost_st.remove(right)
    return n-len(lost_st) # 수업을 들을수 있는 학생들 : 전체 수(n)-잃어버린학생 수(lost_st)

print(solution(5,[2,4],[1,3,5]))#5
print(solution(5,[2,4],[3]))#4