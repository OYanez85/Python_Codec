# Orders number divisible by 11 will receive the coupon
# order263
order_263_r = 263 % 11
print(order_263_r)

order_263_coupon = 'Yes'
if order_263_r % 11 == 0:
  order_263_coupon ='Yes'
  print(order_263_coupon)
else:
  order_263_coupon = 'No'
  print (order_263_coupon)

#order264
order_264_r = 264 % 11
print(order_264_r)

order_264_coupon = 'Yes'
if order_264_r % 11 == 0:
  order_264_coupon ='Yes'
  print(order_264_coupon)
else:
  order_263_coupon = 'No'
  print (order_264_coupon)
