""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    return preOrder(root)["result"]

# Note that a dictionary is used here in place of an object (formatted like an
# object literal in JS) - this should probably be rewritten as a custom class

#need to check left subtree values all less than current
#need to check right subtree values all greater than current
#keep track of min, max value of subtrees
def preOrder(node):
    if(not node.left and not node.right):
        return {"result": True, "minimum": node.data, "maximum": node.data}

    if(node.left):
        if(node.left.data >= node.data):
            return {"result": False, "minimum": node.left.data, "maximum": node.left.data}
        left = preOrder(node.left)

    if(node.right):
        if(node.right.data <= node.data):
            return {"result": False, "minimum": node.right.data, "maximum": node.right.data}
        right = preOrder(node.right)

    if(left["result"] and node.data > left["maximum"] and
      right["result"] and node.data < right["minimum"]):
        outcome = {"result":True, "minimum": left["minimum"], "maximum": right["maximum"]}
    else:
        outcome = {"result":False, "minimum": left["minimum"], "maximum": right["maximum"]}

    return outcome
