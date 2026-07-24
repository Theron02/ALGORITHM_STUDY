def solution(numbers):
    answer = 0
    sorted_numbers = sorted(numbers)
    answer = sorted_numbers[-1] * sorted_numbers[-2]
    return answer