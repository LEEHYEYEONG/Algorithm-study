# 10814 : 나이순 정렬
## 😎solved code
### 💻code
```python
import sys

n = int(sys.stdin.readline().rstrip())

people = []

for i in range(n):
  age,name = sys.stdin.readline().rstrip().split()
  people.append([int(age),name,i])

#나이순, 나이가 같으면 입장순(i)으로 정렬  
people.sort(key= lambda x : (x[0],x[2]))

for age, name, ticket in people:
  print(age, name)
  ```
## ❗️결과
성공
## 💡접근
1. 입력값에 int와 문자열이 섞여있기 때문에 자료형 구분없이 입력값을 받는다.
2. 이후 리스트에 나이, 이름을 저장해줄 때 나이는 int형으로 구분해주고 입장 순서 (i)를 추가로 append한다.
3. 리스트를 lambda를 이용하여 나이순, 나이가 같다면 입장순(i)로 정렬해주고 순서대로 출력해준다.
## 🧐문제 회고
나이의 자료형을 int로 구분해주지않으면 정렬과정에서 의도와 다르게 순서가 뒤로 밀릴 수 있다.
따라서 자료형 구분을 확실하게 해주는게 중요하다!

# 1234 : ABCD
## 😎solved code
## 🥺unsolved code
### 💻code
```python

  ```
## ❗️결과

## 💡접근

## 🧐문제 회고

# 1234 : ABCD
## 😎solved code
## 🥺unsolved code
### 💻code
```python

  ```
## ❗️결과

## 💡접근

## 🧐문제 회고