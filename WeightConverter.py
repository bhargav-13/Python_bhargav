weight = int(input("Enter Weight:"))

unit = input("Enter kilogran or Pound  (K/L) :")

if unit == "K":
    weight = weight* 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight/2.205
    unit = "kgs."
else:
    print(f" {unit} is not valid")


weight= round(weight, 2)

print(f"your weight is= {weight}{unit}")
