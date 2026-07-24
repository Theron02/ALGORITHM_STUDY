def solution(n, k):
    answer = 0
    answer = n * 12000 + k * 2000
    if n // 10 > 0:
        answer -= (n // 10) * 2000
    return answer