PaintRequired = 0
perL = 11

TotalArea = int(input("What is the total area of all the walls?\n"))
UnpaintableArea = int(input("What is the total area of the unpaintable surfaces?\n"))
PaintableArea = TotalArea - UnpaintableArea

Coats = int(input("How many coats is needed?\n"))
PaintRequired = (PaintableArea * Coats)/perL

print("You will need " + str(round(PaintRequired, 2)) + " Litres of Paint")

CostPLitre = float(input("How much does 1 Litre of paint cost?\n£"))
Cost = PaintRequired * CostPLitre
print("It will cost you £" + str(round(Cost, 2)))