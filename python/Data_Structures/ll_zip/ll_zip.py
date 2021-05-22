from Data_Structures.linked_list.linked_list import Node, Linked_list

def zipLists(list1, list2):
    '''
    A function that takes two linked lists and merges them into one
    '''
    first = list1
    second = list2

    current1 = first.head
    current2 = second.head

    length1 =0
    length2 =0

    while(current1):
      length1 += 1
      current1 = current1.next

    while(current2):
      length2 += 1
      current2 = current2.next

    if length1 < length2:
      temp =first
      first = second
      second =temp

    linked_first = first.head
    linked_second = second.head

    while linked_first and linked_second:

      first_next = linked_first.next
      second_next = linked_second.next

      linked_second.next = first_next
      linked_first.next = linked_second

      linked_first = first_next
      linked_second = second_next

      second.head = linked_second

    return f'{first}'


