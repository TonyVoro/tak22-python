import math

n = input('Sisesta string: ').strip() 

print(len(n))
i = math.floor(len(n) / 2)

if len(n) >= 7 and len(n) % 2 == 1:
    print('Vastab tingimustele')
    i = math.floor(len(n) / 2)
    print(n[i-1], n[i], n[i+1])
else:
    print('Sisend ei vasta tingimustele')
