function solution(files) {
    files.sort((a, b) => compare(a, b));
    return files;
}

const compare = (a, b) => { // sort 의 기준이 될 함수
    const reg = /(\D*)(\d{1,5})/i; // 숫자가 아닌 무리(head), 그 뒤에 붙는 1~5개의 숫자(number)를 검사하는 정규표현식
    const regA = a.match(reg); // 1번 인덱스에 head, 2번 인덱스에 number가 들어간다.
    const regB = b.match(reg);
    
    //head 비교
    const compareHead = regA[1].toUpperCase().localeCompare(regB[1].toUpperCase()); // head의 대소문자를 신경쓰지 않으므로 다 대문자로 바꿔서 비교한다. -1이면 a가 앞순위, 1이면 뒤, 0이면 같음
    if(compareHead !== 0){ // head가 다르면 number 비교 불필요
        return compareHead;
    }
    // head가 같을 때 number 비교
    const compareNumber = +regA[2] - +regB[2];
    return compareNumber;
}