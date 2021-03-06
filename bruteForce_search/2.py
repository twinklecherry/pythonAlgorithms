#https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3
import math
from itertools import permutations

def is_prime_number(n):
    """소수판별 함수"""
    if n==0 or n==1:                                # 0,1 은 소수가 아님
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):   # sqrt(n)까지만 for문을 돌면서 확인하면 된다.
            if n % i == 0:                          # 2~sqrt(num)까지 나누어 떨어지는 숫자가 있으면 소수가 아님
                return False 
        return True                                 # for문을 다 돌았는데도 False가 아니면 소수

def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):              
        arr = list(permutations(numbers, i))        # permutations(순열)을 사용해 i개씩 묶어지는 list 생성
        for j in range(len(arr)):                   # 생성한 list(arr) 길이만큼 for문 실행
            num = int(''.join(map(str,arr[j])))     # list(arr)의 값들은 tuple들로 되어있으모 join(map(str,))을 사용해 join해준다
            if is_prime_number(num):                
                answer.append(num)                  # is_prime_number() 함수가 True일 경우 (= 소수일 경우) num 추가
    
    answer = list(set(answer))                      # 같은 값이 나올 수 있기 때문에 set()을 통해 중복값 제거
    return len(answer)

print(solution("17"))#3
print(solution("011"))#2

# permutations(순열) : 중복을 허용하지 않고 순서에 의미가 있다.
#   : 같은 값이라도 순서가 다르면 다른 값으로 인식
# -> permutations(반복 가능한 객체, n) // n=몇개를 뽑을 것인지
#