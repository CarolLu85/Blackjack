import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_cards = []
player_cards = []
end_of_game = False
def deal_cards(cards_list):
  """ Returns a random number/card from the deck"""
  random_numbers = random.choice(cards)
  cards_list.append(random_numbers)

def score(cards_list):
  """" Take a list of cards and return the score calculated from the cards list."""
  if len(cards_list) == 2 and sum == 21:
    print(f"{cards_list} gets a blackjack, end of the game")
    return 0 

  if 11 in cards_list and sum(cards_list) > 21:
    cards_list.remove(11)
    cards_list.append(1)   
    return sum(cards_list)

def compare(player_score, dealer_score):
  if dealer_score == player_score:
    return "Draw"
  elif player_score == 0:
    return "You win, you got a Blackjack"
  elif dealer_score == 0:
    return "Sorry, You lose. dealer got a blackjack"
  elif player_score > 21:
    return "Sorry, You lose"
  elif dealer_score > 21:
    return "You win"
  elif player_score > dealer_score:
    return "You win"
  else:
    return "You  lose"

for _ in range(2):
  deal_cards(player_cards)
  deal_cards(dealer_cards)  

while not end_of_game:
  player_score = score(player_cards)
  dealer_score = score(dealer_cards)

  if player_score == 0 or computer_score == 0 or player_score > 21:
    end_of_game = True
    print("Game over.")
  else:
    question = input("type 'hit' to get one more card, type 'stand' to exit \n")
    if question == "hit":
      player_cards.append(deal_cards())
    else:
      end_of_game = True
      print("Game over")

  while dealer_score < 17:
    dealer_cards.append(deal_cards())
    dealer_score = sum(dealer_cards)

  print(compare(player_score, dealer_score))



 
#     for c in range(0, length):
#       sum += cards_list[c]
#     if sum > 21:
#       print("socre is bigger than 21")
#     if cards_list == dealer_cards and sum < 17:
#       while sum <= 21:
#         random_numbers = random.choice(cards_list)
#         print(random_numbers)
#         sum = sum + random_numbers 
#         return sum
#     elif cards_list == dealer_cards and sum >= 17:
#       return sum
#     if cards_list == player_cards and sum < 21:
#       while True:
#         question = input("type 'hint' to get one more card, type 'no' to exit \n")
#         if question == "hint":
#           random_numbers = random.choice(cards_list)
#           player_cards.append(random_numbers)
#           print(cards_list)
#           sum = sum + random_numbers
#           print(sum)
#           if sum == 21:
#             return sum   
#           elif sum > 21:
#             length_new = len(cards_list)
#             if 11 in cards_list:
#               cards_list.remove(11)
#               cards_list.append(1)    
#               print(cards_list)
#               for d in range(0, length):
#                 sum += cards_list[d]
#                 print(sum)
#                 return sum
#             else:
#               return sum
#         elif question == "no":
#           sum = sum + 0
#           return sum   
          
# player_score = score(player_cards)
# print(player_score)
# dealer_score = score(dealer_cards)
# print(dealer_score)
# print ("*********")

# End_of_game = False
# while not End_of_game:
#   if player_score == 0:
#     End_of_game = True
#     print("player wins")
#   elif dealer_score == 0:
#     End_of_game = True
#     print("dealer wins")    
#   elif dealer_score == player_score:
#     End_of_game = True
#     print("its a draw")
#   elif player_score > 21:
#     End_of_game = True
#     print("player lose")
#   elif dealer_score > 21:
#     End_of_game = True
#     print("dealer lose")
#   else:
#     if player_score > dealer_score:
#       End_of_game = True   
#       print("player wins")
#     elif player_score < dealer_score:
#       End_of_game = True   
#       print("dealer wins")

# unsolved issues: two Ace in a hand. on what condition, change the two Aces to 1, or just simplely change both of them to 1 and move to the next round.