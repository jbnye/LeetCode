var removeDuplicates = function (nums) {
  let l = 1;
  for (let r = 1; r < nums.length; r++) {
    if (nums[l - 1] == nums[r]) {
    } else {
      nums[l] = nums[r];
      l++;
    }
  }
  return l;
};
