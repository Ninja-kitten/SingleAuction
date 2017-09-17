
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

def auctionRound(clock,increment,bidlist):
  #if the incrementing won't be take it over
  if clock+increment > sorted(bidlist)[-1]:
    return clock
  #if the increment won't screw you over let's do this auciton
  else:
    #see if the clock is already past the second place
    if clock > sorted(bidlist)[-2]:
      return clock
    else:
      clock += increment
      return clock
    
