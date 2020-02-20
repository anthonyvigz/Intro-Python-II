class Item:
  
  def __init__(self, name, description):
    self.name = name
    self.name = description

  def onTake(self):
    print('You have picked up {self.name.capitalize()}')

  def __str__(self):
    return self.name
