items={"phone":200,"tv":500,"laptop":300,"remote":30,"mouse":50}
print(items)

cart={}
while True:
    product=input("wich items do you want to buy")
    if product == "stop":
         break
    quantity=int(input("how many do you want to buy"))
    cart[product]=quantity
    print(cart)
for key,value in cart.items():
    print (key,value)
   
        
