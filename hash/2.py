#https://programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    answer = True
    hashMap = dict()
    phone_book.sort()

    for phoneNo in phone_book : #숫자하나씩 딕셔너리에 담음
        hashMap[phoneNo] = 1

    for phoneNo in phone_book:
        tmp = ''
        for no in phoneNo: 
            tmp += no
            if tmp in hashMap and tmp != phoneNo: #딕셔너리 키로 같지만 전체 숫자가 다른경우
                answer = False
    return answer

print(solution(["119", "97674223", "1195524421"]))