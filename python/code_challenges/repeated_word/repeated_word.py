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
if __name__ == '__main__':
  print(repeated_word("Once upon a time, there was a brave princess who..."))
  print(repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."))
  print(repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))
  print(repeated_word("Once upon a time, there was no brave princess who..."))
