skrito_stevilo = "12"
odgovor = raw_input("Ugani skrito stevilo med 1 in 20:")
while odgovor != skrito_stevilo:
    odgovor = raw_input("Poskusi znova:")
if odgovor == skrito_stevilo:
    print("Pravilno")