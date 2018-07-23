"""
안녕하세요, 매일프로그래밍 이번주 문제입니다.
두개의 정렬된(sorted) 정수 링크드리스트(linked list)가 주어지면, 두 리스트를 합친 정렬된 링크드리스트를 만드시오.

예제)
Input: 1->2->3, 1->2->3
Output: 1->1->2->2->3->3

Input: 1->3->5->6, 2->4
﻿Output: 1->2->3->4->5->6
"""


class Node:
    def __init__(self, value):
        self.next = None
        self.value = int(value)


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


def make_node(input_str):
    """
    :param input_str: -> split 가능한 문자열
    :return: LinkedList
    """
    linked_list = LinkedList()
    node_list = [Node(n) for n in input_str.split("->")]
    for node in node_list:
        linked_list.add(node)
    return linked_list


def add_linked_list(_first_linked_list, _second_linked_list):
    result_linked_list = LinkedList()
    first_head = _first_linked_list.head
    second_head = _second_linked_list.head

    while first_head or second_head:
        if first_head and second_head:
            if first_head.value >= second_head.value:
                result_linked_list.add(Node(first_head.value))
                result_linked_list.add(Node(second_head.value))
            else:
                result_linked_list.add(Node(first_head.value))
                result_linked_list.add(Node(second_head.value))
            first_head = first_head.next
            second_head = second_head.next
        elif first_head and not second_head:
            result_linked_list.add(Node(first_head.value))
            first_head = first_head.next
        else:
            result_linked_list.add(Node(second_head.value))
            second_head = second_head.next
    return result_linked_list


print(add_linked_list(make_node('1->2->3'), make_node('1->2->3')))
print(add_linked_list(make_node('1->3->5->6'), make_node('2->4')))
