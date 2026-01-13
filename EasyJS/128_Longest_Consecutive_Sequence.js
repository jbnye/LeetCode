var longestConsecutive = function (nums) {
  let ans = 0;

  if (nums.length == 0) return 0;

  let set = new Set(nums);

  for (const num of set) {
    if (!set.has(num - 1)) {
      let current = 1;

      let n = num;

      while (set.has(n + 1)) {
        n++;

        current++;
      }

      if (ans < current) {
        ans = current;
      }
    }
  }

  return ans;
};
