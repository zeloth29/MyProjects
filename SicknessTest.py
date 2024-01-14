temp = 0
fever = 0
total = 0
hour = 1
while hour < 7:
    temp = int(input("Enter temperature: "))
    if temp < 30 or temp > 44:
        print("Invalid temperature. Temperature must be between 30 and 44.")
        continue
    if temp > 37:
        fever = fever + 1
    total = total + temp
    hour = hour + 1
average = round(total / hour, 1)  # round to 1 decimal place
print("Average temperature:", average)
print("Incidents of fever:", fever)