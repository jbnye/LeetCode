var plusOne = function (digits) {
  //   let number = parseInt(digits.join());
  //   number += 1;
  //   return num.toString().split("").map(Number);
  let carry = true;
  for (let i = digits.length - 1; i >= 0; i--) {
    if (carry) {
      if (digits[i] === 9) {
        digits[i] = 0;
      } else {
        digits[i] += 1;
        carry = false;
      }
    } else {
      break;
    }
  }
  if (carry) {
    digits.unshift(1);
  }
  return digits;
};

console.log(plusOne([1, 2, 3]));
