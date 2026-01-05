var sortedArrayToBST = function (nums) {
  const build = (left, right) => {
    if (left == right) return null;
    let mid = Math.floor((left + right) / 2);
    let node = new TreeNode(nums[mid]);
    node.left = build(left, mid);
    node.right = build(mid + 1, right);
    return node;
  };
  return build(0, nums.length);
};
