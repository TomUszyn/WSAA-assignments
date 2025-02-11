# Program called assignment2-carddraw.py that uses the Deck of Cards API to draw five cards from a deck of cards.
# The program should display the draw cards. A more advanced version should also detect special hands such as pairs, triples, straights, and all hands of the same suit.
# Author: Tomasz Uszynski

# Import requests module
import requests

# Import Counter class from collections module
from collections import Counter

# Get a deck-ID
deckId = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/").json()["deck_id"]

# API URL to draw 5 cards from the same deck
url = f"https://deckofcardsapi.com/api/deck/{deckId}/draw/?count=5"

# Send GET request
response = requests.get(url)

# Parse JSON response
if response.status_code == 200:
    data = response.json()
    cards = data.get("cards", [])  # Get drawn cards
    
    # Display drawn cards
    print("\nDrawn Cards:")
    for card in cards:
        print(f"{card['value']} of {card['suit']}")
            
    # Extract values and suits
    values = [card['value'] for card in cards]
    suits = [card['suit'] for card in cards]
    
    # Count occurrences of each value and suit
    valueCount = Counter(values)
    suitCount = Counter(suits)
    
    # Check for pairs, triples, straight, or all same suit
    pairs = [value for value, count in valueCount.items() if count == 2]
    triples = [value for value, count in valueCount.items() if count == 3]
    allSameSuit = len(suitCount) == 1  # All cards have the same suit
    
    # Define the sorted value order
    sortedValues = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'ACE']
        
    # Get the index of a card value in the predefined sorted order
    def getCardValueIndex(value):
        return sortedValues.index(value)
    
    # Sort card values by their index in the sorted order
    sortedCards = sorted(values, key=getCardValueIndex)
    
    # Check for a straight
    straight = all(getCardValueIndex(sortedCards[i]) == getCardValueIndex(sortedCards[0]) + i for i in range(5))
    
    # Congratulate user if any special hand is found
    if pairs or triples or allSameSuit or straight:
        print("\nCongratulations! You got a special hand!")
        if pairs:
            print(f"Pair(s): {', '.join(pairs)}\n")
        if triples:
            print(f"Triple: {', '.join(triples)}\n")
        if allSameSuit:
            print("All cards are of the same suit!\n")
        if straight:
            print("You have a straight!\n")
    else:
        print("\nNo special hand found.\n")
else:
    print("Failed to draw cards.")



# To understand how to use the Deck of Cards API visit: https://www.youtube.com/watch?v=qF6zUptypGE and https://deckofcardsapi.com/.
# To see how to take JSON data from URL to Python visit: https://reqbin.com/code/python/rituxo3j/python-requests-json-example.
# To see how to use the Counter class visit: https://www.geeksforgeeks.org/python-counter-objects-elements/.
