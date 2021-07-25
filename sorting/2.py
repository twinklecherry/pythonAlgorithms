#https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3

def solution(numbers):
    answer = '' 
    num1 = [str(i)*3 for i in numbers]
    nums = list(enumerate(num1))
    nums.sort(key = lambda x:x[1], reverse = True)
    for index, value in nums:
        answer += str(numbers[index])
        
    return str(int(answer))
    
solution([3, 30, 34, 5, 9]	)