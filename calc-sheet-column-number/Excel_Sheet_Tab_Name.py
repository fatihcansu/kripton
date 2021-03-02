alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def ColumnNumber(Cname):

  result=0
  for i in range(0,len(Cname)):

    result=result+alphabet.index(Cname[i])+1*(26**(len(Cname)-1-i))
  return result
