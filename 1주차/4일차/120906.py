def solution(n):
    answer = 0
    numlist = list(map(int, str(n)))
    for i in numlist:
        answer += i
    return answer