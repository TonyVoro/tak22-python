# Leia muutuja abil etteantud tekstis olevate täishäälikute (a, e, i, o, u, õ, ä, ö, ü) arv

letters = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]
i = 0

for c in text:
    if c.lower() in letters:
        i += 1

print("Täishäälikute arv tekstis: ")