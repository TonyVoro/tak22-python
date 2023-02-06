mylist = ["banaan", "õun", "pirn"]
print(mylist[0])

mylist.append("kookos")
print(mylist[3])

mylist[1] = "kirss"

if 'pirn' in mylist:
    print("Jah, 'pirn' eksisteerib selles listis: ", mylist)

mylistlength = len(mylist)
print("Listi suurus on: ", mylistlength)

mylist.remove("banaan")
print(mylist)

mylist.sort(reverse = True)
print(mylist)

