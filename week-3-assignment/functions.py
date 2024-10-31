def calculate_discount(price, discount_percent):
  
  if isinstance(discount_percent, str) and "%" in discount_percent:
    discount_percent = discount_percent.replace("%", "")
    
  discount_percent = float(discount_percent)
  
  if discount_percent >= 20:
    after_discount = price * (discount_percent / 100)
    return  price - after_discount
  else:
    return price
  
  
price = float(input("Enter the price of the item: "))
discount_percent = input("Enter the discount percentage: ")
    
print(calculate_discount(price, discount_percent))

