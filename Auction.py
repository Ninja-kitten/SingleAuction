
import random
start = 20
inc = 1
n = 5
lowbound = 20
ubound = 40

def initBidders(size,bidlist,a,b):
  for i in size:
    bidlist.append(random.unif(a,b))
  return (clock,bidlist)

def auctionRound(clock,increment,bidlist):
  if len(bidlist == 1):
    return(clock,bidlist)
  #if the incrementing won't be take it over
  elif clock+increment > sorted(bidlist)[-1]:
    return (clock,[sorted(bidlist)[-1]])
  #if the increment won't screw you over let's do this auciton
  else:
    clock += increment
    for p in bidlist:
      if p < clock:
        bidlist.remove(p)
    return (clock,bidlist)

def runAuction(start,increment,size,a,b):
   clock = start
   bidlist = []
   initBidders(size,bidlist,a,b)
   while len(bidlist > 1):
    (clock,bidlist) = auctionRound(clock,increment,bidlist)
   return clock
