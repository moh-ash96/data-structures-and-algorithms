def reverseArray (my_list):
    length = len(my_list)
    for int in my_list:
      my_list.insert(length, my_list[0])
      my_list.pop(0)
      length-=1
    return my_list
