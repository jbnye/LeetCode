var convertToTitle = function (columnNumber) {
  let ans = [];
  let temp = columnNumber;

  while (temp > 0) {
    temp--;
    let char = String.fromCharCode((temp % 26) + 65);
    ans.unshift(char);
    temp = Math.floor(temp / 26);
  }

  return ans.join("");
};
