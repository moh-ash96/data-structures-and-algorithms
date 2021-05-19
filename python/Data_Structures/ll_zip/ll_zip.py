from Data_Structures.linked_list.linked_list import Node, Linked_list

def zipLists(list1, list2):
  new_list = Linked_list()
  current1 = list1.head
  current2 = list2.head
  while current1.next and current2.next:
    current1_next = current1.next
    current2_next = current2.next

    current2.next = current1_next
    current1.next = current2_next

    current2 = current2_next
    current1 = current1_next
    new_list.insert(current2.value)
    new_list.insert(current1.value)

  return new_list


