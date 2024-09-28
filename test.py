class TreeNode:
    def __init__(self, index, links):
        self.index = index
        # links[index][0]이 -1이 아닌 경우 왼쪽 자식 노드 생성
        self.left = None if links[index][0] == -1 else TreeNode(links[index][0], links)
        # links[index][1]이 -1이 아닌 경우 오른쪽 자식 노드 생성
        self.right = None if links[index][1] == -1 else TreeNode(links[index][1], links)


selected = [1,3,6]

def dfs_pre_order(node):
    temp =[]
    if node is not None and node.index in selected : 
        temp = []
        return 0
    elif node is not None :
        temp.append(node.index)
        
        dfs_pre_order(node.left)  # 왼쪽 서브트리 탐색
        dfs_pre_order(node.right)  # 오른쪽 서브트리 탐색
        return temp

        
# links 데이터
links = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]
# index = [   0          1         2         3        4       5       6      7        8        9        10       11]
# index = [   0          1         #         3        #       #       6      7        #        9        #       #]
num = [      12 ,       30 ,     1 ,       8 ,     8 ,      6 ,     20      ,7       ,5      ,10      , 4         ,1]




# 트리 생성
nodes = [TreeNode(i, links) for i in range(len(links))]

# DFS 실행
tmp = []

for node in nodes:
    dfs_pre_order(node.left)
    tmp=tmp + dfs_pre_order(node.right)   

    
unique_tmp = []
[unique_tmp.append(x) for x in tmp if x not in unique_tmp]

print(sorted(unique_tmp))
print(unique_tmp)

    

