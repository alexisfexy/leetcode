
# Definition for singly-linked list.
from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class AddTwoNumbers(object):
    """
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    EXAMPLE:
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.
    """
    def string_manipulation_soln(self, l1: ListNode, l2: ListNode):
        string_one = ""
        string_two = ""
        while l1:
            string_one += str(l1.val)
            l1 = l1.next
        while l2:
            string_two += str(l2.val)
            l2 = l2.next
        one = int(string_one[::-1])
        two = int(string_two[::-1])
        sum_int = one + two

        string_sum = str(sum_int)[::-1]
        current_node = ListNode(val=int(string_sum[0]), next=None)
        final = current_node
        for index, num in enumerate(string_sum):
            if index == len(string_sum) - 1:
                current_node.next = None
            else:
                next_node = ListNode(val=int(string_sum[index + 1]), next=None)
                current_node.next = next_node
                current_node = next_node
        return final

    def carry_over_soln(self, l1: ListNode, l2: ListNode):
        carry = 0
        current_node = ListNode(val=0, next=None)
        final = current_node
        while l1 or l2 or carry:
            node_sum = carry
            if l1:
                node_sum += l1.val
                l1 = l1.next
            if l2:
                node_sum += l2.val
                l2 = l2.next
            if node_sum >= 10:
                node_sum = node_sum % 10
                carry = 1
            else:
                carry = 0
            current_node.val = node_sum
            if l1 or l2 or carry:
                next_node = ListNode()
                current_node.next = next_node
                current_node = next_node
        return final

    def carry_over_soln_prev_node(self, l1: ListNode, l2: ListNode):
        carry = 0
        previous_node = ListNode(val=0, next=None)
        final = previous_node
        while l1 or l2 or carry:
            node_sum = carry
            if l1:
                node_sum+= l1.val
                l1 = l1.next
            if l2:
                node_sum += l2.val
                l2 = l2.next
            if node_sum >= 10:
                node_sum = node_sum % 10
                carry = 1
            else:
                carry = 0
            current_node = ListNode(val=node_sum)
            previous_node.next = current_node
            previous_node = current_node
        return final.next
