import sys
sys.setrecursionlimit(10**6)

# 전위순회
def preorder(arrY, answer):
    node = arrY[0] # 루트 노드
    left, right = [], [] # 왼쪽 트리, 오른쪽 트리
    
    for i in range(1, len(arrY)):
        if node[0] > arrY[i][0]:
            left.append(arrY[i])
        else:
            right.append(arrY[i])
    
    answer.append(node[2])
    
    if len(left) > 0:
        preorder(left, answer)
    if len(right) > 0:
        preorder(right, answer)
    return

# 후위순회
def postorder(arrY, answer):
    node = arrY[0] # 루트 노드
    left, right = [], [] # 왼쪽 트리, 오른쪽 트리
    
    for i in range(1, len(arrY)):
        if node[0] > arrY[i][0]:
            left.append(arrY[i])
        else:
            right.append(arrY[i])
    
    if len(left) > 0:
        postorder(left, answer)
    if len(right) > 0:
        postorder(right, answer)
        
    answer.append(node[2])
    return

def solution(nodeinfo):
    preanswer, postanswer = [], []
    
    # 노드 번호 저장
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    
    # y좌표 내림차순 -> x좌표 오름차순으로 정렬
    arrY = sorted(nodeinfo, key = lambda x : (-x[1], x[0]))
    
    preorder(arrY, preanswer)
    postorder(arrY, postanswer)
    
    return [preanswer, postanswer]