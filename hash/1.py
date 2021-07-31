#https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    participant.sort()  #sort: 리스트 원본값을 직접 수정
    completion.sort()   # 1) participant와 completion을 정렬함
    for parti, compl in zip(participant, completion): #zip: python내장함수로 같은 인덱스끼리 짝지음(배열의 길이가 다를 경우 남는 인덱스는 zip 객체에서 제외)
        if parti != compl:
            return parti
    return participant[-1]
            
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))