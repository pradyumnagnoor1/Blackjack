# Blackjack

In this program, I created a version of blackjack that can be played in the terminal of the program. I wanted to make this program unique so I created ascii playing cards to make the program more visually appealing. This program implements many functions. The first one is a function that gets the int value of the arguement 'card'. If the card was a Jack, Queen, or King the function would return the value 10. If it was an Ace it would return an 11. If it was anything else it would return the int value of that card. The next function handValue that returns the total value of the argument 'hand'. The variable value finds the sum by iterating through the cards in the hand and using the cardValue function to convert the cards into int values. The next function is a draw card function that contains 2 lists (suits and ranks) and an empty list called deck. In this function I implemented a nested for loop that firsts creates a variable suit that iterates through the suits list and under that for loop is another for loop that contains a variable rank that iterates through the ranks list. This nested for loop allows me to create a deck of 52 cards.  
