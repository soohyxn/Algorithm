import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def postorder(start, end):
    if start > end:
        return

    root = preorder[start]
    idx = start + 1

    while idx <= end:
        if preorder[idx] > root:
            break
        idx += 1

    postorder(start+1, idx-1)
    postorder(idx, end)
    print(root)

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break
postorder(0, len(preorder)-1)