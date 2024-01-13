function cb(arr, i) {
  const ret = [];

  if (i === 1) return arr.map((item) => [item]);

  arr.forEach((item, index, origin) => {
    const remainder = origin.slice(index + 1);
    const combinations = cb(remainder, i - 1);
    const combine = combinations.map((v) => [item, ...v].sort().join(""));
    ret.push(...combine);
  });
  return ret;
}

function solution(orders, course) {
  var answer = [];

  for (let i = 0; i < course.length; i++) {
    const map = {};
    let max = 0;

    orders.forEach((order) => {
      const cbResult = cb(order.split(""), course[i]);
      cbResult.forEach((item) => {
        if (map[item]) map[item]++;
        else map[item] = 1;
        max = Math.max(max, map[item]);
      });
    });
    for (const key in map) {
      if (map[key] === max && max > 1) answer.push(key);
    }
  }
  return answer.sort();
}
