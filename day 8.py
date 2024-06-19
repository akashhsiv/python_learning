cars =('bmw ', 'audi' ,' benz ', 'subru')
for car in cars:
    if car == 'audi':
       print(car.upper())
    else:
       print(car.title())
       request_topplings='mushrooms'
if request_topplings != 'anchloppies':
    print("hold the anchloppies!")
    answer = 20
if answer !=47:
    print("that is not correctplease try again")
    banned_users = ['andrew', 'atat', 'david','kumar']
    user = 'theresa'
if user not in banned_users:
    print(f"{user.title()}, you can text as you wish")
age = 28
if age >= 28:
    print("you are old enough to marry")
    print("have you married yet")
age = 15
if age >=18:
    print("you are old enough to vote")
    print("are you voted yet")
else:
    print("you are not old enough to vote yet")
    print("please apply for voterid as soon as  you turn 18")
age = 17
if age <=4:
    print("your admission cost is 0$")
elif age <=18:
    print("your admission cost is 25$")
else:
    print("your admission cost is 50$")
age = 22
if age <4:
    price = 0
elif age <20:
    price = 25
else:
    price = 50
print(f"your admisson cost is ${price}")

ages = 20
if age <4:
    price = 20
elif age <18:
    price = 40
elif age <60:
    price = 30
else:
    price = 20
print(f"you admission cost is ${price}.")
requested_topplings =['mushroom','chees']
if "mushroom" in requested_topplings:
    print("adding mushroom")
if "pepporni" in requested_topplings:
    print("adding pepproni")
if "chees" in requested_topplings:
    print("adding chees")
print("\nfinished making your pizza!!")
age = 17
if age <2:
    point =  8
elif age <8:
    point = 9
elif age <18:
    point = 0
print(f"this is just a {point}!!!.")
requested_toppings =['mushroom','pepporoni', 'cheees', 'greenpepper']
for requested_topping in requested_toppings:
    print(f"adding{requested_topping}.")
print("\nFinished making your pizza!")

requested_toppings = ['mushroom', 'greenpepper', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'greenpepper':
        print("Adding green pepper to your pizza.")
    else:
        print(f"Sorry, we are out of {requested_topping} now.")

print("\nFinished making your pizza!")