
from art import logo
print(logo)


bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  #yaha p aik variable define karengay jo highets bid ki value store karyga
  highest_bid = 0
  winner = ""
  # bidding_record = {"Sajid":123 , "Saqib":452}
  for bidder in bidding_record:  #dict main for loop key ko uthata hai na k value ko | to yaha bidder main key aegi jo k sajid hai us name ki value ko hold karwanay k liye ye nechay wali line likhnegay. bidding_record[sajid] = 123
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: # yaha p pehli dafa loop par value 0 set hogi kiu k upar highest value 0 hai 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")  



while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  New_bidder = input("Are there any other bidders? Type 'Yes' or 'No'.")
  if New_bidder == "No":
    bidding_finished = True
    find_highest_bidder(bids)
  elif New_bidder == "Yes":
    clear()
    
  

