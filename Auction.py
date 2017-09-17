
import random
start = 20
clock = start
increment = 1
n = 5
bidders = []
lowbound = 20
ubound = 40

def initBidders(size,bidlist,a,b):
  for i in size:
    bidlist.append(random.unif(a,b))
  return bidlist




#value tie  
if sorted(bidders)[-1]== sorted(bidders)[-2]:
  if n == 2:
    while clock+increment < bidders[0]:
      clock += increment
  else:
    while clock <= sorted(bidders)[-3]:
      clock += increment
else:
  while clock < sorted(bidders)[-2]:
    clock+= increment
