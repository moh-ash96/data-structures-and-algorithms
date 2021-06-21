import re
def repeated_word(string):
  li2 = string.split(' ')
  li = []
  for i in li2:
    i = i.replace(',', '')
    li.append(i.lower())
  first_location = 0
  second_location = 0
  saved_word = ''
  for word in li:
    counter = 0
    ind = 0
    for i in li:
      li2.append(i)
    while word in li2:
      if counter == 2:
        break
      ind = li2.index(word)
      if ind is not None:
        counter +=1
        li2.pop(ind)
    li2 = []
    if counter == 2:
      first_location = ind + counter

      if first_location < second_location or second_location ==0:
        second_location = first_location
        saved_word = word

  return saved_word

