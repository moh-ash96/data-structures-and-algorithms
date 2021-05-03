def insertShiftArray(arr, int):
  i=0
  for n in arr:
    i+=1
  if i>1:
      new_arr = arr[:i//2] + [int] + arr[i//2:]
  else:
     new_arr = arr + [int]
  return new_arr


