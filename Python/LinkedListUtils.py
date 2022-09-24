# This library contains the basic linked list operations
# Note that the implementations may be different than listed
# because the linked list class may be used differently

# TODO put into one class here, and make one general linked list implementation
# to be used for all methods

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#

# add a new head/root to a linked list and return the root/head
def insertNodeAtHead(head, data):
    node = SinglyLinkedListNode(data)
    node.next = head
    head = node

    return head

# this must be set to a value greater than the size of the linked list
# so that there is not a stack overflow error
sys.setrecursionlimit(5000)

# add a new tail to a linked list and return the root/head
def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    if(not head):
        head = node
    elif(not head.next):
        head.next = node
    else:
        insertNodeAtTail(head.next, data)
    return head

# add a new node to a specific position in a linked list and return the root/head
def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data)
    if(position==0):
        node.next = head
        return node

    count = 0
    current = head
    while(count<position-1):
        current=current.next
        count+=1

    node.next = current.next
    current.next = node

    return head

# get node at index location (head index = 0)
def getNode(head, index):
    curr_index = 0
    curr_node = head
    while(curr_index < index):
        curr_node = curr_node.next
        index += 1

    return curr_node

# compare two linked lists to determine if they are equal (not necessarily the same object)
# like deep equals, check each element
def equals(llist1, llist2):
    current_1 = llist1
    current_2 = llist2
    if(current_1==current_2==None):
        return True

    while(current_1 or current_2):
        if(current_1==None or current_2==None):
            return False
        if(current_1.data!=current_2.data):
            return False
        current_1 = current_1.next
        current_2 = current_2.next

    return True

# reverse a linked list iteratively - O(n) time and O(n) space
def reverseIterative(head):
    if(not head):
        return

    current = head

    store_stack = [current]
    while(current):
        current = current.next
        store_stack.append(current)

    store_stack.pop()
    new_current = store_stack.pop()
    head = new_current
    while(store_stack):
        new_current.next = store_stack.pop()
        new_current = new_current.next

    new_current.next = None

    return head

# reverse a linked list iteratively - O(n) time and O(1) space
def reverseRecursive(curr_node, parent=None):
    # case where the curr_node is the end of the initial linked list
    if(curr_node.next == None):
        curr_node.next = parent
        return curr_node

    next_node = curr_node.next
    curr_node.next = parent
    return reverseList(next_node, curr_node)


# merge two sorted lists
def mergeLists(head1, head2):
    def compare_Nodes(a, b):
        if(a.data<b.data):
            new_list=a
            a = a.next
        else:
            new_list= b
            b = b.next
        return a, b, new_list

    first = head1
    second = head2
    if(first==None):
        return second
    if(second==None):
        return first

    new_list = None
    setHead = True

    while(first and second):
        if(setHead==True):
            first, second, new_list = compare_Nodes(first, second)
            head = new_list
            setHead = False
        else:
            first, second, new_list.next = compare_Nodes(first, second)
            new_list = new_list.next


    if(first and not second):
        while(first):
            new_list.next = first
            first = first.next
            new_list = new_list.next
    elif(second and not first):
        while(second):
            new_list.next = second
            second = second.next
            new_list = new_list.next

    return head
