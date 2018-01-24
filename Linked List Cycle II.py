# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if (head == None):
        return None
    if (head.next == head):
        return True
    if (head.next == None):
        return None
    point1 = head
    point2 = head
    index = 1
    cur = head
    while (not point1 == None and not point2.next == None):
        point1 = point1.next
        point2 = point2.next.next
        cur = cur.next
        # index+=1
        # if(index%2==1):
        #     point1=cur
        # if(index%2==0):
        #     point2=cur
        if (point1 == point2):
            return True
    else:
        return None
h1=ListNode(1)
h1.next=h1
detectCycle(h1)