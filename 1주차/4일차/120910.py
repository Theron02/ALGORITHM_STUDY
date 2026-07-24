def solution(n, t):
    answer = n
    for i in range(t):
        answer += n
        n *= 2
    return answer