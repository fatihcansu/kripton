#https://leetcode.com/problems/house-robber/
houses_one=[5,2,3,1,4,1,1,4]
houses_two=[4,9,1,10,21,4]
houses_three=[4,1,1,4]
def robbery(houses):
  if len(houses)==0:
    return 0
  if len(houses)==1:
    return houses[0]
  if len(houses)==2:
    return [max(houses)]
  first=0
  second=0
  for i in range(0,len(houses)):
    first, second = max(second+houses[i],first), first 
  return first


print(robbery(houses_one))
print(robbery(houses_two))
print(robbery(houses_three))
