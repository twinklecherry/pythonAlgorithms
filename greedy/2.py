#https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3
def solution(name):
    name_al = [min(ord(i) - ord('A'), ord('Z') - ord(i)+1) for i in name]
    idx, answer = 0, 0
    while True:
        answer += name_al[idx]
        name_al[idx] = 0
        if sum(name_al) == 0:
            break
        left, right = 1, 1
        while name_al[idx - left] == 0:
            left += 1
        while name_al[idx + right] == 0:
            right += 1
        answer += left if left<right else right
        idx += -left if left<right else right
    return answer

# 1) name_al 에 min함수를 사용해 name에 대한 최소한의 이동을 구한다.
# 2) answer에 모든 합을 더해 조이스틱의 가동횟수를 구한다.
# 3) 현재 위치인 idx에서 left와 right로 이동하며 먼저 만나는 방향을 찾는다.
# 4) 만나는 방향(left or right)의 인덱스를 찾는다.

print(solution("JEROEN"))#56
print(solution("JAN"))#23