N, L = map(int, input().split())
# N = 물 새는 곳의 갯수
# L = 테이프 길이
T = list(map(int, input().split()))
T.sort()
cnt = 1

# print(T)
for i in T[1:]:
    if i in range(T[0], T[0] + L):
        continue
    else:
        T[0] = i
        cnt += 1

print(cnt)

# N과 L은 각각 물 새는곳의 갯수와 테이프의 길이이다.
# T로 N만큼의 숫자를 입력받고 제일 가까운 구멍부터 찾기위해 오름차순으로 정리한다.
# 최종적으로 출력할 cnt변수를 1로 초기화한다. 무조건 한번은 붙여야 하기 때문이다.
# T배열의 1번째 수부터 for문을 돈다. 만약 T의 첫번째 수부터 L(길이)만큼 더한 길이 안에 i(T값)가 존재한다면
# 테이프를 붙일 수 있는 길이이므로 넘어간다.
# 만약 테이프를 붙일 수 없는 길이라면 첫 번째 순서를 바꾸고 cnt를 증가시킨다.
