class LNode:
    def __init__(self,x):
        self.data = x
        self.next = None

def CreateLink(x):
    i = 1
    head = LNode(None)
    tmp = None
    cur = head
    while i<=x:
        tmp = LNode(i)
        cur.next = tmp
        cur = tmp
        i += 1
    return head



def RecursiveReverse(head):
    '''无头节点'''
    if head is None or head.next is None:
        return head
    else:
        newhead = RecursiveReverse(head.next)
        head.next.next = head
        head.next = None
    return newhead


def Reverse(head):
    '''有头节点'''
    if head.next is None:
        return head

    firstNode = head.next
    newhead = RecursiveReverse(firstNode)
    head.next = newhead
    return head

if __name__ == '__main__':
    head = CreateLink(8)
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next
    print('-------')
    head = Reverse(head)
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next
