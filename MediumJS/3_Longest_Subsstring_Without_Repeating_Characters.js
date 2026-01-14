var lengthOfLongestSubstring = function (s) {
  if (!s.length) return 0;
  if (s.length == 1) return 1;
  let left = 0;
  let right = 0;
  let ans = 0;
  let set = new Set();
  while (right < s.length) {
    while (set.has(s[right])) {
      set.delete(s[left]);
      left++;
    }
    set.add(s[right]);
    right++;
    ans = Math.max(ans, right - left);
  }
  return ans;
};

console.log(lengthOfLongestSubstring("abcabcbb"));
