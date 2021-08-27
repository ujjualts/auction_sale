import art

print(art.logo)

bidfinished=False
bids={}
print("Welcome to auction\n")

def highbid(bids):
  highest_bid=0
  for name in bids:
    amount=bids[name]
    if amount>highest_bid:
      winner=name
      highest_bid=amount 
  print(f'highest bid is {highest_bid}  goes to {winner}')


while not bidfinished:
  name=input("Please enter your name: ")
  bid=int(input("Please enter your bid: "))
  bids[name]=bid
  other_bid=input('Are there any  other bidders: y/n :').lower()
  if other_bid=='n':
    bidfinished=True
highbid(bids)




