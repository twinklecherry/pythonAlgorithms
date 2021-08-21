#https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3
def solution(brown, yellow):
    total = brown + yellow
    answer = []

    for col in range(3, total):
        row = int(total / col)
        # 카펫의 가로 길이는 세로길이와 같거나 세로 길이보다 길다는 조건
        if( ((row * col) == total) & (row >= col) & ( ((col-2) * (row-2)) == yellow)):                
            answer = [row, col]
            break
    return answer

print(solution(10,2))#4,3
print(solution(8,1))#3,3