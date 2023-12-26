input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    kitronik_VIEW128x64.clear()
    kitronik_VIEW128x64.show(reposta, 2, kitronik_VIEW128x64.ShowAlign.Centre, kitronik_VIEW128x64.FontSelection.Big)
})
let reposta = ""
kitronik_VIEW128x64.show("OLED 02", 1, kitronik_VIEW128x64.ShowAlign.Centre, kitronik_VIEW128x64.FontSelection.Big)
kitronik_VIEW128x64.show("CARA", 2, kitronik_VIEW128x64.ShowAlign.Centre, kitronik_VIEW128x64.FontSelection.Big)
kitronik_VIEW128x64.show("OU", 3, kitronik_VIEW128x64.ShowAlign.Centre, kitronik_VIEW128x64.FontSelection.Big)
kitronik_VIEW128x64.show("COROA", 4, kitronik_VIEW128x64.ShowAlign.Centre, kitronik_VIEW128x64.FontSelection.Big)
let num = randint(1, 2)
if (num == 1) {
    reposta = "Cara"
} else {
    reposta = "Coroa"
}

basic.forever(function on_forever() {
    
})
