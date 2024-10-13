public class SameTree {
    public static void main(String[] args) {
        TreeNode r1 = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        TreeNode r2 = new TreeNode(1, new TreeNode(2), new TreeNode(4));

        System.err.println(new SameTree().isSameTree(r1, r2));
    }

    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p==null) {
            return q==null;
        }

        if(q==null) {
            return p==null;
        }

        return p.val==q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }

}
