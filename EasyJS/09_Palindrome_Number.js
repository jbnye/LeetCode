/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  // const s = x.toString();
  // const reverse_s = s.split('').reverse().join('');
  // return true ? reverse_s == s : false
  let num = x;
  let reverse = 0;
  while (num > 0) {
    let digit = num % 10;
    reverse = reverse * 10 + digit;
    num = Math.floor(num / 10);
  }
  return reverse == x;
};
