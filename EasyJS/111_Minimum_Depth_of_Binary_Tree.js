var minDepth = function (root) {
  if (!root) return 0;

  if (!root.left && !root.right) return 1;

  if (!root.left) return 1 + minDepth(root.right);
  if (!root.right) return 1 + minDepth(root.left);

  return 1 + Math.min(minDepth(root.left), minDepth(root.right));

  // let queue = [[root, 1]];
  // while(queue.length){
  //     let [node, depth] = queue.shift();
  //     if(node.left == null && node.right == null){
  //         return depth;
  //     }else{
  //         if(node.left) {queue.push([node.left,depth + 1]);}
  //         if(node.right){ queue.push([node.right, depth +1 ]);}
  //     }
  // }
};
