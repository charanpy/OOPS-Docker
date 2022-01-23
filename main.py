from item import Item


item1 = Item('Phone',100,5)
item2 = Item('Laptop', 1000, 10)
item3 = Item('Cable', 10, 5)
item4 = Item('Mouse', 50, 5)
item5 = Item('Keyboard', 75, 5)

# Suppose we need to add unique attribute to laptop then
# item2.has_numPad = True

# item2.pay_rate = 0.7

# item2.apply_discount()
# print(item2.price)

# __dict__ covert attributes -> dictionary
# print(Item.__dict__,"\n",item1.__dict__)

# print(Item.all)
# print(Item.classMethod())

#Static meth
# print(Item.is_integer(7))
item1.name = 'New'
print(item1.name)