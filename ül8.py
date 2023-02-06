n = int(input('Aasta: '))

if n % 400 or (n % 4 == 0 and n % 100 != 0):
    print(n, 'on liigaasta')
else:
    print(n, 'on lihtaasta')