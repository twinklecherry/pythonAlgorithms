#https://programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    genreScore = dict() # 장르별 속한 노래의 총 점수
    chk = dict() # 노래 고유번호를 key, 해당노래가 속한 장르점수 및 개별점수를 value
    
    for i in range(len(genres)): 
        genreScore[genres[i]] = genreScore.get(genres[i], 0) + plays[i] 
    
    for i in range(len(genres)): 
        chk[i] = [genreScore[genres[i]], plays[i]] 
    
    chk = sorted(chk.items(), key=lambda x: (x[1], -x[0]), reverse=True) 
    genreScore = sorted(genreScore.items(), key=lambda x:x[1], reverse=True) 
    
    start = 0 
    result = []
    for gs in genreScore: 
        cnt = 0 
        for i in range(start, len(chk)): 
            if chk[i][1][0] == gs[1] and cnt < 2: 
                start += 1 
                result.append(chk[i][0]) 
                cnt += 1 
    return result

# 1) for문을 사용해 두 딕셔너리 값 설정
# 2) sorted를 이용해 딕셔너리 정렬
# 3) 먼저 수록된 기준 1번을 맞추기 위해 genreScore 내림차순 정렬
# 4) chk를 sorted안에서 람다식으로 chk점수로 내림차순 정렬한 뒤 고유번호로 오름차순으로 정렬
# 5) for문으로 순서대로 추출
# 6) if문으로 장르별 두개씩 추출하기 위해 cnt에 각 장르별 추출된 횟수 카운트
# 7) for문이 이미 탐색한 장르를 재탐색할 수 없게 start 변수 지정

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))