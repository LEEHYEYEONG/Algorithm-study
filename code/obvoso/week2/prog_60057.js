function stringZip(s, chunkSize) {
  const chunkedStringArr = getChunkedStringArr(s, chunkSize);
  let zippedString = chunkedStringArr[0];
  let zipCount = 1;
  let zipCompletedString = "";

  for (let i = 1; i < chunkedStringArr.length; i++) {
    const chunkedString = chunkedStringArr[i];

    if (zippedString === chunkedString) {
      zipCount += 1;
    } else {
      const zipStr = zipCount === 1 ? "" : String(zipCount);
      zipCompletedString += zipStr + zippedString;
      zippedString = chunkedString;
      zipCount = 1;
    }
  }
  zipCompletedString += (zipCount === 1 ? "" : String(zipCount)) + zippedString;
  return zipCompletedString;
}

function getChunkedStringArr(s, chunkSize) {
  let chunkedString = "";
  const chunkedStringArr = [];

  for (const str of s) {
    chunkedString += str;

    if (chunkedString.length === chunkSize) {
      chunkedStringArr.push(chunkedString);
      chunkedString = "";
    }
  }

  if (chunkedString) {
    chunkedStringArr.push(chunkedString);
  }

  return chunkedStringArr;
}

function solution(s) {
  const sArray = s.split("");
  let result = Number.MAX_SAFE_INTEGER;

  if (sArray.length === 1) return 1;

  for (
    let chunkSize = 1;
    chunkSize <= Math.floor(sArray.length / 2);
    chunkSize++
  ) {
    const zippedString = stringZip(sArray, chunkSize);
    result = Math.min(result, zippedString.length);
  }
  return result;
}
