# 기능 개발
## 배열의 길이는 100개 이하.


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

# progresses = [93, 30, 55]
# speeds = [1, 30, 5]

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

print(solution(progresses, speeds))