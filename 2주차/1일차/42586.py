def solution(progresses, speeds):
    answer = []
    days = []
    cnt = 1
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            days.append((100 - progresses[i]) // speeds[i])
        else:
            days.append((100 - progresses[i]) // speeds[i] + 1)
    for i in range(1, len(days)):
        if days[i] > days[i-1]:
            answer.append(cnt)
            cnt = 1
        elif days[i] <= days[i-1]:
            cnt += 1
            days[i] = days[i-1]
    answer.append(cnt)
   
    return answer


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))