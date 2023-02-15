### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # required card.value should be ==
    if card.value = 1:
      return True
    else
      return False
   
# spelling error, required def instead of dif, indentation on if statement also incorrect.
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    # need to state card1 not just card in return.
    return card
  else:
    return card2
  

# def requires indentation to ensure it is a method part of the class.
def cards_total(self, cards):
  # total has not been declared as an int variable.
  total
  for card in cards:
    total += card.value
    # will need to stringyfy total for concatonation as you cannot mix a string and an int.
    return "You have a total of" + total
  
```
