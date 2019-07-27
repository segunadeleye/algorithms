# array[start:stop] = [start,..., stop - 1]

def mergeSort(array):
  n = len(array)
  if n == 1:
    return array

  mid = n // 2
  left = array[0:mid]
  right = array[mid:]

  return merge(mergeSort(left), mergeSort(right), n)

def merge(left, right, n):
  merged = []
  iLeft = 0
  iRight = 0
  leftLength = len(left)
  rightLength = len(right)

  for i in range(n):
    if iLeft >= leftLength:
      '''
      All the items in the left array have been copied over
      '''
      merged.append(right[iRight])
      iRight += 1
    elif iRight >= rightLength:
      '''
      All the items in the right array have been copied over
      '''
      merged.append(left[iLeft])
      iLeft += 1
    elif left[iLeft] <= right[iRight]:
      merged.append(left[iLeft])
      iLeft += 1
    else:
      merged.append(right[iRight])
      iRight += 1
    # print(iLeft, iRight, merged)

  return merged

print(mergeSort([6,5,4,3,2,1]))
print(mergeSort([1,20,6,4,5]))
print(mergeSort([1,2,7,4,5,62,5,2,5,6,2,6,7,7,2,4,7,8,3,2,3,6,78,1,2,31,4,734,73,75,2]))


def countInversions(array):
  n = len(array)
  if n == 1:
    return 0

  mid = n // 2
  left = array[0:mid]
  right = array[mid:]

  sortedLeft, leftInversions = mergeSort(left), countInversions(left)
  sortedRight, rightInversions = mergeSort(right), countInversions(right)
  splitInversions = mergeInversion(sortedLeft, sortedRight, n)

  return leftInversions + rightInversions + splitInversions

def mergeInversion(left, right, n):
  inversions = 0
  mid = n // 2
  iLeft = 0
  iRight = 0
  leftLength = len(left)
  rightLength = len(right)

  for i in range(n):
    if iLeft >= leftLength:
      '''
      All the items in the left array have been copied over
      '''
      inversions += (mid - iLeft)
      # OR => inversions += (len(left[iLeft:]))
      iRight += 1
    elif iRight >= rightLength:
      '''
      All the items in the right array have been copied over
      '''
      iLeft += 1
    elif left[iLeft] <= right[iRight]:
      iLeft += 1
    else:
      # OR => inversions += len(left[iLeft:])
      inversions += (mid - iLeft)
      iRight += 1

  return inversions

print(countInversions([6,5,4,3,2,1]))
print(countInversions([1,20,6,4,5]))
print(countInversions([1,2,7,4,5,62,5,2,5,6,2,6,7,7,2,4,7,8,3,2,3,6,78,1,2,31,4,734,73,75,2]))
