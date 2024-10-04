public class BalancedBinaryTree {
    public static void main(String... args) {
        
    }

    private boolean isBalanced;
    public boolean isBalanced(TreeNode root) {
        isBalanced = true;
        getHeight(root);
        return isBalanced;
    }

    private int getHeight(TreeNode root) {
        if(root==null) {
            return 0;
        }

        int leftHeight = getHeight(root.left);
        int rightHeight = getHeight(root.right);

        if(Math.abs(rightHeight-leftHeight)>1) {
            isBalanced = false;
        }

        return Math.max(leftHeight, rightHeight)+1;
    }

}


class TreeNode {
         int val;
         TreeNode left;
         TreeNode right;
         TreeNode() {}
         TreeNode(int val) { this.val = val; }
         TreeNode(int val, TreeNode left, TreeNode right) {
             this.val = val;
             this.left = left;
             this.right = right;
        }
}