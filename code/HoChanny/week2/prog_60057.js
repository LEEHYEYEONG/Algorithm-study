function solution(s) {
    let answer = 0;

    let result = s; // 가장 짧은 문자열이 담길 변수
    let temp = ""; // 비교 대상


    for (let i = 1; i < s.length / 2 + 1; i++) { // 1개부터 (s의 길이)/2 까지 모든 단위로 압축해본다.
        let prev = s.slice(0, i); // 전 단계와 같은지 비교용. 처음 자른 문자열로 시작한다.
        let count = 1;            // 지금까지 1번 연속으로 등장했다.

        for (let j = i; j < s.length; j += i) { // i만큼 잘라가면서
            let now = s.slice(j, j + i);

            if (now === prev) { // 앞 단계와 같은 문자열인 경우
                count++; // 계수 늘려주기
            }
            else { // 다른 문자열인 경우
                if (count >= 2) { // 2 이상의 계수는 문자열에 추가함
                    temp = temp + count;
                }
                temp += prev;
                prev = now; //prev 갱신
                count = 1;
            }
        }

        if (count >= 2) { // 반복문 종료 후 비교군이 없어 남은 부속물을 처리해준다.
            temp = temp + count;
        }
        temp += prev;


        if (temp.length < result.length) { // 짧은 문자열 찾기
            result = temp;
        }
        temp = ""; // 다음 압축을 위해 temp 초기화
    }

    answer = result.length;
    return answer;
}
