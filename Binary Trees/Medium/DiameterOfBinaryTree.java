import java.util.*;

public class DiameterOfBinaryTree {
    public static void main(String[] args) {
        TreeNode r = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        System.out.println(new DiameterOfBinaryTree().diameterOfBinaryTree(r));

    }

    private int maxDiameter;
    public int diameterOfBinaryTree(TreeNode root) {
        maxDiameter = 0;
        height(root);
        return maxDiameter;
    }

    private int height(TreeNode root) {

        if(root==null) {
            return 0;
        }

        int leftHeight = height(root.left);
        int rightHeight = height(root.right);

        maxDiameter = Math.max(maxDiameter, leftHeight+rightHeight);
        return 1 + Math.max(leftHeight, rightHeight);
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