def BinarySearch(arr, key):
  mid = 0
  start = 0
  end = 0
  for i in arr:
    end+=1
  if key > arr[end-1]:
    return -1
  else:
    while (start <= end):
        mid = (start + end) // 2
        if key == arr[mid]:
            return mid

        if key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
  return -1
