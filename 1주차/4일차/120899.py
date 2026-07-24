def solution(array):
    answer = []
    max = 0
    max_index = 0
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
            max_index = i
    answer.append(max)
    answer.append(max_index)
    return answer