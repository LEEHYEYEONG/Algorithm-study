let orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"];
let course = [2, 3, 4];
let answer = [];

const getCombination = (arr, n) => {
    let result = [];
    if (n == 1) {
        return arr.map((e) => [e]);
    }

    arr.forEach((fixed, index, origin) => {
        let remain = origin.slice(index + 1);
        let fromRemain = getCombination(remain, n - 1);
        let combination = fromRemain.map((value) => [fixed, ...value].sort().join(""));
        result.push(...combination);
    })

    return result;
}
course.forEach((len) => {
    let combinations = {};
    let max = 0;

    orders.forEach((e) => {
        let parsedMenu = e.split("")
        getCombination(parsedMenu, len).forEach((value) => {
            if(!combinations[value]){
                combinations[value] = 1;
            }
            else{
                combinations[value] += 1;
            }
        });
    });
    console.log(combinations);
    for (let c in combinations){
        if(combinations[c] > max){
            max = combinations[c];
        }
    }
    if(max >= 2){
        for (let c in combinations){
            if(combinations[c] == max){
                answer.push(c)
            }
        }
    }
    answer.sort();
    console.log(answer);
})

