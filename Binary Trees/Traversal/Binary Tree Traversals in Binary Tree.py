from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    inorder, preorder, postorder = [], [], []
    getPreOrder(root, preorder)
    getInOrder(root, inorder)
    getPostOrder(root, postorder)

    return [inorder, preorder, postorder]
    


def getPreOrder(node: BinaryTreeNode, res: list[int]):
    if node==None:
        return
    
    res.append(node.data)
    getPreOrder(node.left, res)
    getPreOrder(node.right, res)

def getInOrder(node: BinaryTreeNode, res: list[int]):
    if node==None:
        return
    
    getInOrder(node.left, res)
    res.append(node.data)
    getInOrder(node.right, res)

def getPostOrder(node: BinaryTreeNode, res: list[int]):
    if node==None:
        return
    
    getPostOrder(node.left, res)
    getPostOrder(node.right, res)
    res.append(node.data)


if __name__ == "__main__":
    b = BinaryTreeNode(1)
    b.left = BinaryTreeNode(2)
    b.right = BinaryTreeNode(3)
    b.right.right = BinaryTreeNode(6)

    print(getTreeTraversal(b))