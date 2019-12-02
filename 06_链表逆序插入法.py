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

def Rerserve(head):
    if head is None or head.next is None:
        return
    cur = head.next.next
    head.next.next = None
    while cur is not None:
        next = cur.next
        cur.next = head.next
        head.next = cur
        cur = next
    return head

if __name__ == '__main__':
    head = CreateLink(8)
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next

    head = Rerserve(head)
    cur = head.next
    while cur is not None:
        print(cur.data)
        cur = cur.next