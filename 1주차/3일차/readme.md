# 3일차 문제 풀이

## 배열 자르기
정수 배열 `numbers`와 정수 `num1`, `num2`가 매개변수로 주어질 때, `numbers`의 `num1`번째 인덱스부터 `num2`번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성해보세요.

**풀이** : 반복문으로 `num1`부터 `num2 + 1`까지 요소들을 answer 배열에 추가함.

``` python
def solution(numbers, num1, num2):
    answer = []
    for i in range(num1, num2 + 1):
        answer.append(numbers[i])
    return answer
```

## 순서쌍의 개수
순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다. 자연수 `n`이 매개변수로 주어질 때 두 숫자의 곱이 `n`인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.

**풀이** : 자기 자신을 제외하면 n의 가장 큰 약수는 아무리 커도 n // 2를 넘을 수 없어서, n // 2 + 1까지 반복시킴.
아까 제외시킨 자기 자신을 마지막에 더함.


```python
def solution(n):
    answer = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            answer += 1
    return answer + 1
```

## 점의 위치 구하기
- x 좌표와 y 좌표가 모두 양수이면 제1사분면에 속합니다.
- x 좌표가 음수, y 좌표가 양수이면 제2사분면에 속합니다.
- x 좌표와 y 좌표가 모두 음수이면 제3사분면에 속합니다.
- x 좌표가 양수, y 좌표가 음수이면 제4사분면에 속합니다.

**풀이** : dot[0]이 x좌표, dot[1]이 y좌표라고 명시되어 있어서, 조건문으로 0보다 큰지, 작은지를 판별함.

```python
def solution(dot):
    answer = 0
    if dot[0] > 0 and dot[1] > 0:
        answer = 1
    elif dot[0] < 0 and dot[1] > 0:
        answer = 2
    elif dot[0] < 0 and dot[1] < 0:
        answer = 3
    else:
        answer = 4
    return answer
```

## 최대값 만들기 (1)
정수 배열 `numbers`가 매개변수로 주어집니다. `numbers`의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

**풀이** : 배열을 정렬한 뒤, 마지막 인덱스와, 마지막 전 인덱스를 곱함.

```python
def solution(numbers):
    answer = 0
    sorted_numbers = sorted(numbers)
    answer = sorted_numbers[-1] * sorted_numbers[-2]
    return answer
```

## 모음 제거
영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 문자열 `my_string`이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

**풀이** : 모음 배열을 만들어, 반복문을 이용해 i번째 인덱스가 모음에 들어있지 않으면 answer 배열에 추가함.

```python
def solution(my_string):
    answer = ''
    moeum = ['a', 'e', 'i', 'o', 'u']
    for i in my_string:
        if i not in moeum:
            answer += i
    return answer
```

## 숨어있는 숫자의 덧셈 (1)
문자열 `my_string`이 매개변수로 주어집니다. `my_string`안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요. 

**풀이** : 문자가 숫자인지 판별하는 함수인 .isdigit()을 이용하여, 숫자라면 answer에 더해감.

```python
def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():
            answer += int(i)
    return answer
```

## 배열 요소의 길이
문자열 배열 `strlist`가 매개변수로 주어집니다. `strlist` 각 원소의 길이를 담은 배열을 return하도록 solution 함수를 완성해주세요.

**풀이** : strlist의 길이를 answer 배열에 추가함.

```python
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer
```

## 삼각형의 완성조건 (1)
선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

- 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
삼각형의 세 변의 길이가 담긴 배열 `sides`이 매개변수로 주어집니다. 세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return하도록 solution 함수를 완성해주세요.

**풀이** : 가장 큰 변이 나머지 두 변의 합보다 작아지만 삼각형이 되므로, 정렬 한 후 조건문으로 판별함

```python
def solution(sides):
    answer = 0
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        answer = 1
    else:
        answer = 2
    return answer
```

## 대문자와 소문자
문자열 `my_string`이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.

**풀이** : .upper(), .lower()를 활용하여 대문자는 소문자로, 소문자는 대문자로 변경함.

```python
def solution(my_string):
    answer = ''
    for i in my_string:
        if i.upper() == i:
            answer += i.lower()
        else:
            answer += i.upper()
    return answer
```

## 약수 구하기
정수 `n`이 매개변수로 주어질 때, `n`의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

**풀이** : n을 1부터 n+1까지 나머지가 0인것들을 answer에 추가함. 낮은 숫자부터 점점 올라가기 때문에 알아서 오름차순으로 됨.

```python
def solution(n):
    answer = []
    for i in range(1, n + 1):
        if n % i == 0:
            answer.append(i)
    return answer
```