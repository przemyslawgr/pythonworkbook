mpg = int(input("Fuel effciency in miles per galon(USA)"))
gallon_in_litres = 3.7854
miles_in_km = 1.6
litres_per_hundred = mpg  * (100 / miles_in_km) * gallon_in_litres
print(f"This is {litres_per_hundred} in l/100km")
