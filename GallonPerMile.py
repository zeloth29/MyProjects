LastFillMile = float(input("What was the car Mileage last time it was filled?\n"))
CurrentMile = float(input("What is the current car mileage?\n"))
LitreReq = int(input("How many Litres does the tank take to fill?\n"))
Distance = round(float(LastFillMile)-float(CurrentMile), 3)
Gallon = float(LitreReq) * 0.22
GallonPerMile = Gallon / Distance
print("The car takes " + str(GallonPerMile) + "G/mile")