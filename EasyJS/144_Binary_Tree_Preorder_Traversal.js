var preorderTraversal = function(root) {
    let ans = [];
    const helper = (root) => {
        if(!root)return;
        ans.push(root.val);
        if(root.left){
            helper(root.left);
        }
        if(root.right){
            helper(root.right);
        }
    }
    helper(root);
    return ans;
};