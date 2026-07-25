# 소수 찾기
# def solution(nums):
#     answer = 0
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             for k in range(j+1, len(nums)):
#                 sum = nums[i] + nums[j] + nums[k]
#                 q = 2
#                 if sum < 2:
#                     break
#                 while q  <= sum ** 0.5:
#                     if sum % q == 0:
#                         break
#                     q += 1
#                 else : 
#                     answer += 1
#     return answer

# 함수 분리
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    size = len(nums)
    for i in range(size):
        for j in range(i+1, size):
            for k in range(j+1, size):
                if is_prime(nums[i] + nums[j] + nums[k]):
                    answer += 1
    return answer

