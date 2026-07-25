# 연속된 중복 숫자 제거
# answer에 arr[i]를 넣고, 
# answer[i]와 answer[i-1]이 같으면 pop()으로 제거

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if len(answer) == 0:
            answer.append(arr[i])
        elif answer[-1] != arr[i]:
            answer.append(arr[i])
    return answer