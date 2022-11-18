class node:
    def __init__(self, data):
        self.data = data
        self.pre = None
        self.next = None

class linkedlist :
    def __init__(self):
        self.head = None


def delete_node(ll, data):
    tmp = ll
    if tmp.head.data == "":
        print("Binary is empty.")
    else:
        tmp = tmp.head
        while tmp.next is not None or tmp.pre is not None:
            if data > tmp.data and tmp.next is not None:
                if data == tmp.next.data and tmp.next.next is None and tmp.next.pre is None:
                    tmp.next = None
                else:
                    tmp = tmp.next
            elif data < tmp.data and tmp.pre is not None:
                if data == tmp.pre.data and tmp.pre.next is None and tmp.pre.pre is None:
                    tmp.pre = None
                else:
                    tmp = tmp.pre
            else:
                break
        p = tmp
        if p.next is not None:
            p = p.next
            while p.pre is not None:
                p = p.pre
            tmp.data = p.data
            tmp.next = p.next
            tmp.pre = p.pre
        elif p.pre is not None:
            p = p.pre
            while p.next is not None:
                p = p.next
            tmp.data = p.data
            tmp.next = p.next
            tmp.pre = p.pre
    return tmp


def add(ll, data):
    tmp = ll
    p = node(data)
    if tmp.head.data == "":
        tmp.head = p
    else:
        tmp = tmp.head
        while tmp.next is not None or tmp.pre is not None :
            if data > tmp.data and tmp.next is not None:
                tmp = tmp.next
            elif data < tmp.data and tmp.pre is not None :
                tmp = tmp.pre
            else :
                break
        if data < tmp.data and tmp.pre is None:
            tmp.pre = p
        elif data > tmp.data and tmp.next is None:
            tmp.next = p
    return tmp

def find_height(tmp):
    if tmp is None:
        return 0
    else:
        pre = find_height(tmp.pre)
        nxt = find_height(tmp.next)
        if pre > nxt:
            return pre + 1
        else:
            return nxt + 1

def find_child(tmp):
    if tmp is not None:
        if tmp.next is not None:
            find_child(tmp.next)
            print(tmp.next.data, end=' ')
        if tmp.pre is not None:
            find_child(tmp.pre)
            print(tmp.pre.data, end=' ')

def find_parent(tmp):
    if tmp is not None:
        if tmp.next and tmp.pre is not None:
            print(tmp.data, end=' ')
            find_parent(tmp.pre)
            find_parent(tmp.next)
        if tmp.next is not None and tmp.pre is None:
            print(tmp.data, end=' ')
            find_parent(tmp.next)
        if tmp.pre is not None and tmp.next is None:
            print(tmp.data, end=' ')
            find_parent(tmp.pre)

def find_leaves(tmp):
    if tmp is not None:
        if tmp.next or tmp.pre is not None:
            find_leaves(tmp.pre)
            find_leaves(tmp.next)
        else :
            print(tmp.data, end=' ')

def find_sibling(tmp):
    if tmp is not None:
        if tmp.next and tmp.pre is not None:
            print(f'{tmp.next.data},{tmp.pre.data}', end=' ')
            find_sibling(tmp.pre)
            find_sibling(tmp.next)


def main():
    ll = linkedlist()
    ll.head = node("")
    # exercise 1
    # add(ll, 1)
    # add(ll, 2)
    # add(ll, 3)
    # add(ll, 4)
    # exercise 2.1
    add(ll, 50)
    add(ll, 25)
    add(ll, 75)
    add(ll, 30)
    add(ll, 60)
    add(ll, 40)
    # exercise 2.2
    delete_node(ll, 30)
    delete_node(ll, 75)
    delete_node(ll, 40)
    # exercise 2.3
    print(f'\nFind height :  {find_height(ll.head)}')
    print('Find parent :', end=' ')
    find_parent(ll.head)
    print('\nFind child :', end=' ')
    find_child(ll.head)
    print('\nFind leaves :', end=' ')
    find_leaves(ll.head)
    print('\nFind siblings :', end=' ')
    find_sibling(ll.head)

if __name__ == "__main__":
    main()