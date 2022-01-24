class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
def union(llist_1, llist_2):
    # Your Solution Here
    union_dict=dict()
    result_ll=LinkedList()
    if llist_1.size()>0:
        result_ll.append(llist_1.head)
        union_dict[llist_1.head.val]
        temp_node=llist_1.head
        while temp_node.next:
            result_ll.append(temp_node)
            temp_node=temp_node.next
    if llist_2.size()>0:
        temp_node2=llist_2.head
        result_ll.append(temp_node2)
        while temp_node2.next:
            result_ll.append(temp_node2)
            temp_node2=temp_node2.next
    return result_ll

def intersection(llist_1, llist_2):
    # Your Solution Here
    #using a dictionary
    first_ll_dict = dict()
    intersection_llist=LinkedList()
    if llist_1.size()>0:
        node1 = llist_1.head
        first_ll_dict[node1.value]=True
        while node1.next:
            node1=node1.next
            first_ll_dict[node1.value] = True
        if llist_2.size()>0:
            node2 = llist_2.head
            if node2.value in first_ll_dict.keys():
                intersection_llist.append(node2.value)
            else:
                return []
            while node2.next:
                node2=node2.next
                if node2.value in first_ll_dict.keys():
                    intersection_llist.append(node2.value)
            return intersection_llist
        else:
            return None


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

#print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

#print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))