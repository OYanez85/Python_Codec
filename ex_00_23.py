#Ground shipping
#Defining variables
shipping_weight = 4.8
ground_shipping_cost = float()
#Ground Shipping if/elif/else
if shipping_weight <= 2:
  ground_shipping_cost = round(shipping_weight * 1.50 + 20.00, 2)
elif shipping_weight > 2 and shipping_weight <= 6:
  ground_shipping_cost = round(shipping_weight * 3.00 + 20.00, 2)
elif shipping_weight > 6 and shipping_weight <= 10:
  ground_shipping_cost = round(shipping_weight * 4.00 + 20.00, 2)
else:
  ground_shipping_cost = shipping_weight * 4.75 + 20.00
print("Ground Shipping $", ground_shipping_cost)

#Ground shipping premium
#Defining variables
drone_shipping_cost = float()
cost_ground_premium = 125.00
#Ground Shipping Premium if/elif/else
if shipping_weight <= 2:
  drone_shipping_cost = round(shipping_weight * 4.50, 2)
elif shipping_weight > 2 and shipping_weight <= 6:
  drone_shipping_cost = round(shipping_weight * 9.00, 2)
elif shipping_weight > 6 and shipping_weight <= 10:
  drone_shipping_cost = round(shipping_weight * 12.00, 2)
else:
  drone_shipping_cost = round(shipping_weight * 14.25, 2)
print("Ground Shipping Premium $", cost_ground_premium)
print("Ground Shipping Premium $", drone_shipping_cost)
