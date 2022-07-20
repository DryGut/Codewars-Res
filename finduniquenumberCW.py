arr = [ 0, 0, 0.55, 0, 0 ]
def find_uniq(arr):

  print([i for i in set(arr) if arr.count(i) == 1][0])
  

find_uniq(arr)