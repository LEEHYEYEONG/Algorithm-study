function solution(places) {
    var answer = [];

    let newPlaces = places.map(row => row.map(e => e.split(''))); // 문자열을 문자의 배열로 분할해주는 과정
    newPlaces.forEach((place) => {
        answer.push(check(place)); // 각 대기실 별로 거리두기를 체크함
    })


    return answer;
}

const check = (place) => {
    dx = [1, 0, -1, 0]; // 상하좌우 이동을 결정할 배열들
    dy = [0, 1, 0, -1];

    for (let i = 0; i < 5; i++) {
        for (let j = 0; j < 5; j++) {
            let now = place[i][j];

            if (now === 'P') { //P의 사방에 다른 P가 있으면 안된다
                for (let k = 0; k < 4; k++) {
                    let nx = i + dx[k];
                    let ny = j + dy[k];
                    if (nx >= 0 && nx < 5 && ny >= 0 && ny < 5 && place[nx][ny] === 'P') {
                        return 0;
                    }
                }
            }
            else if (now === 'O') { // O의 사방에 2개 이상의 P가 있으면 안된다
                let count = 0;
                for (let k = 0; k < 4; k++) {
                    let nx = i + dx[k];
                    let ny = j + dy[k];
                    if (nx >= 0 && nx < 5 && ny >= 0 && ny < 5 && place[nx][ny] === 'P') {
                        count++;
                    }
                }
                if (count >= 2) {
                    return 0;
                }
            }
        }
    }
    return 1;
}
