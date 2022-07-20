nums = [0, 1, 2, 3]

def no_odds():
  nums1 = []
  for i in nums:
    if i % 2 == 0:
      nums1.append(i)

  print(nums1)
no_odds()    