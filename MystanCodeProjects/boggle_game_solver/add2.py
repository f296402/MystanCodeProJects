"""
File: add2.py
Name:
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    #                     #
    #        TODO:        #
    #                     #
    #######################
    dec = 0  # 進位值
    cur1 = l1  # 用cur裝l1的head
    cur2 = l2  # 用cur裝l2的head
    l3 = ListNode(0, None)  # 創一個Linked List來裝解答
    cur3 = l3  # 不能用head跑 不然l3會不見！（所以才要用cur)
    while cur1 is not None or cur2 is not None or dec != 0:  # 檢查cur1和cur2是不是None，還有是否要進位（要進位代表cur3要更新值）
        answer_val = 0  # 用來裝cur1/cur2/dec的總和
        if cur1 is not None:  # 如果cur1不是None，我才把cur1加到answer_val，然後走到next
            answer_val += cur1.val
            cur1 = cur1.next
        if cur2 is not None:  # 如果cur2不是None，我才把cur2加到answer_val，然後走到next
            answer_val += cur2.val
            cur2 = cur2.next
        answer_val += dec  # answer_val加上層cur%後的十進位
        dec = 0  # 十進位更新成0
        if answer_val >= 10:
            dec = answer_val // 10  # cur1/cur2/dec的總和取十進位數值
            answer_val = answer_val % 10  # cur1/cur2/dec的總和取餘數
        cur3.val = answer_val  # 更新cur3 date的值
        if cur1 is not None or cur2 is not None or dec != 0:  # dec!=0表示要進位,所以cur3還是要走到下一個
            cur3.next = ListNode(0, None)  # 創cur3下一個ListNode（date = 0)
            cur3 = cur3.next  # cur3走到下一個
    return l3
####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
