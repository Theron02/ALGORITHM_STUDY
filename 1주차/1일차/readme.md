# 1일차 문제 풀이

## 두 수의 합 구하기
정수 `num1`과 `num2`가 주어질 때, `num1`과 `num2`의 합을 return하도록 soltuion 함수를 완성해주세요.

**풀이** : num1 + num2를 리턴함.

```python
def solution(num1, num2):
    return num1 + num2
```

## 두 수의 차 구하기
정수 `num1`과 `num2`가 주어질 때, `num1`에서 `num2`를 뺀 값을 return하도록 soltuion 함수를 완성해주세요.

**풀이** : num1 - num2를 리턴함.

```python
def solution(num1, num2):
    return num1 - num2
```

## 두 수의 곱 구하기
정수 `num1`, `num2`가 매개변수 주어집니다. `num1`과 `num2`를 곱한 값을 return 하도록 solution 함수를 완성해주세요.

**풀이** : num1 * num2를 리턴함.

```python
def solution(num1, num2):
    return num1 * num2
```

## 몫 구하기
정수 `num1`, `num2`가 매개변수로 주어질 때, `num1`을 `num2`로 나눈 몫을 return 하도록 solution 함수를 완성해주세요.

**풀이** : num1 // num2를 리턴함.

```python
def solution(num1, num2):
    return num1 // num2
```

## 두 수의 나눗셈
정수 `num1`과 `num2`가 매개변수로 주어질 때, `num1`을 `num2`로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 solution 함수를 완성해주세요.

**풀이** : int(num1/num2 * 1000)를 리턴함

```python
def solution(num1, num2):
    return int(num1/num2 * 1000)
```

## 숫자 비교하기
정수 `num1`과 `num2`가 매개변수로 주어집니다. 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요.

**풀이** : 조건문으로 같으면 1, 다르면 -1을 반환함.

```python
def solution(num1, num2):
    answer = 0
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer
```

## 나머지 구하기
정수 `num1`, `num2`가 매개변수로 주어질 때, `num1`를 `num2`로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.

**풀이** : num1 % num2를 리턴함

```python
def solution(num1, num2):
    return num1 % num2
```

## 피자 나눠 먹기 (1)
머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 `n`이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.

**풀이** : math 라이브러리의 올림 함수인 ceil함수 사용.

```python
import math

def solution(n):
    answer = math.ceil(n / 7)
    return answer
```

## 피자 나눠 먹기 (3)
머쓱이네 피자가게는 피자를 두 조각에서 열 조각까지 원하는 조각 수로 잘라줍니다. 피자 조각 수 `slice`와 피자를 먹는 사람의 수 `n`이 매개변수로 주어질 때, `n`명의 사람이 최소 한 조각 이상 피자를 먹으려면 최소 몇 판의 피자를 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.

**풀이** : math 라이브러리의 올림 함수인 ceil을 이용하여, n/slice를 올림.

```python
import math
def solution(slice, n):
    answer = 0
    answer = math.ceil(n / slice)
    return answer
```

## 나이 출력
머쓱이는 선생님이 몇 년도에 태어났는지 궁금해졌습니다. 2022년 기준 선생님의 나이 `age`가 주어질 때, 선생님의 출생 연도를 return 하는 solution 함수를 완성해주세요

**풀이** : 2022 - age + 1을 리턴함.

```python
def solution(age):
    return 2022 - age + 1
```