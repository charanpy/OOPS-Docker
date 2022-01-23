from item import Item

class Phone(Item):
  def __init__(self, name: str, price: float, quantity=0,broken_phone=0):
      
      super().__init__(name, price, quantity)

      assert broken_phone >= 0

      self.broken_phone = broken_phone







