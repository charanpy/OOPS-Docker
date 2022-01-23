class Item:
  pay_rate = 0.8 # Class Attribute
  all = []

  #self refers to instance(reference of instance)
  def __init__(self,name:str,price:float,quantity=0):
      # Run validation
      assert price >= 0, f"Price {price} is not greater than zero"
      assert quantity >= 0, f"Price {quantity} is not greater than zero"

      #Assign to self object
      self.__name = name
      self.price = price
      self.quantity = quantity

      # Actions to execute
      Item.all.append(self)

  # readOnly
  @property
  def name(self):
    return self.__name

  # setter for read only
  @name.setter
  def name(self,value):
    self.__name = value




  def calculate_total_price(self):
    return self.price*self.quantity

  def apply_discount(self):
    self.price = self.price * self.pay_rate

  @classmethod
  def classMethod(cls):
    print(cls)
    return "I'm class method"

  @staticmethod
  def is_integer(num):
    if isinstance(num, float):
      return num.is_integer()
    elif isinstance(num,int):
      return True
    else:
      return False

  # Representation of instance in string
  def __repr__(self):
      return f"Item('{self.name}',{self.price},{self.quantity})"

