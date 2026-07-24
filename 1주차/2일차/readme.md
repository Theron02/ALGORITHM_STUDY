# 2일차 문제 풀이

## 배열의 평균값
정수 배열 `numbers`가 매개변수로 주어집니다. `numbers`의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

**풀이** : answer에 numbers의 요소들을 다 넣은 후, numbers의 길이로 나눔.

```python
def solution(numbers):
    answer = 0
    for i in numbers : 
        answer += i
    return answer/len(numbers)
```

## 아이스 아메리카노
머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 아이스 아메리카노는 한잔에 5,500원입니다. 머쓱이가 가지고 있는 돈 `money`가 매개변수로 주어질 때, 머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

**풀이** : answer 배열에 money를 5500으로 나눈 몫과, 나머지를 차례대로 추가함.

```python
def solution(money):
    answer = []
    answer.append(money // 5500)
    answer.append(money % 5500)
    return answer
```

## 배열 뒤집기
정수가 들어 있는 배열 `num_list`가 매개변수로 주어집니다. `num_list`의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.

**풀이** : .reverse() 함수를 이용해 배열을 뒤집음.

```python
def solution(num_list):
    answer = []
    num_list.reverse()
    answer = num_list
    return answer
```

## 뒤집힌 문자열
문자열 `my_string`이 매개변수로 주어집니다. `my_string`을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.

**풀이** : my_string을 리스트에 담아, .reverse()로 뒤집고, .join으로 문자열로 만듦.

```python
def solution(my_string):
    answer = ''
    arr = list(my_string)
    arr.reverse()
    answer = ''.join(arr)    
    return answer
```


## 짝수 홀수 개수
정수가 담긴 리스트 `num_list`가 주어질 때, `num_list`의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

**풀이** : even_count, odd_count를 만들어 배열의 요소가 2로 나누어 떨어지면 even_count를 1증가, 그렇지 않으면 odd_count를 1 증가 시킨 후, 순서대로 answer에 추가함.

```python
def solution(num_list):
    answer = []
    even_count = 0
    odd_count = 0
    for i in num_list:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    answer.append(even_count)
    answer.append(odd_count)
    
    return answer
```

## 문자 반복 출력하기
문자열 `my_string`과 정수 n이 매개변수로 주어질 때, `my_string`에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.

**풀이** : 배열의 요소를 n번 곱해 answer에 추가함.

```python
def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i * n
    return answer
```

## 특정 문자 제거하기
문자열 `my_string`과 문자 letter이 매개변수로 주어집니다. `my_string`에서 `letter`를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

**풀이** : 반복문과 조건문을 이용해, 배열의 요소가 letter 안에 없으면 answer에 추가함.

```python
def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i != letter:
            answer += i
    return answer
```

## 각도기
각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다. 각 `angle`이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.
- 예각 : 0 < `angle` < 90
- 직각 : `angle` = 90
- 둔각 : 90 < `angle` < 180
- 평각 : `angle` = 180

**풀이** : 조건문을 이용함

```python
def solution(angle):
    answer = 0
    if angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle < 180:
        answer = 3
    else:
        answer = 4
    return answer
```

## 양꼬치
머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다. 양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다. 정수 `n`과 `k`가 매개변수로 주어졌을 때, 양꼬치 `n`인분과 음료수 `k`개를 먹었다면 총얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요.

**풀이** : answer에 기본적으로 n*12000 + k*2000을 해놓은 후, 조건문으로 n을 10으로 나눈 몫에 2000을 곱해서 뺌.

```python
def solution(n, k):
    answer = 0
    answer = n * 12000 + k * 2000
    if n // 10 > 0:
        answer -= (n // 10) * 2000
    return answer
```

## 짝수의 합
정수 `n`이 주어질 때, `n`이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

**풀이** : 반복분을 이용해, n+1까지 2로 나누어 떨어지는 값을 answer에 더함.

```python
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            answer += i
    return answer
```