class atm(object):
  """
  
  """

  def __init__(money_given,pin,enter_the_card,):
    self.money_given = money_given
    self.pin = pin
    self.enter_the_card = enter_the_card
    

  def money_given(self):
    print("given")

  def enter_the_card(self):
    print("entered")

  def pin(self):
    print("wrong pin")
    



a = card("A6", "red", "audi", 80)

print(card.money_given())

print(enter_the_card())

print( pin())