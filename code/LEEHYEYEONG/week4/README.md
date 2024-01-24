# 백준 10814번

## 접근

이 문제를 보고 나이와 가입 순서를 저장하여 이 두개를 key로 해 출력하도록 만들면 될 것 같았다.

일단은 배열에 나이, 가입한 순서, 이름으로 저장하게 코드를 작성했다.

```python
for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    member.append([int(age), i, name])
```

그리고 sort에 key 값을 기준으로 정렬되도록 작성해주었다.

lambda 식을 이용해 age를 기준으로 오름차순, age가 같다면 i를 기준으로 오름차순 정리하도록 하였다.

`member.sort(key= lambda x:(x[0], x[1]))`

## 참고

key를 기준으로 정렬

[[Python] sort()에서의 key lambda 사용하기](https://kingofbackend.tistory.com/98)
