var isPalindrome = function (s) {
  const arr = s.toLowerCase().split("");

  const filtered = arr.filter((ch) => {
    const code = ch.charCodeAt(0);
    if (code >= 48 && code <= 57) return true;
    if (code >= 97 && code <= 122) return true;

    return false;
  });

  let l = 0;
  let r = filtered.length - 1;

  while (l < r) {
    if (filtered[l] !== filtered[r]) return false;
    l++;
    r--;
  }

  return true;
};
