class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_pre_order(node):
    if node is not None:
        print(node.value)  # 현재 노드 방문
        dfs_pre_order(node.left)  # 왼쪽 서브트리 탐색
        dfs_pre_order(node.right)  # 오른쪽 서브트리 탐색

# 이진 트리 생성
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# 깊이 우선 탐색 실행
dfs_pre_order(root)

    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
