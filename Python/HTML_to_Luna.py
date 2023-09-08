import re
from collections import deque

# used for DOM
class Node():
    def __init__(self, tag, parent=None):
        self.tag = tag
        self.parent = parent
        self.children = []
    
    # this can perform a recursive print (no separate tree print function needed!)
    # must loop over all top-level nodes in order for this to work
    def __str__(self):
        curr_LUNA_tag = self.tag.upper()
        if(len(self.children) == 0):
            if(curr_LUNA_tag == "IMG"):
                return curr_LUNA_tag + "({})"
            else:
                return curr_LUNA_tag + "([])"
                
        else:
            if(curr_LUNA_tag == "IMG"):
                return curr_LUNA_tag + "({" + ", ".join([str(a) for a in self.children]) + "})"
            else:
                return curr_LUNA_tag + "([" + ", ".join([str(a) for a in self.children]) + "])"
            
        
        
# break up HTML code into nodes by stripping off the top level, then the next level, etc.  
# this part has the most work required - figuring out how to strip off multiple nodes on the same level, 
# with different children (separate "trees")
# might have an old regex for this from HR, or use a stack to match tags
# use a stack for now, after tokenizing the tags (go through HTML and keep track of the current node,
# going back up the tree on closing tags and down the tree with new nodes on opening tags)



# make a tree of the tags (need to define a node class with multiple children possible in array)
# then perform a post order tree traversal and combine string results based on tags
# may need multiple trees based on top-level html being one tag or multiple
def solution(html):
    regex = r"<.+?>"
    tokens = re.findall(regex, html)
    token_queue = deque(tokens)
    stack = []
    
    # root nodes for top-level DOM (may have multiple root nodes)
    root_nodes = []
    
    # print(tokens)
    tag_regex = r"[a-zA-Z]+"
    
    for token in tokens:
        token_tag = re.findall(tag_regex, token)[0]
        # perform different actions if opening or closing tag
        if("/" in token and not token_tag == "img"):
            # go up the tree to the parent
            stack.pop() 
            continue  
        else:
            if(len(stack) > 0):
                node = Node(token_tag, parent = stack[-1])
                stack[-1].children.append(node)
            else:
                node = Node(token_tag)
                root_nodes.append(node)
                
            stack.append(node)
            
            if(node.tag == "img"):
                stack.pop()
    
    return "".join([str(a) for a in root_nodes])