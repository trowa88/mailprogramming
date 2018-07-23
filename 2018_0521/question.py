"""
링크드 리스트(linked list)의 머리 노드(head node)와 정수 N이 주어지면, 끝에서 N번째 노드(node)를 제거하고 머리 노드(head node)를 리턴하시오.
단, 리스트를 한번만 돌면서 풀어야합니다. N은 리스트 길이보다 크지 않습니다.

예제)
Input: 1->2->3->4->5, N=2
Output: 1->2->3->5

Input: 1->2->3, N=3
Output: 2->3

Input: 1, N=1
﻿Output: null
"""


class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self.head = None
        self.cur = None

    def __len__(self):
        tmp = self.head
        _len = 0
        while tmp:
            _len += 1
            tmp = tmp.next
        return _len

    def __str__(self):
        tmp = self.head
        txt = ''
        while tmp:
            txt += f'{tmp.value}'
            if tmp.next:
                txt += '->'
            tmp = tmp.next
        return txt or 'null'

    def add(self, node):
        if self.head is None:
            self.head = node
            self.cur = self.head
        else:
            self.cur.next = node
            self.cur = node

    def remove(self, _n):
        """
        n 번째 노드 제거
        :param _n:
        :return: Linked list
        """
        index = self.__len__() - _n
        i = 0
        prev = self.head
        tmp = self.head
        while i <= index - 1:
            prev = tmp
            tmp = tmp.next
            i += 1
        if prev == tmp:
            self.head = prev.next
            self.cur = self.head
        else:
            prev.next = tmp.next
            self.cur = tmp.next

        print(self)


def make_node(input_str):
    """
    :param input_str: -> split 가능한 문자열
    :return: LinkedList
    """
    linked_list = LinkedList()
    node_list = [Node(n) for n in input_str.split("->")]
    for node in node_list:
        linked_list.add(node)

    print(len(linked_list))
    return linked_list


def remove_node(_linked_list, _n):
    pass


make_node("1->2->3->4->5").remove(2)
make_node("1->2->3").remove(3)
make_node("1").remove(1)
