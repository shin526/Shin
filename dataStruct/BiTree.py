#! /usr/bin/python


class Node:
    __slots__ = ('data', 'left', 'right')

    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


class BiTree:
    __slots__ = ('root')

    def __init__(self, root: Node) -> None:
        self.root = root

    def preorderTraversal(self, root: Node):
        '''先序遍历'''
        '''递归'''
        # if not root:
        #     return []
        # else:
        #     return [root.data] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        '''非递归'''
        stack = [root]
        res = []
        while stack:
            cur = stack.pop()
            if cur:
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
                stack.append(cur)
                stack.append(None)
            else:
                cur = stack.pop()
                res.append(cur.data)
        return res

    def inorderTraversal(self, root: Node):
        '''中序遍历'''
        '''递归'''
        # if not root:
        #     return []
        # else:
        #     return self.inorderTraversal(root.left) + [root.data] + self.inorderTraversal(root.right)
        '''非递归'''
        stack = [root]
        res = []
        while stack:
            cur = stack.pop()
            if cur:
                if cur.right:
                    stack.append(cur.right)
                stack.append(cur)
                stack.append(None)
                if cur.left:
                    stack.append(cur.left)
            else:
                cur = stack.pop()
                res.append(cur.data)
        return res

    def postorderTraversal(self, root: Node):
        '''后序遍历'''
        '''递归'''
        # if not root:
        #     return []
        # else:
        #     return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.data]
        '''非递归'''
        stack = [root]
        res = []
        while stack:
            cur = stack.pop()
            if cur:
                stack.append(cur)
                stack.append(None)
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
            else:
                cur = stack.pop()
                res.append(cur.data)
        return res

    def levelOrder(self, root: Node):
        '''层序遍历'''
        queue = [root]
        res = []
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                cur = queue.pop(0)
                level.append(cur.data)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(level)
        return res


def createBiTree():
    A, B, C, D, E, F, G = [Node(x) for x in 'ABCDEFG']
    D.left = B
    B.left = A
    B.right = C
    C.left = F
    C.right = E
    F.right = G
    return BiTree(D)


def main():
    tree = createBiTree()
    preorder = tree.preorderTraversal(tree.root)
    inoder = tree.inorderTraversal(tree.root)
    postorder = tree.postorderTraversal(tree.root)
    levelOrder = tree.levelOrder(tree.root)
    print(f'先序遍历：{preorder}\n中序遍历：{inoder}\n后序遍历：{postorder}\n层序遍历：{levelOrder}')


if __name__ == '__main__':
    main()
