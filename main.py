def on_logo_pressed():
    kitronik_VIEW128x64.clear()
    kitronik_VIEW128x64.show(reposta,
        2,
        kitronik_VIEW128x64.ShowAlign.CENTRE,
        kitronik_VIEW128x64.FontSelection.BIG)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

reposta = ""
kitronik_VIEW128x64.show("OLED 02",
    1,
    kitronik_VIEW128x64.ShowAlign.CENTRE,
    kitronik_VIEW128x64.FontSelection.BIG)
kitronik_VIEW128x64.show("CARA",
    2,
    kitronik_VIEW128x64.ShowAlign.CENTRE,
    kitronik_VIEW128x64.FontSelection.BIG)
kitronik_VIEW128x64.show("OU",
    3,
    kitronik_VIEW128x64.ShowAlign.CENTRE,
    kitronik_VIEW128x64.FontSelection.BIG)
kitronik_VIEW128x64.show("COROA",
    4,
    kitronik_VIEW128x64.ShowAlign.CENTRE,
    kitronik_VIEW128x64.FontSelection.BIG)
num = randint(1, 2)
if num == 1:
    reposta = "Cara"
else:
    reposta = "Coroa"

def on_forever():
    pass
basic.forever(on_forever)
