dictionary = {
  "name": "Tony",
  "lastname": "Vorontsov",
  "age": 17,
  "birth_year": 2006,
  "residence": "Kuressaare",
  "dessert": "Chocolate"
}

print(dictionary.get('residence'))
print(dictionary['residence'])

dictionary['dessert'] = 'chocolate'

for k, v in dictionary.items():
  print(k, v)

x = dictionary.get("dessert")
print(x)

keys = dictionary.keys()
print(keys)

keyToFind = 'personal_idetification_number'

if dictionary.get('personal_idetification_number') == None:
  print('Isikukood ei eksisteeri selles dictionaris')
else:
  print('Isikukood eksisteerib selles dictionaris')

print("Dictionary suurus: ", len(dictionary), "elementi")

dictionary["height"] = "169cm"

del dictionary['birth_year']
print(dictionary)