"""
顺序表：将一组数据按一片连续的存储空间存放数据的物理地址
单链表：上一个元素的一个属性指向下一个元素的存储空间地址
环形单链表：首尾相连的单链表
双链表：该元素保存上一个节点的地址和下一个节点的地址
环形双链表：首尾相连的双链表
"""


class Node(object):
    def __init__(self,elem):
        self.elem=elem
        self.next=None

class SingleLinkList(object):
    def __init__(self,node=None):
        self.__head=node

    def is_empty(self):
        return self.__head==None

    def length(self):
        if self.is_empty():
            return 0
        else:
            cur=self.__head
            count=0
            while cur!=None:
                count+=1
                cur=cur.next
            return count

    def append(self,item):
        node=Node(item)
        if self.is_empty():
            self.__head=node
        else :
            cur=self.__head
            temp=None
            while cur!=None:
                temp=cur
                cur=cur.next
            cur=node
            temp.next=cur

    def insert(self,i,item):
        node=Node(item)
        if self.is_empty() :
            self.__head=node
        else:
            cur=self.__head
            count=0
            temp=None
            while i!=count and cur!=None:
                temp=cur
                count+=1
                cur=cur.next
            node.next=cur
            temp.next=node

    def delete(self,i):
        cur=self.__head
        count=0
        if i>=self.length():
            return False
        temp=None
        while i!=count:
            temp=cur
            cur=cur.next
            count+=1
        temp.next=cur.next
        return True

    def select(self,i):
        if i>=self.length():
            return False
        else:
            count=0
            cur=self.__head
            while i!=count:
                count+=1
                cur=cur.next
            return cur.elem


    def tralver(self):
        if self.is_empty():
            print("空")
        else:
            cur=self.__head
            while cur!=None:
                print(cur.elem)
                cur=cur.next




if __name__=="__main__":
    sll=SingleLinkList()
    print(sll.is_empty())
    print(sll.length())
    sll.append("1")
    sll.append(3)
    sll.append(5)
    sll.append(7)
    sll.append("9hahaha")
    print(sll.is_empty())
    print(sll.length())
    sll.tralver()
    sll.insert(1,2)
    sll.tralver()
    sll.insert(6,12)
    sll.insert(5,11)
    sll.tralver()
    sll.insert(11, 15)
    sll.tralver()
    sll.delete(1)
    sll.tralver()
    print(sll.select(1))

