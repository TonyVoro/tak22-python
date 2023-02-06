name = input('Your name: ')

if name == 'Bob':
    print('Greetings, Bob!')

place = input('Where do you live: ')
if place.lower() == 'saaremaa':
    print('I love Saaremaa!')

age = int(input('Your age: '))
if age < 18:
    print('You are too young to drive a car')
elif age == 18:
    print('Congratulations!')
else:
    print('You can drive a car!')
