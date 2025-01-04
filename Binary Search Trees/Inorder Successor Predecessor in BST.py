from cimports import Node


class Solution:
    def findPreSuc(self, root, pre, suc, key):
        tmp = root
        pre.key = -1
        while tmp != None:
            if tmp.key < key:
                pre.key = tmp.key
                tmp = tmp.right
            else:
                tmp = tmp.left

        tmp = root
        suc.key = -1
        while tmp != None:
            if tmp.key > key:
                suc.key = tmp.key
                tmp = tmp.left
            else:
                tmp = tmp.right

if __name__ == "__main__":
    s = Solution()
    r = Node(8, left=Node(1, right=Node(4, left=Node(3))), right=Node(9, right=Node(10)))
    pre, suc = None, None
    s.findPreSuc(r, pre, suc, 8)
    print(pre, suc)
