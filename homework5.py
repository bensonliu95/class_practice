import random
b=["♥","♣","♦","♠"]
n=["3","4","5","6","7","8","9","10","11","12","13","A","2"]
card=[]
for x in range(4):
    for y in range(13):
        card.append(b[x]+n[y])
print(card)