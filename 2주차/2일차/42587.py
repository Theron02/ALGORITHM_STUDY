def solution(priorities, location):
    answer = 0
    while len(priorities) > 0:
        max_priority = max(priorities)
        if priorities[0] == max_priority:
            answer += 1
            priorities.pop(0)
            if location == 0:
                break
            else:
                location -= 1
        else:
            priorities.append(priorities.pop(0))
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer