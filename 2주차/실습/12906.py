# 연속된 중복 숫자 제거
# len(answer)에 길이가 0일때는 arr[i]를 넣고, 
# answer[-1]과 arr[i]가 같지 않으면 arr[i]를 answer에 넣음.

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if len(answer) == 0:
            answer.append(arr[i])
        elif answer[-1] != arr[i]:
            answer.append(arr[i])
    return answer
