import random
import os
# def clear_screen():
  # os.system("cls")

dealer_cards = []
player_cards = []
end_of_game = False
def deal_cards(cards_list):
  """ Returns a random number/card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_numbers = random.choice(cards)
  return random_numbers

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
  """ Compares the player's score with the dealer's."""
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
  player_cards(deal_cards(player_cards))
  dealer_cards(deal_cards(dealer_cards)) 

print(f"the player got {player_cards}")
print(f"the dealer's second card is {dealer_cards[1]}")

while not end_of_game:
  player_score = score(player_cards)
  dealer_score = score(dealer_cards)

  if player_score == 0 or dealer_score == 0 or player_score > 21:
    print("Game over.")
    end_of_game = True
  else:
    question = input("type 'hit' to get one more card, type 'stand' to exit \n")
    if question == "hit":
      player_cards.append(deal_cards(player_cards))
      print(f"now your cards are {player_cards}")
    else:
      print("Game over")
      end_of_game = True

  while dealer_score < 17:
    dealer_cards.append(deal_cards(dealer_cards))
    dealer_score = sum(dealer_cards)


print(f"the dealer got {dealer_cards}") 
print(f"the player got {player_cards}")
print(compare(player_score, dealer_score))


# unsolved issues: two Ace in a hand. on what condition, change the two Aces to 1, or just simplely change both of them to 1 and move to the next round.