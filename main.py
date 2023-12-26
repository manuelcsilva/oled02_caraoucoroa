reposta = ""
kitronik_VIEW128x64.show(0)
num = randint(1, 2)
if num == 1:
    reposta = "Cara"
else:
    reposta = "Coroa"

def on_forever():
    pass
basic.forever(on_forever)
