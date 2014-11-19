def sum13(nums):
  if len(nums) == 0:
    return 0
  for i, n in enumerate(nums):
    if n == 13:
      nums[i] = 0
      if i+1 < len(nums):
        nums[i+1] = 0

  return sum(nums)

def sum67(nums):
  count = 0
  keepCount = True

  for n in nums:
    if n == 6:
      keepCount = False
    if keepCount:
      count += n
    if n == 7:
      keepCount = True
      
  return count

def has22(nums):
  last2 = False
  for n in nums:
    if n == 2 and last2:
      return True
    if n == 2:
      last2 = True
    else:
      last2 = False
  return False
    
  
