# GDCS 알고리즘 스터디

# 목표

- 기업 코딩테스트에 자주 출제되는 문제 유형을 빠르게 익히고 합격할 역량 기르기

# 진행 기간 및 내용

겨울방학 GDSC 자율 알고리즘 스터디

그리디, 구현, DFS/BFS, 정렬, 이진탐색, DP, 최단경로, 그래프 등 유형 연습 문제(백준)와 유형을 모르는 실전 문제(프로그래머스)를 풉니다.

- 참고 교재
  **_이것이 취업을 위한 코딩 테스트다_** 교재를 활용했습니다. 위에 언급한 유형들은 교재의 목차에 해당합니다.
  [이것이 취업을 위한 코딩 테스트다 with 파이썬 - YES24](http://www.yes24.com/Product/Goods/91433923)

| 주차 | 기간          | 내용                                                    | 총 문제 수 |
| ---- | ------------- | ------------------------------------------------------- | ---------- |
| 1    | 01/01 - 01/07 | 그리디 + 프로그래머스 실전                               | 3          |
| 2    | 01/08 - 01/14 | 구현 + 프로그래머스 실전                                 | 3          |
| 3    | 01/15 - 01/21 | DFS/BFS + 프로그래머스 실전                              | 3          |
| 4    | 01/22 - 01/28 | 정렬 + 프로그래머스 실전                                 | 3          |
| 5    | 01/29 - 02/04 | 이진탐색 + 프로그래머스 실전                             | 3          |
| 6    | 02/05 - 02/11 | DP + 프로그래머스 실전                                   | 3          |
| 7    | 02/12 - 02/18 | 최단경로 + 프로그래머스 실전                             | 3          |
| 8    | 02/19 - 02/25 | 그래프 + 프로그래머스 실전                               | 3          |

# 진행 방식

- 해당 주차 총무가 백준 + 프로그래머스 문제 출제
  - 총무는 매주 돌아가면서 바꿈
- 마감일까지 출제된 3문제 풀기 + README.md 작성 후 깃헙에 PR
  - README.md는 공부한 내용, 문제 풀이, 접근 방법 등 자유롭게 작성하시면 됩니다.
  - 문제를 못 풀었을 경우 접근 방법에 대해 회고하여 적어주세요.
- 코드 리뷰 후 merge
- 총무가 벌금 계산 후 -> 다음 주차 총무가 README.md 업데이트 (문제 출제)

# 보증금

- 어느 정도의 참여도를 부여하기 위해 `(인원 수) * (주차 수) * 300` 원을 1 인당 보증금으로 생각하고 있습니다
  스터디 완주 시 보증금은 반환됩니다
  단, 해당 주차에 **“미션”** 실패 시, 보증금에서 `(인원 수) * 300` 원이 차감됩니다.
  ex) 스터디 인원 7명, 총 8주차 스터디인 경우
  1인당 보증금 : `7 * 8 * 300 = 16,800` 원
  미션 실패한 주 당 `7 * 300 = 2,100` 원 차감
- 스터디 종료 후, 차감으로 인해 남은 보증금 잔액은 `(보증금 잔액) / (인원 수)` 만큼 배분합니다.

# 기타

- 문제풀이를 위한 언어 선택은 자유입니다.
- 코드리뷰의 편의를 위해 Readme에 풀이를 잘 작성해주세요!
- 문제를 못 풀었다면 어디까지 생각하고 접근했는지 Readme에 기록해주세요!
- 커리큘럼과 진행방식은 협의 가능합니다.
  - +) 개인적으로 알고리즘 유형을 알 수 없는 실전 문제만 풀며 감각을 끌어올리는 훈련을 하고 싶어요.
  - +) 보증금을 조금 낮추고/올리고 싶어요
- 출제 **난이도 기준**은 대략 아래와 같습니다.
  - 백준 : Silver 1,2 ~ gold 3,4 (평균 gold 5)
  - 프로그래머스 : Lv 2 ~ 4 (평균 Lv.3) (출처: 카카오 블라인드, 테크 인턴십 등)

# 진행 방식 상세

## 매 주 일정

### 0. 시작

- git clone 후 각자 github 아이디명으로 branch 파기

### 1. 월 ~ 토요일 자정

- 알고리즘 공부
- 출제된 문제 풀기
- README.md 작성
- 내 브랜치에 push
- 내 브랜치 → main으로 pull request

### 2. 일요일

- 사이클에 맞춰 해당 사람 코드 PR 리뷰
- 주차별 해당 사람 = (자신의 번호 + 해당 주차) % 인원수
- 예) 1주차-jonghyeonjo99 : (jonghyeonjo99(0) + 1) % n == 1 => 1번 사람 코드 PR

### 3. 월요일

- 총무가 벌금 계산
- 문제 출제 + README.md 커리큘럼에 업데이트

## 멤버 및 번호

_문제 출제자 및 총무를 위한 멤버 번호 입니다._

조종현(0) → 장광진(1) → 이혜영(2) → 오혁준(3) → 오송민(4) → 이찬호(5) → 주채연(6) → 박지원(7)

## 코드 리뷰 예시

1. 코드의 시간 복잡도
2. 코드의 개선 방안
3. 추천해줄 새로운 함수나 라이브러리
4. 그 외의 코멘트

## 폴더 구조

```
README.md
code
   ㄴ jonghyeonjo99 // 자신의 github 닉네임
     ㄴ week1
       ㄴ boj_1541.py
       ㄴ boj_1461.py
       ㄴ boj_2138.py   // 백준 문제
       ㄴ prog_12345.py // 프로그래머스 문제
       ㄴ README.md     // 1주차 README
```

# 멤버 별 제출 현황

- 총무가 PR 기준으로 월요일마다 업데이트 해주세요!
- ✅ : 미션 성공
- 😥 : 미션 실패 (지각, 미제출, 미흡)

| 멤버                                              | 1주차 | 2주차 | 3주차 | 4주차 | 5주차 | 6주차 | 7주차 | 8주차 |
| ------------------------------------------------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| [jonghyeonjo99](https://github.com/jonghyeonjo99) |  ✅  |  😥  |  ✅  |  ✅  |  ✅  |  😥  |  ✅  |      |
| [HoChanny](https://github.com/HoChanny)           |  ✅  |  ✅  |  ✅  |  ✅  |  😥  |  ✅  |  😥  |      |
| [jjuny-won](https://github.com/jjuny-won)         |  ✅  |  ✅  |  ✅  |  ✅  |  ✅  |  ✅  |  ✅  |      |
| [LEEHYEYEONG](https://github.com/LEEHYEYEONG)     |  ✅  |  ✅  |  ✅  |  ✅  |  ✅  |  ✅  |  😥  |      |
| [obvoso](https://github.com/obvoso)               |  ✅  |  ✅  |  😥  |  😥  |  ✅  |  😥  |  😥  |      |
| [OhHyukJun](https://github.com/OhHyukJun)         |  ✅  |  ✅  |  ✅  |  ✅  |  ✅  |  ✅  |  😥  |      |
| [joochaeyeon](https://github.com/joochaeyeon)     |  ✅  |  ✅  |  ✅  |  ✅  |  ✅  |  ✅  |  ✅  |      |
| [wkdrhkdwls](https://github.com/wkdrhkdwls)       |  ✅  |  😥  |  😥  |  😥  |  😥  |  😥  |  😥  |      |

# 커리큘럼

- 총무가 월요일마다 업데이트 해주세요!

## Week 1

- 총무 : [jonghyeonjo99](https://github.com/jonghyeonjo99)

### 1. 그리디

- 문제정보 : 수리공 항승 (1449)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/1449

- 문제정보 : 강의실 배정 (11000)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/11000

### 2. 실전

- 문제정보 : 메뉴 리뉴얼 (72411)
- 출처 : 프로그래머스
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/72411

## Week 2

-총무 : [wkdrhkdwls](https://github.com/wkdrhkdwls)

### 1. 구현

- 문제정보 : 달팽이 (1913)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/1913

- 문제정보 : 빗물 (14719)
- 출처 : 백준
- 링크 :  https://www.acmicpc.net/problem/14719

### 2. 실전

 - 문제정보 : 문자열 압축 (60057)
 - 출처 : 프로그래머스
 - 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/60057

## Week 3

-총무 : [LEEHYEYEONG](https://github.com/leehyeyeong)

### 1. DFS/BFS

- 문제정보 : DFS와 BFS (1260)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/1260

- 문제정보 : 숨바꼭질2 (12851)
- 출처 : 백준
- 링크 :  https://www.acmicpc.net/problem/12851

### 2. 실전

 - 문제정보 : 거리두기 확인하기 (81302)
 - 출처 : 프로그래머스
 - 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/81302

## Week 4
- 총무 : [OhHyukJun](https://github.com/OhHyukJun)

### 1. 정렬

- 문제정보 : 나이순 정렬 (10814)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/10814

- 문제정보 : 좌표압축 (18870)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/18870

### 2. 실전

 - 문제정보 : 파일명 정렬 (17686)
 - 출처 : 프로그래머스
 - 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/17686

## Week 5
- 총무 : [obvoso](https://github.com/obvoso)

### 1. 이진탐색

- 문제정보 : 예산 (2512)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/2512

- 문제정보 : 공유기 설치 (2110)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/2110

### 2. 실전

 - 문제정보 : 입국 심사 (43238)
 - 출처 : 프로그래머스 
 - 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43238
 - 
 ## week 6
 -총무 [HoChanny](https://github.com/HoChanny)

 ### 1. DP

 - 문제정보 : 평범한 배낭 (12865)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/12865

- 문제정보 : 합분해 (2225)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/2225

### 2. 실전

 - 문제정보 : N으로 표현 (42895)
 - 출처 : 프로그래머스 
 - 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42895

## Week 7
- 총무 : [joochaeyeon](https://github.com/joochaeyeon)

### 1. 최단경로
- 문제정보 : 최단경로 (1753)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/1753

- 문제정보 : 타임머신 (11657)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/11657

### 2. 실전

 - 문제정보 : 배달 (12978)
 - 출처 : 프로그래머스 
 - 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12978

## Week8
- 총무 : [jjuny-won](https://github.com/jjuny-won)

### 1. 그래프
- 문제정보 : 도시 분할 계획 (1647)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/1753

- - 문제정보 : 장난감 조립 (2637)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/1753

### 2. 실전
 - 문제정보 : 도넛과 막대 그래프 (258711)
 - 출처 : 프로그래머스 
 - 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/258711
