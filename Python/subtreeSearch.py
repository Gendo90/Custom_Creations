#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

# use pre-order traversal
# first node, then left, then right
# gives whether or not t2 is a subtree of t1
def isSubtree(t1, t2):
    if(t2 == None):
        return True
    if(t1==None):
        return False
    return preorderTraversal(t1, t2)



def preorderTraversal(root, subtreeRoot, subtreeFound=False):
    if(subtreeFound):
        return True
    print(root.value)

    if(root.value == subtreeRoot.value):
        subtreeFound = checkEquivalentTrees(root, subtreeRoot)
        print(subtreeFound)

    if(subtreeFound): return True
    else:
        left_result = False
        right_result = False
        if(root.left):
            left_result = preorderTraversal(root.left, subtreeRoot)
            if(left_result==True):
                return True
        if(root.right):
            right_result = preorderTraversal(root.right, subtreeRoot)

    return subtreeFound or left_result or right_result

# check the trees in pre-order
def checkEquivalentTrees(node1, node2, equalThusFar=True):
    if(not equalThusFar):
        return False
    if((node1 is None and node2 is not None) or (node2 is None and node1 is not None)):
        return False
    if(node1 is None and node2 is None):
        return True
    if(not (node1.value == node2.value) ):
        equalThusFar = False
        return False


    left_result = checkEquivalentTrees(node1.left, node2.left, equalThusFar)
    if(not left_result):
        return False
    right_result = checkEquivalentTrees(node1.right, node2.right, equalThusFar)
    if(not right_result):
        return False

    if(left_result and right_result):
        return True
