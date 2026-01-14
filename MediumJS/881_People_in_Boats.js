var numRescueBoats = function (people, limit) {
  let arr = people.sort((a, b) => a - b);
  let ans = 0;
  let left = 0;
  let right = arr.length - 1;
  while (right > left) {
    if (arr[right] + arr[left] <= limit) {
      ans++;
      left++;
      right--;
    } else {
      ans++;
      right--;
    }
  }
  if (right == left) {
    if (arr[left] <= limit) {
      ans++;
    }
  }
  return ans;
};
