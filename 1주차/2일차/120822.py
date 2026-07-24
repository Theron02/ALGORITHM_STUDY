def solution(my_string):
    answer = ''
    arr = list(my_string)
    arr.reverse()
    answer = ''.join(arr)    
    return answer