base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')

is_member = False
is_weekend = False

if is_member:
    discount = 3
    print("User qualifies for membership discount")
else:
    discount = 0
    print("User does not qualify for membership discount")

print('Discount:', discount)
