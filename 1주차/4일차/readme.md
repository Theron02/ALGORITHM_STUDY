# 4일차 문제 풀이

## 편지
머쓱이는 할머니께 생신 축하 편지를 쓰려고 합니다. 할머니가 보시기 편하도록 글자 한 자 한 자를 가로 2cm 크기로 적으려고 하며, 편지를 가로로만 적을 때, 축하 문구 `message`를 적기 위해 필요한 편지지의 최소 가로길이를 return 하도록 solution 함수를 완성해주세요.

**풀이** : 메세지 수 만큼 answer에 더한 후, 2를 곱하여 리턴함.

```python
def solution(message):
    answer = 0
    for i in message:
        answer += 1
    return answer * 2
```

## 가장 큰 수 찾기
정수 배열 `array`가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

**풀이** : max값과, 그 값의 인덱스를 변수에 저장해, 반복문 이후 answer에 추가함.

```python
def solution(array):
    answer = []
    max = 0
    max_index = 0
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
            max_index = i
    answer.append(max)
    answer.append(max_index)
    return answer
```

## 배열의 유사도
두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 `s1`과 `s2`가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

**풀이** : 이중 반복문으로 배열 두개를 돌아 같은 요소를 찾음.

```python
def solution(s1, s2):
    answer = 0
    for i in s1:
        for j in s2:
            if i == j:
                answer += 1
    return answer
```

## n의 배수 고르기
정수 `n`과 정수 배열 `numlist`가 매개변수로 주어질 때, `numlist`에서 `n`의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.

**풀이** : 반복문을 이용하여 i번째 요소가 n으로 나누어 떨어지면 answer에 추가함.

```python
def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    return answer
```

## 자릿수 더하기
정수 `n`이 매개변수로 주어질 때 `n`의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요

**풀이** : n을 리스트로 변환 후, 반복문을 이용해 더함.

```python
def solution(n):
    answer = 0
    numlist = list(map(int, str(n)))
    for i in numlist:
        answer += i
    return answer
```

## 문자열안에 문자열
문자열 `str1`, `str2`가 매개변수로 주어집니다. `str1` 안에 `str2`가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.

**풀이** : str2기 str1에 있으면 1, 없으면 2를 반환

```python
def solution(str1, str2):
    answer = 0
    if str2 in str1:
        answer = 1
    else : 
        answer = 2
    return answer
```

## 제곱수 판별하기
어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 정수 `n`이 매개변수로 주어질 때, `n`이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.

**풀이** : 제곱근 연산자 (** 0.5)를 사용함.

```python
def solution(n):
    if (n ** 0.5) % 1 == 0:
        return 1
    else:
        return 2
```

## 세균 증식
어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 처음 세균의 마리수 `n`과 경과한 시간 `t`가 매개변수로 주어질 때 `t`시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.

**풀이** : 초기값을 n으로 주고, 시간당 n을 두배씩 하여 answer에 더함.

```python
def solution(n, t):
    answer = n
    for i in range(t):
        answer += n
        n *= 2
    return answer
```

## 머쓱이보다 키 큰 사람
머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다. 머쓱이네 반 친구들의 키가 담긴 정수 배열 `array`와 머쓱이의 키 `height`가 매개변수로 주어질 때, 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.

**풀이** : array의 요소가 height보다 크면 answer에 1 추가함.

```python
def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer
```

## 옷가게 할인 받기
머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
구매한 옷의 가격 `price`가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.

**풀이** : 조건문을 이용해, 해당 조건에 맞으면 세일이 들어가도록 곱함.

```python
def solution(price):
    answer = 0
    if price >= 500000:
        answer = int(price * 0.8)
    elif price >= 300000:
        answer = int(price * 0.9)
    elif price >= 100000:
        answer = int(price * 0.95)
    else: 
        answer = int(price)

    return answer
```