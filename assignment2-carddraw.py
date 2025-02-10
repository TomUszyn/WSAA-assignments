# Program called assignment2-carddraw.py that uses the Deck of Cards API to draw five cards from a deck of cards.
# The program should display the draw cards. A more advanced version should also detect special hands such as pairs, triples, straights, and all hands of the same suit.
# Author: Tomasz Uszynski

# Import requests module
import requests

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
    print("Drawn Cards:")
    for card in cards:
        print(f"{card['value']} of {card['suit']}")

